#!/usr/bin/env python3
"""
Pose le verbatim canonique de la definition en OUVERTURE des descriptions
Zenodo qui en sont depourvues (backlog D2, GO auteur du 2026-08-02).

Etat constate le 2026-08-02 (audit) :
  - 8 records FR : verbatim en ouverture -> conformes
  - AWP-01/05 EN : verbatim en ouverture -> conformes
  - AWP-02/04/06 EN + AWP-07 FR : verbatim EN INCISE dans le corps
    -> conformes par decision actee (commit e6c6b8a : "AWP-06 EN inchange,
       verbatim deja en incise"). NE PAS TOUCHER.
  - AWP-03 EN, AWP-07 EN, AWP-08 FR, AWP-08 EN : verbatim ABSENT -> ce script.

Ne reecrit JAMAIS le texte de l'auteur : ajoute seulement un paragraphe
liminaire. Idempotent (ne pose rien si le verbatim est deja present).

Usage :
    python scripts/zenodo_fix_verbatim.py            # dry-run
    python scripts/zenodo_fix_verbatim.py --apply
"""
import os, sys, json, time, re, html, urllib.request, urllib.error

TOKEN = os.environ.get('ZENODO_TOKEN')
if not TOKEN:
    sys.exit("ERREUR : variable ZENODO_TOKEN absente")
APPLY = "--apply" in sys.argv

VERBATIM = {
    "fr": "L’anthropie est l’hypothèse selon laquelle les systèmes "
          "sociaux déplacent le désordre plutôt qu’ils ne le résolvent.",
    "en": "Anthropy is the hypothesis that social systems displace disorder "
          "rather than resolve it.",
}
# Marqueurs de detection (normalises, sans accents)
MARK = {"fr": "deplacent le desordre plutot qu",
        "en": "displace disorder rather than resolve it"}

TARGETS = [
    ("AWP-03 EN", "19434094", "en"),
    ("AWP-07 EN", "21200288", "en"),
    ("AWP-08 FR", "21506320", "fr"),
    ("AWP-08 EN", "21507249", "en"),
]


def norm(s):
    s = re.sub("<[^>]+>", " ", html.unescape(s or ""))
    for a, b in [("’", "'"), ("é", "e"), ("è", "e"), ("ê", "e"),
                 ("ô", "o"), ("à", "a"), (" ", " "), ("î", "i"),
                 ("â", "a")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def api(path, method="GET", data=None):
    req = urllib.request.Request(f"https://zenodo.org/api{path}", method=method)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    body = None
    if data is not None:
        req.add_header("Content-Type", "application/json")
        body = json.dumps(data).encode("utf-8")
    with urllib.request.urlopen(req, data=body, timeout=30) as r:
        raw = r.read()
        return json.loads(raw) if raw else {}


print("=" * 72)
print(f"Verbatim canonique Zenodo — mode : {'APPLY' if APPLY else 'DRY-RUN'}")
print("=" * 72)

done = 0
for label, rec, lang in TARGETS:
    print(f"\n--- {label} (record {rec}) ---")
    try:
        dep = api(f"/deposit/depositions/{rec}")
    except Exception as e:
        print(f"  [ERR] lecture : {e}")
        continue
    meta = dep.get("metadata", {})
    desc = meta.get("description", "") or ""

    if MARK[lang] in norm(desc):
        print("  [SKIP] verbatim deja present")
        continue

    para = f"<p>{VERBATIM[lang]}</p>"
    # Si la description n'est pas balisee, on enveloppe le corps existant.
    new_desc = (para + " " + desc) if desc.lstrip().startswith("<") \
        else (para + " <p>" + desc.strip() + "</p>")

    print(f"  [ADD] paragraphe liminaire ({len(desc)} -> {len(new_desc)} car.)")
    print(f"        \"{VERBATIM[lang][:70]}...\"")
    if not APPLY:
        continue

    try:
        api(f"/deposit/depositions/{rec}/actions/edit", method="POST")
        nm = dict(meta)
        nm["description"] = new_desc
        api(f"/deposit/depositions/{rec}", method="PUT", data={"metadata": nm})
        api(f"/deposit/depositions/{rec}/actions/publish", method="POST")
        print("  [OK] republie")
        done += 1
        time.sleep(1)
    except urllib.error.HTTPError as e:
        print(f"  [ERR] HTTP {e.code} : {e.read().decode('utf-8','replace')[:200]}")
        try:
            api(f"/deposit/depositions/{rec}/actions/discard", method="POST")
            print("  [ROLLBACK] brouillon annule")
        except Exception:
            pass

print("\n" + "=" * 72)
if APPLY:
    print(f"Records mis a jour : {done}/{len(TARGETS)}")
else:
    print("DRY-RUN termine. Pour appliquer : --apply")
