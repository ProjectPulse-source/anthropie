#!/usr/bin/env python3
"""
Surveillance de l'etat des depots du corpus AWP sur les plateformes externes.

DOCTRINE DU DEPOT ECHELONNE (auteur, 2026-08-02) :
  Jamais plus de 1 a 2 depots a la fois sur une meme plateforme. On depose,
  on SURVEILLE, et on ne pose le suivant qu'une fois le precedent ACCEPTE.
  Motif : 5 depots MPRA en 18 minutes le 07/04 sont restes bloques 118 jours,
  alors qu'un depot isole le 08/05 a ete accepte en 7 jours.

Ce script repond a une seule question : "ou en est chaque depot, maintenant ?"
Il ne depose rien et ne modifie rien.

Methodes de detection (aucun mot de passe requis) :
  - SSRN   : API CROSSREF sur 10.2139/ssrn.<id>. NE PAS utiliser doi.org :
             SSRN renvoie 403 anti-bot sur la redirection finale, ce qui
             produit un faux negatif (constate le 2026-08-02 : les 6 papiers
             etaient en ligne et le detecteur les disait tous absents).
             Crossref renvoie en prime le TITRE tel qu'il est publie, ce qui
             permet de reperer les titres degrades a la soumission.
  - MPRA   : HTTP sur /id/eprint/<id> (200 => publie, 401/403 => en review)
  - OSF    : API publique des preprints
  - Zenodo : API (token) — deja couvert par zenodo_audit_complet.py

Usage : python scripts/check_deposits_status.py
"""
import os, sys, json, urllib.request, urllib.error, ssl

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# --- Etat declare (tenir a jour ; source : data/works.yaml) ---------------
SSRN = [("AWP-01", "6543618"), ("AWP-02", "6615059"), ("AWP-03", "6615278"),
        ("AWP-04", "6615305"), ("AWP-05", "6615438"), ("AWP-06", "6735581")]
SSRN_MANQUANTS = ["AWP-07", "AWP-08"]

MPRA = [("AWP-01", "128604"), ("AWP-02", "128605"), ("AWP-03", "128606"),
        ("AWP-04", "128607"), ("AWP-05", "128608"), ("AWP-06", "129034")]
MPRA_MANQUANTS = ["AWP-07", "AWP-08"]

OSF_PROFIL = "ymkpj"
OSF_ATTENDUS = 8  # objectif si SocArXiv est retenu comme canal actif


def http_status(url):
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None


def crossref(doi):
    """Retourne (existe, titre) via l'API Crossref. Jamais doi.org (403 SSRN)."""
    try:
        req = urllib.request.Request(f"https://api.crossref.org/works/{doi}",
                                     headers=UA)
        with urllib.request.urlopen(req, timeout=25, context=CTX) as r:
            msg = json.loads(r.read())["message"]
        titles = msg.get("title") or [""]
        return True, titles[0]
    except Exception:
        return False, ""


print("=" * 70)
print("ETAT DES DEPOTS — surveillance (doctrine du depot echelonne)")
print("=" * 70)

# --- SSRN --------------------------------------------------------------
print("\n[SSRN]  via Crossref (jamais doi.org : 403 anti-bot = faux negatif)")
ssrn_ok = 0
for label, sid in SSRN:
    ok, title = crossref(f"10.2139/ssrn.{sid}")
    ssrn_ok += ok
    state = "EN LIGNE" if ok else "ABSENT"
    print(f"   {label}  {sid}  {state}  {title[:44]}")
for label in SSRN_MANQUANTS:
    print(f"   {label}  --       A DEPOSER")
print(f"   -> {ssrn_ok}/{len(SSRN)} en ligne ; {len(SSRN_MANQUANTS)} a deposer")

# --- MPRA --------------------------------------------------------------
print("\n[MPRA]  200 = publie ; 401/403 = encore en moderation")
mpra_live = 0
for label, mid in MPRA:
    code = http_status(f"https://mpra.ub.uni-muenchen.de/id/eprint/{mid}")
    if code == 200:
        mpra_live += 1
        state = "PUBLIE"
    elif code in (401, 403):
        state = "EN MODERATION"
    else:
        state = f"HTTP {code}"
    print(f"   {label}  {mid}  {state}")
for label in MPRA_MANQUANTS:
    print(f"   {label}  --       A DEPOSER (apres deblocage du lot d'avril)")
print(f"   -> {mpra_live}/{len(MPRA)} publies")

# --- OSF ---------------------------------------------------------------
print("\n[OSF / SocArXiv]")
try:
    req = urllib.request.Request(
        f"https://api.osf.io/v2/users/{OSF_PROFIL}/preprints/?page[size]=30",
        headers=UA)
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        d = json.loads(r.read())
    n = len(d.get("data", []))
    for p in d.get("data", []):
        a = p["attributes"]
        print(f"   {p['id']:12} {a.get('title','')[:46]}")
    print(f"   -> {n} preprint(s) en ligne (objectif si canal retenu : {OSF_ATTENDUS})")
except Exception as e:
    print(f"   ERREUR : {e}")

# --- Rappel de doctrine -------------------------------------------------
print("\n" + "=" * 70)
print("REGLE : ne poser le depot suivant qu'apres ACCEPTATION du precedent.")
print("Jamais plus de 1-2 depots simultanes sur une meme plateforme.")
