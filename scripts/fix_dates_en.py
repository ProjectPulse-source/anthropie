import re
import sys
from pathlib import Path

# Console Windows = cp1252 : n'encode ni « → » ni « ⚠ » ni « ✓ ». Enjeu accru
# ici : ce script MODIFIE le front matter. Un crash en cours d'impression du
# journal laisserait une passe partiellement appliquee sans compte rendu lisible.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

CORRECTIONS = {
    "awp-01": "2026-04-05",
    "awp-02": "2026-04-06",
    "awp-03": "2026-04-06",
    "awp-04": "2026-04-06",
}
FIELDS_TO_UPDATE = ["date", "publication_date"]

def patch_front_matter(text, new_date):
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None, "pas de front matter détecté"
    fm_old = m.group(1)
    fm_new = fm_old
    changes = []
    for field in FIELDS_TO_UPDATE:
        pattern = rf"(^\s*{field}\s*:\s*['\"]?)([^'\"\n#]+?)(['\"]?\s*(?:#|$))"
        def replacer(match):
            old_val = match.group(2).strip().split("T")[0]
            if old_val == new_date:
                return match.group(0)
            changes.append(f"{field}: {old_val} → {new_date}")
            return f"{match.group(1)}{new_date}{match.group(3)}"
        fm_new = re.sub(pattern, replacer, fm_new, count=1, flags=re.MULTILINE)
    if not changes:
        return text, "aucun changement nécessaire"
    new_text = text.replace(f"---\n{fm_old}\n---", f"---\n{fm_new}\n---", 1)
    return new_text, "; ".join(changes)

print("# Correction des dates front matter EN\n")
for slug, new_date in CORRECTIONS.items():
    md = Path(f"content/awp/{slug}.en.md")
    if not md.exists():
        print(f"⚠ {slug.upper()} : {md} introuvable, ignoré")
        continue
    old_text = md.read_text(encoding="utf-8")
    new_text, msg = patch_front_matter(old_text, new_date)
    if new_text is None:
        print(f"⚠ {slug.upper()} : {msg}")
        continue
    if new_text == old_text:
        print(f"= {slug.upper()} : {msg}")
        continue
    md.write_text(new_text, encoding="utf-8")
    print(f"✓ {slug.upper()} ({md.name}) : {msg}")

print("\nRelance la vérification :")
