"""Traduction anglaise de la Constitution publiée par le Conseil constitutionnel, pour les pages anglaises du dossier
Promesses. Source : https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958, page archivée le 06/10/2026
(constitution_en_conseil_constitutionnel.html, empreinte SHA256 ci-dessous ; à jour de la révision du 8 mars 2024 : l'art.
34 y porte la liberté garantie à la femme d'avoir recours à une interruption volontaire de grossesse).

Règle des pages anglaises (06/10/2026) : la Constitution se cite dans CETTE traduction, mot pour mot ; les autres textes
français se citent en français, suivis de « our translation ». Les générateurs vérifient chaque citation anglaise par
`citer()`, qui arrête si le texte manque, et l'empreinte du fichier par `texte()`.
"""
from __future__ import annotations

import hashlib
import html
import re
from pathlib import Path

ICI = Path(__file__).resolve().parent
FICHIER = ICI / "constitution_en_conseil_constitutionnel.html"
SHA256 = "d6a446ae36afe1f820c379e849a857bf56edf1f6b5f442ff0004e9f1dc25c936"
URL = "https://www.conseil-constitutionnel.fr/en/constitution-of-4-october-1958"
ATTRIBUTION = "English translation published by the Conseil constitutionnel"


def norm(s: str) -> str:
    s = s.replace(" ", " ").replace(" ", " ").replace("’", "'").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()


def texte() -> str:
    # Fins de ligne normalisées avant l'empreinte : git (core.autocrlf) peut réécrire le fichier en CRLF au checkout ;
    # l'empreinte d'origine (LF) reste celle du document téléchargé.
    b = FICHIER.read_bytes().replace(b"\r\n", b"\n")
    if hashlib.sha256(b).hexdigest() != SHA256:
        raise ValueError("constitution_en : empreinte du fichier archivé changée")
    return norm(html.unescape(re.sub(r"<[^>]+>", " ", b.decode("utf-8"))))


def article(n: str, t: str | None = None) -> str:
    """Texte de l'article n (« 24 », « 49 »…), du titre « Article n » au titre d'article suivant."""
    t = t or texte()
    # La page porte d'abord une table des matières (« Article 24 Article 25 … ») : on garde l'occurrence la plus longue,
    # celle du corps de l'article.
    ms = re.findall(r"Article %s (.*?)(?= Article \d+(?:-\d+)? | Title [IVXL]+ - )" % re.escape(n), t)
    ms = [m for m in ms if len(m) > 40]
    if len(ms) != 1:
        raise ValueError("constitution_en : article %s : %d occurrences de corps" % (n, len(ms)))
    return ms[0]


def citer(n: str, citation: str, t: str | None = None) -> str:
    """Renvoie la citation si elle figure mot pour mot dans l'article n de la traduction ; sinon arrête."""
    c = norm(citation)
    if c not in article(n, t):
        raise ValueError("constitution_en : citation absente de l'article %s : %r" % (n, c[:60]))
    return c
