#!/usr/bin/env python3
"""Linter encodage console — détecte les scripts qui plantent en imprimant leur rapport.

MOTIF (2026-08-11). La console Windows sort en cp1252, qui ne sait encoder ni
« ✓ » ni « → » ni « ⚠ » ni le moindre emoji. Un `print()` contenant un de ces
caractères lève `UnicodeEncodeError` et le script sort **1**.

Ce mode de défaillance est pernicieux pour une raison précise : sur un linter,
l'échec technique est **indiscernable du succès de la détection**. `check-corpus-
counters.py` sortait 1 sur corpus sain — parce que le crash se produisait en
imprimant la ligne « Aucune divergence détectée. ✓ ». Or `CLAUDE.md` déclare ce
gate bloquant avant commit, et la consigne dit de lire le code de sortie. Le gate
était donc rouge en permanence, et son docstring annonçait « Encodage UTF-8 forcé
pour Windows » sans le faire : état déclaré ≠ état réel.

CE QUE CE LINTER VÉRIFIE
    Un fichier est signalé si et seulement si :
      (1) un littéral passé à `print()` contient un caractère hors cp1252, ET
      (2) le fichier ne reconfigure pas réellement `sys.stdout`.
    La condition (2) est ce qui évite de crier sur un fichier déjà réparé.

    ⚠ `# -*- coding: utf-8 -*-` N'EST PAS une garde : ce cookie déclare
    l'encodage de la SOURCE, jamais celui de stdout. Deux fichiers du dépôt ont
    été classés « protégés » à tort sur ce critère avant correction.

CORRECTIF ATTENDU (3 lignes, après les imports) :
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

PORTÉE — borne inférieure assumée. L'analyse est statique (AST) : elle voit les
littéraux, pas un caractère arrivant par variable ou lu d'un fichier de données.
Elle ne remplace donc pas l'exécution ; elle attrape le cas courant, qui est
celui des messages en dur. Ni exécution, ni réseau, ni écriture.

Sortie : 0 si aucun fichier fautif, 1 sinon. Stdlib pure.
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

# Ce linter s'applique à lui-même la règle qu'il fait respecter.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent

# Reconfigurations qui protègent réellement le flux de sortie.
# Le cookie `coding:` est délibérément absent : il ne protège rien.
REAL_GUARD = re.compile(
    r"sys\.stdout\.reconfigure"
    r"|io\.TextIOWrapper\s*\(\s*sys\.stdout"
    r"|codecs\.getwriter\s*\([^)]*\)\s*\(\s*sys\.stdout"
    r"|sys\.stdout\s*="
    r"|environ\s*\[\s*[\"']PYTHONIOENCODING"
    r"|environ\s*\[\s*[\"']PYTHONUTF8"
)


def unencodable(text: str) -> set[str]:
    """Caractères que cp1252 ne sait pas encoder."""
    out = set()
    for ch in text:
        if ord(ch) < 128:
            continue
        try:
            ch.encode("cp1252")
        except UnicodeEncodeError:
            out.add(ch)
    return out


class PrintScanner(ast.NodeVisitor):
    """Ne retient que les littéraux atteignant réellement print()."""

    def __init__(self) -> None:
        self.hits: list[tuple[int, str]] = []

    def visit_Call(self, node: ast.Call) -> None:
        func = node.func
        if isinstance(func, ast.Name) and func.id == "print":
            bad: set[str] = set()
            for arg in node.args:
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                        bad |= unencodable(sub.value)
            if bad:
                self.hits.append((node.lineno, "".join(sorted(bad))))
        self.generic_visit(node)


def targets() -> list[Path]:
    seen: dict[Path, None] = {}
    for path in sorted(REPO_ROOT.glob("scripts/*.py")) + sorted(REPO_ROOT.glob("*.py")):
        seen.setdefault(path.resolve(), None)
    return list(seen)


def main() -> int:
    offenders: list[tuple[Path, list[tuple[int, str]]]] = []
    scanned = 0
    guarded = 0

    for path in targets():
        try:
            src = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"  [illisible] {path.name} : {exc}", file=sys.stderr)
            continue
        try:
            tree = ast.parse(src)
        except SyntaxError as exc:
            print(f"  [syntaxe]   {path.name} : ligne {exc.lineno}", file=sys.stderr)
            continue

        scanned += 1
        scanner = PrintScanner()
        scanner.visit(tree)
        if not scanner.hits:
            continue
        if REAL_GUARD.search(src):
            guarded += 1
            continue
        offenders.append((path, scanner.hits))

    print(f"Encodage console : {scanned} script(s) analysé(s), "
          f"{guarded} protégé(s) par une garde explicite.")

    if not offenders:
        print("\nAucun script ne plante à l'impression. ✓")
        return 0

    print(f"\n{len(offenders)} script(s) planteront sous console cp1252 :\n")
    for path, hits in offenders:
        rel = path.relative_to(REPO_ROOT).as_posix()
        print(f"  {rel}")
        for lineno, chars in hits:
            print(f"      ligne {lineno:>4} : {chars}")
    print("\nCorrectif — 3 lignes après les imports (nécessite `import sys`) :")
    print('    if hasattr(sys.stdout, "reconfigure"):')
    print('        sys.stdout.reconfigure(encoding="utf-8")')
    print('        sys.stderr.reconfigure(encoding="utf-8")')
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
