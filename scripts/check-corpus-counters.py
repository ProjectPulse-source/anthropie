#!/usr/bin/env python3
"""Linter cohérence corpus AWP — détecte les chiffres durs désynchronisés.

Vérité runtime : compte les AWP par glob de content/awp/awp-*.md (FR) et
content/awp/awp-*.en.md (EN). Puis scanne content/, layouts/, i18n/, data/
à la recherche de mentions textuelles "cinq Anthropie Working Papers",
"five AWP", "5 Anthropie Working Papers", etc. qui divergent de la vérité.

Sortie : rapport ordonné par chemin/ligne. Code de sortie 0 si aucune
divergence, 1 sinon.

Stdlib pure. Python 3.10+. Encodage UTF-8 forcé pour Windows.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Conversion mots → entiers (FR + EN, 1 à 10)
# ---------------------------------------------------------------------------
WORDS_TO_INT_FR = {
    "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5,
    "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10,
}
WORDS_TO_INT_EN = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
}


# ---------------------------------------------------------------------------
# Patterns de détection (regex, insensibles à la casse)
# ---------------------------------------------------------------------------
PATTERNS = [
    # FR mots AWP (avec ou sans "Anthropie")
    (re.compile(
        r"\b(un|deux|trois|quatre|cinq|six|sept|huit|neuf|dix)\s+"
        r"(?:Anthropie\s+)?Working\s+Papers?\b",
        re.IGNORECASE,
    ), "fr_word"),
    # FR mots AWP sigle (sans "un" : article indéfini polysémique, on n'écrit
    # pas "un AWP" comme compteur cardinal — on dit "1 AWP" si besoin)
    (re.compile(
        r"\b(deux|trois|quatre|cinq|six|sept|huit|neuf|dix)\s+AWP\b",
        re.IGNORECASE,
    ), "fr_word"),
    # EN mots AWP avec qualificatif "Anthropy" ou "Anthropie"
    (re.compile(
        r"\b(one|two|three|four|five|six|seven|eight|nine|ten)\s+"
        r"(?:Anthropy|Anthropie)\s+Working\s+Papers?\b",
        re.IGNORECASE,
    ), "en_word"),
    # EN mots AWP variante (sans qualificatif)
    (re.compile(
        r"\b(one|two|three|four|five|six|seven|eight|nine|ten)\s+"
        r"Working\s+Papers?\b",
        re.IGNORECASE,
    ), "en_word"),
    # EN mots AWP sigle (sans "one" : article indéfini polysémique en EN aussi)
    (re.compile(
        r"\b(two|three|four|five|six|seven|eight|nine|ten)\s+AWP\b",
        re.IGNORECASE,
    ), "en_word"),
    # Numériques AWP (FR + EN, ambigu sur la langue → détection par chemin)
    (re.compile(
        r"\b(\d+)\s+(?:Anthropie|Anthropy)?\s*Working\s+Papers?\b",
        re.IGNORECASE,
    ), "numeric"),
    # Numériques AWP sigle
    (re.compile(
        r"\b(\d+)\s+AWP\b",
        re.IGNORECASE,
    ), "numeric"),
]


# ---------------------------------------------------------------------------
# Normalisation HTML inline (tolérer <em>, <i>, <strong>, <b>, <span>)
# ---------------------------------------------------------------------------
# Le hero index.html écrit p.ex. "cinq <em>Anthropie Working Papers</em>" ;
# sans normalisation le pattern \b(cinq)\s+Anthropie\b ne matche pas car le
# tag <em> est intercalé. On retire les tags inline simples avant matching,
# mais on garde la ligne d'origine pour l'extrait affiché à l'utilisateur.
INLINE_TAGS_RE = re.compile(
    r"</?(?:em|i|strong|b|span|a|code|kbd|mark|small|sub|sup)\b[^>]*>",
    re.IGNORECASE,
)


def _strip_inline_html(line: str) -> str:
    """Retire les tags HTML inline simples, conserve le reste."""
    return INLINE_TAGS_RE.sub("", line)


# ---------------------------------------------------------------------------
# Exclusions
# ---------------------------------------------------------------------------
EXCLUDED_PREFIXES = (
    ".git/", ".git\\",
    "node_modules/", "node_modules\\",
    "public/", "public\\",
    "resources/", "resources\\",
    ".hugo_cache/", ".hugo_cache\\",
    "docs/archive/", "docs\\archive\\",
    "scripts/", "scripts\\",  # exclure le linter lui-même
)
EXCLUDED_FILES = (
    "BRIEF-CLAUDE-CODE-REDESIGN.md",
)
SCANNED_DIRS = ("content", "layouts", "i18n", "data")
SCANNED_EXTS = (".md", ".html", ".toml", ".yaml", ".yml")


def _is_excluded(rel_path: str) -> bool:
    """Vrai si le chemin (forme relative) est exclu du scan."""
    rp = rel_path.replace("\\", "/")
    if any(rp.startswith(p.replace("\\", "/")) for p in EXCLUDED_PREFIXES):
        return True
    if Path(rp).name in EXCLUDED_FILES:
        return True
    return False


def _detect_lang(rel_path: str) -> str:
    """Détecte la langue d'un fichier par convention de nommage du repo."""
    rp = rel_path.replace("\\", "/")
    name = Path(rp).name.lower()
    if name.endswith(".en.md") or name.endswith(".en.html"):
        return "en"
    if name.endswith(".fr.md") or name.endswith(".fr.html"):
        return "fr"
    if rp == "i18n/en.toml" or name == "en.toml":
        return "en"
    if rp == "i18n/fr.toml" or name == "fr.toml":
        return "fr"
    return "fr"  # defaultContentLanguage du site


