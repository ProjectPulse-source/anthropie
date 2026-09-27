"""Search Console (API officielle, gratuite) en LECTURE : requêtes, pages, clics, impressions, CTR, position.

    python search_console.py sites
    python search_console.py requetes [--jours 28] [--dimension query|page|country|device] [--limite 50]

Authentification : compte de service Google, ajouté comme utilisateur « Restreint » (lecture) de la
propriété — aucun droit d'écriture sur le site ni sur la Search Console. Clé JSON hors dépôt :
D:\\PRO\\01_SITE\\_secrets\\search_console_sa.json (surcharge : SEARCH_CONSOLE_SA). Jamais affichée.
Jeton : JWT RS256 signé localement (bibliothèque `cryptography`, déjà présente), aucune dépendance Google.
Arbitrage API-MCP du 27/09, point 4 ; gestes de l'auteur : GUIDE_GESTES_AUTEUR_OUTILLAGE.md, G8.
"""
from __future__ import annotations

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

CLE = Path(os.environ.get("SEARCH_CONSOLE_SA", r"D:\PRO\01_SITE\_secrets\search_console_sa.json"))
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
API = "https://searchconsole.googleapis.com/webmasters/v3"
PROPRIETE = os.environ.get("SEARCH_CONSOLE_SITE", "sc-domain:stephane-lalut.com")


def _b64(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def jwt(sa: dict, maintenant: int | None = None) -> str:
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    t = int(maintenant or time.time())
    entete = _b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    corps = _b64(json.dumps({"iss": sa["client_email"], "scope": SCOPE, "aud": sa["token_uri"],
                             "iat": t, "exp": t + 3600}).encode())
    cle = serialization.load_pem_private_key(sa["private_key"].encode(), password=None)
    sig = cle.sign(f"{entete}.{corps}".encode(), padding.PKCS1v15(), hashes.SHA256())
    return f"{entete}.{corps}.{_b64(sig)}"


def jeton() -> str:
    if not CLE.is_file():
        sys.exit(f"CLÉ ABSENTE : {CLE} — geste G8 du guide (compte de service en lecture)")
    sa = json.loads(CLE.read_text(encoding="utf-8"))
    data = urllib.parse.urlencode({"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                                   "assertion": jwt(sa)}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(sa["token_uri"], data=data), timeout=30) as r:
            return json.loads(r.read())["access_token"]
    except urllib.error.HTTPError as e:
        sys.exit(f"OAuth refusé : HTTP {e.code}")  # le corps n'est jamais relayé


def appel(chemin: str, corps: dict | None = None) -> dict:
    req = urllib.request.Request(f"{API}{chemin}", data=json.dumps(corps).encode() if corps else None,
                                 headers={"Authorization": f"Bearer {jeton()}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"Search Console HTTP {e.code} sur {chemin} — propriété {PROPRIETE} partagée avec le compte de service ?")


def requetes(jours: int = 28, dimension: str = "query", limite: int = 50) -> list[dict]:
    fin = date.today() - timedelta(days=3)  # les données des 2-3 derniers jours sont incomplètes
    corps = {"startDate": (fin - timedelta(days=jours)).isoformat(), "endDate": fin.isoformat(),
             "dimensions": [dimension], "rowLimit": limite}
    d = appel(f"/sites/{urllib.parse.quote(PROPRIETE, safe='')}/searchAnalytics/query", corps)
    return [{"cle": r["keys"][0], "clics": r["clicks"], "impressions": r["impressions"],
             "ctr": round(r["ctr"], 4), "position": round(r["position"], 1)} for r in d.get("rows", [])]


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv or argv[0] not in ("sites", "requetes"):
        print(__doc__)
        return 2
    if argv[0] == "sites":
        print(json.dumps(appel("/sites"), ensure_ascii=False, indent=1))
        return 0
    opt = {a.lstrip("-"): b for a, b in zip(argv[1::2], argv[2::2])}
    rows = requetes(int(opt.get("jours", 28)), opt.get("dimension", "query"), int(opt.get("limite", 50)))
    for r in rows:
        print(f"{r['clics']:>6} clics {r['impressions']:>8} impr. CTR {r['ctr']:.1%} pos. {r['position']:>5}  {r['cle']}")
    print(f"{len(rows)} lignes — propriété {PROPRIETE}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
