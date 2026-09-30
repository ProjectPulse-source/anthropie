# -*- coding: utf-8 -*-
"""smoke-production.py -- contrôle de fumée du site SERVI, après déploiement.

    python scripts/smoke-production.py [--base https://stephane-lalut.com] [--attendre 240]

Vérifie sur la production ce que scripts/audit-liens-build.py vérifie dans le build, pour les pages multilingues
du dossier dette et les deux index des ressources : réponse HTTP 200 finale (après redirections), langue de la page,
canonical auto-référent et absolu, alternates FR/EN absolus, auto-référents et réciproques, onglets du dossier et
index des ressources qui pointent vers des pages de la MÊME langue, chacune servie en 200.
--attendre N : relance les vérifications toutes les 20 s pendant N secondes tant qu'elles échouent (le temps que le
CDN de GitHub Pages serve le nouveau déploiement). Sortie 1 si un défaut persiste.

POURQUOI (arbitrage ENTRANTE_2026-09-30_Architecture_Dette-02, F) : le 30/09/2026, le build validé et la production
divergeaient -- versions anglaises justes en local, absentes en ligne. « Validé » ne se dit plus avant d'avoir vu la
même topologie en production. Contrôle PERMANENT, réexaminé à la revue annuelle (R2) ; la liste PAGES s'étend à tout
nouveau couple de pages traduites.
"""
import re
import sys
import time
import urllib.request

a = sys.argv[1:]
BASE = a[a.index("--base") + 1].rstrip("/") if "--base" in a else "https://stephane-lalut.com"
ATTENDRE = int(a[a.index("--attendre") + 1]) if "--attendre" in a else 0
PAGES = [  # (FR, EN)
    ("/pourquoi-la-dette-publique-augmente/", "/en/why-does-public-debt-rise/"),
    ("/cout-de-la-dette-publique/", "/en/cost-of-french-public-debt/"),
    ("/qui-paie-la-dette-publique/", "/en/who-really-pays-public-debt/"),
    ("/dette-publique-comparaison-internationale/", "/en/public-debt-international-comparison/"),
    ("/ressources/", "/en/resources/"),
]
DOSSIER_FR = {fr for fr, _en in PAGES[:4]}
DOSSIER_EN = {en for _fr, en in PAGES[:4]}


def get(path):
    req = urllib.request.Request(BASE + path + ("&" if "?" in path else "?") + "smoke=%d" % time.time(),
                                 headers={"User-Agent": "smoke-production/1.0 (stephane-lalut.com)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.geturl(), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, path, ""
    except Exception as e:  # réseau
        return 0, path, str(e)


def verifier():
    err = []
    cache = {}
    for fr, en in PAGES:
        for p, lang, autre in ((fr, "fr", en), (en, "en", fr)):
            code, final, t = get(p)
            cache[p] = t
            if code != 200:
                err.append("%s : HTTP %s" % (p, code))
                continue
            if not final.split("?")[0].endswith(p):
                err.append("%s : redirigé vers %s" % (p, final))
            if not re.search(r'<html[^>]*\blang="?%s' % lang, t):
                err.append("%s : langue de la page différente de %s" % (p, lang))
            canon = re.search(r'<link rel="?canonical"? href="?([^"\s>]+)', t)
            if not canon or canon.group(1) != BASE + p:
                err.append("%s : canonical %s" % (p, canon.group(1) if canon else "absent"))
            alt = dict((k.lower(), v) for k, v in re.findall(r'<link rel="?alternate"? hreflang="?([a-zA-Z-]+)"? href="?([^"\s>]+)', t))
            if alt.get(lang) != BASE + p:
                err.append("%s : alternate %s non auto-référent (%s)" % (p, lang, alt.get(lang)))
            other = "en" if lang == "fr" else "fr"
            if alt.get(other) != BASE + autre:
                err.append("%s : alternate %s attendu %s, trouvé %s" % (p, other, BASE + autre, alt.get(other)))
            # liens vers les volets du dossier : même langue, et servis
            meme = DOSSIER_EN if lang == "en" else DOSSIER_FR
            contraire = DOSSIER_FR if lang == "en" else DOSSIER_EN
            liens = set(re.findall(r'<a\b[^>]*?href="?(?:%s)?(/[^"\s>#?]*)' % re.escape(BASE), t))
            nav = re.search(r'<nav class="?dossier-dette.*?</nav>', t, re.S)
            liens_nav = set(re.findall(r'href="?(?:%s)?(/[^"\s>#?]*)' % re.escape(BASE), nav.group(0))) if nav else set()
            for l in liens_nav & contraire:
                err.append("%s : onglet vers l'autre langue %s" % (p, l))
            if p in ("/ressources/", "/en/resources/"):
                for l in liens & contraire:
                    err.append("%s : entrée de l'index vers l'autre langue %s" % (p, l))
                manquants = meme - liens
                if manquants:
                    err.append("%s : volets absents de l'index %s" % (p, sorted(manquants)))
            elif nav and len(liens_nav & meme) < 3:
                err.append("%s : barre d'onglets incomplète (%s)" % (p, sorted(liens_nav & meme)))
    return err


debut = time.time()
while True:
    err = verifier()
    if not err or time.time() - debut >= ATTENDRE:
        break
    print("attente du deploiement : %d defaut(s), nouvelle verification dans 20 s" % len(err))
    time.sleep(20)
n = sum(2 for _ in PAGES)
if err:
    print("smoke-production : ECHEC sur %s (%d pages verifiees)" % (BASE, n))
    for e in err:
        print("  " + e.encode("ascii", "replace").decode())
    sys.exit(1)
print("smoke-production : OK -- %d pages servies en 200, canonical, paires de langue et onglets conformes (%s)" % (n, BASE))
