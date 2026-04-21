#!/usr/bin/env bash
# audit_geo_v2.sh — Audit GEO refondu (v2)
# Changements v1→v2 :
#   1. Découverte d'URLs via sitemaps (plus d'URL en dur)
#   2. Parsing JSON-LD en Python (plus de grep fragile)
#   3. Extraction liens depuis la page (plus d'endpoint supposé)
#   4. Séparation Partie A (on-site) / Partie B (externe)
#   5. Échelle 3 états + impact estimé pour opportunités

set -u
BASE="https://stephane-lalut.com"
REPORT="audit_geo_v2_$(date +%Y%m%d_%H%M).md"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

# Timeout réseau standardisé
CURL="curl -sS -L --max-time 10"

# Helpers
fetch() { $CURL "${BASE}$1" 2>/dev/null || echo ""; }
http_code() { $CURL -o /dev/null -w "%{http_code}" "$1" 2>/dev/null || echo "000"; }

# ═══════════════════════════════════════════════════════════════
# PHASE 1 — DÉCOUVERTE D'URLS VIA SITEMAPS
# ═══════════════════════════════════════════════════════════════
echo "Découverte des URLs via sitemaps…" >&2

SITEMAP_ROOT=$(fetch "/sitemap.xml")
SITEMAP_FR=$(fetch "/fr/sitemap.xml")
SITEMAP_EN=$(fetch "/en/sitemap.xml")

# Extraire toutes les URLs
ALL_URLS=$(
  echo "$SITEMAP_ROOT$SITEMAP_FR$SITEMAP_EN" \
  | grep -oE '<loc>[^<]+</loc>' \
  | sed -E 's|</?loc>||g' \
  | sort -u
)

# Classification heuristique (pas en dur)
URL_AWP_FR=$(echo "$ALL_URLS" | grep -E "^${BASE}/awp/awp-[0-9]+/?$" | head -1)
URL_AWP_EN=$(echo "$ALL_URLS" | grep -E "^${BASE}/en/awp/awp-[0-9]+/?$" | head -1)
URL_SERIE=$(echo "$ALL_URLS" | grep -iE "(serie-awp|working-papers|anthropie-working)" | grep -v "/en/" | head -1)
URL_SERIE_EN=$(echo "$ALL_URLS" | grep -iE "(serie-awp|working-papers|anthropie-working)" | grep "/en/" | head -1)
URL_ABOUT=$(echo "$ALL_URLS" | grep -iE "(a-propos|about)" | grep -v "/en/" | head -1)
URL_GLOSSAIRE=$(echo "$ALL_URLS" | grep -iE "(glossaire|glossary)" | grep -v "/en/" | head -1)
URL_DEFINITION=$(echo "$ALL_URLS" | grep -iE "(quest-ce|what-is|definition)" | head -1)
URL_HOME_FR="${BASE}/"
URL_HOME_EN="${BASE}/en/"

# Livres (slugs variables — on prend tout ce qui ressemble)
URLS_LIVRES=$(echo "$ALL_URLS" | grep -E "^${BASE}/livres?/[a-z-]+/?$" | grep -v "/en/")

# Export vers le script Python
export AUDIT_BASE="$BASE"
export AUDIT_URLS="$ALL_URLS"
export AUDIT_URL_AWP_FR="$URL_AWP_FR"
export AUDIT_URL_AWP_EN="$URL_AWP_EN"
export AUDIT_URL_SERIE="$URL_SERIE"
export AUDIT_URL_SERIE_EN="$URL_SERIE_EN"
export AUDIT_URL_ABOUT="$URL_ABOUT"
export AUDIT_URL_GLOSSAIRE="$URL_GLOSSAIRE"
export AUDIT_URL_DEFINITION="$URL_DEFINITION"
export AUDIT_URL_HOME_FR="$URL_HOME_FR"
export AUDIT_URL_HOME_EN="$URL_HOME_EN"
export AUDIT_URLS_LIVRES="$URLS_LIVRES"
export AUDIT_TMPDIR="$TMPDIR"
export AUDIT_REPORT="$REPORT"

echo "URLs découvertes :" >&2
echo "  Total : $(echo "$ALL_URLS" | wc -l)" >&2
echo "  AWP FR échantillon : $URL_AWP_FR" >&2
echo "  AWP EN échantillon : $URL_AWP_EN" >&2
echo "  Série FR : $URL_SERIE" >&2
echo "  À propos : $URL_ABOUT" >&2
echo "  Définition : $URL_DEFINITION" >&2
echo "  Livres détectés : $(echo "$URLS_LIVRES" | grep -c .) " >&2

# ═══════════════════════════════════════════════════════════════
# PHASE 2 — DÉLÉGATION À PYTHON POUR PARSING PROPRE
# ═══════════════════════════════════════════════════════════════
echo "Analyse (Python)…" >&2
python audit_geo_v2.py

echo "" >&2
echo "✓ Rapport : $REPORT" >&2
echo "" >&2
cat "$REPORT"