def count_awps(repo_root: Path) -> tuple[int, int]:
    """Compte les AWPs FR + EN par glob du filesystem."""
    fr = sorted(repo_root.glob("content/awp/awp-*.md"))
    fr = [p for p in fr if not p.name.endswith(".en.md")
          and not p.name.startswith("_index")]
    en = sorted(repo_root.glob("content/awp/awp-*.en.md"))
    en = [p for p in en if not p.name.startswith("_index")]
    return len(fr), len(en)


def scan_file(rel_path: str, abs_path: Path, truth_fr: int,
              truth_en: int) -> list[tuple[int, str, int, int, str]]:
    """Scanne un fichier, retourne [(ligne, lang, claimed, truth, extrait)]."""
    out: list[tuple[int, str, int, int, str]] = []
    try:
        text = abs_path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return out

    lang = _detect_lang(rel_path)
    lines = text.splitlines()

    for lineno, line in enumerate(lines, start=1):
        # Ligne dé-taguée pour matching ; ligne originale conservée pour extrait
        line_stripped = _strip_inline_html(line)
        for pat, ptype in PATTERNS:
            for m in pat.finditer(line_stripped):
                token = m.group(1).lower()
                if ptype == "fr_word":
                    claimed = WORDS_TO_INT_FR.get(token)
                elif ptype == "en_word":
                    claimed = WORDS_TO_INT_EN.get(token)
                else:  # numeric
                    try:
                        claimed = int(token)
                    except ValueError:
                        continue
                if claimed is None:
                    continue
                truth = truth_fr if lang == "fr" else truth_en
                if claimed == truth:
                    continue
                extrait = line.strip()
                if len(extrait) > 100:
                    # Centrer autour du match si possible
                    start = max(0, m.start() - 30)
                    extrait = extrait[start:start + 100]
                out.append((lineno, lang, claimed, truth, extrait))
                break  # une seule détection par ligne suffit
    return out


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    truth_fr, truth_en = count_awps(repo_root)

    print(f"Vérité corpus : {truth_fr} AWP FR | {truth_en} AWP EN")
    print()

    all_findings: list[tuple[str, int, str, int, int, str]] = []

    for sub in SCANNED_DIRS:
        base = repo_root / sub
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in SCANNED_EXTS:
                continue
            rel = path.relative_to(repo_root).as_posix()
            if _is_excluded(rel):
                continue
            findings = scan_file(rel, path, truth_fr, truth_en)
            for f in findings:
                all_findings.append((rel,) + f)

    # Tri stable par chemin puis ligne
    all_findings.sort(key=lambda t: (t[0], t[1]))

    if not all_findings:
        print("Aucune divergence détectée. ✓")
        return 0

    print(f"Divergences détectées : {len(all_findings)}")
    print()
    for rel, lineno, lang, claimed, truth, extrait in all_findings:
        print(f"{rel}:{lineno} [{lang}] — claimed={claimed} truth={truth} | "
              f"{extrait}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
