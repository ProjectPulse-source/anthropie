# =============================================================================
# BATCH 12-FIX — Correction des DOIs surnuméraires (Option B)
# Version 2026-05-13
# =============================================================================
#
# CONTEXTE
# --------
# Le batch 12_ a posé 3 DOIs par AWP (Zenodo FR + Zenodo EN + SSRN) sur la
# propriété P356. Wikidata applique une contrainte d'unicité par élément :
# P356 ne doit pas avoir plusieurs valeurs sans qualifier distinctif valide.
# Le qualifier P407 (langue) n'est PAS accepté sur P356.
#
# Conséquence : chaque item AWP affiche 2 ou 3 alertes ⓘ (soft constraints).
# Non bloquant mais risque de nettoyage automatique par bot qualité.
#
# CORRECTION (Option B)
# ---------------------
# Supprime les 2 P356 surnuméraires sur chaque AWP (DOI Zenodo EN + DOI SSRN).
# Garde uniquement le DOI Zenodo FR principal (qui suffit à l'indexation
# Crossref/OpenAlex/Google Scholar).
#
# Le maillage SSRN reste actif via P5587 (SSRN author ID) sur Q138909233.
# Le maillage Zenodo EN reste accessible via Zenodo Communities.
#
# SYNTAXE QUICKSTATEMENTS V2 POUR SUPPRESSION
# -------------------------------------------
# Préfixe `-` devant le QID pour supprimer un statement existant.
# La valeur doit correspondre EXACTEMENT à celle posée en Phase B.
#
# NOM DU LOT (à coller dans QuickStatements) :
#   Lalut-Anthropie-PhaseB-FixDOI-2026-05-13
#
# Volume : 12 commandes de suppression.
# Durée d'exécution : < 30 secondes.
#
# =============================================================================
# AWP-01 (Q139771989) — Suppression DOI EN + DOI SSRN
# =============================================================================

-Q139771989	P356	"10.5281/zenodo.19431208"
-Q139771989	P356	"10.2139/ssrn.6543618"


# =============================================================================
# AWP-02 (Q139771990) — Suppression DOI EN + DOI SSRN
# =============================================================================

-Q139771990	P356	"10.5281/zenodo.19433086"
-Q139771990	P356	"10.2139/ssrn.6615059"


# =============================================================================
# AWP-03 (Q139771991) — Suppression DOI EN + DOI SSRN
# =============================================================================

-Q139771991	P356	"10.5281/zenodo.19434094"
-Q139771991	P356	"10.2139/ssrn.6615278"


# =============================================================================
# AWP-04 (Q139771992) — Suppression DOI EN + DOI SSRN
# =============================================================================

-Q139771992	P356	"10.5281/zenodo.19439921"
-Q139771992	P356	"10.2139/ssrn.6615305"


# =============================================================================
# AWP-05 (Q139771993) — Suppression DOI EN + DOI SSRN
# =============================================================================

-Q139771993	P356	"10.5281/zenodo.19440866"
-Q139771993	P356	"10.2139/ssrn.6615438"


# =============================================================================
# AWP-06 (Q139771994) — Suppression DOI EN + DOI SSRN
# =============================================================================

-Q139771994	P356	"10.5281/zenodo.20077993"
-Q139771994	P356	"10.2139/ssrn.6735581"


# =============================================================================
# FIN BATCH 12-FIX
# =============================================================================
# Après exécution, vérifier :
#   - Chaque item AWP a exactement 1 P356 (le DOI Zenodo FR principal)
#   - Les alertes ⓘ ont disparu
#   - Les P953 (URLs site FR + EN + Zenodo records) restent en place
#
# Statut final attendu : 100% (12) de 12 fait, 0 erreur.
#
# NOTE : Si Stéphane préfère Option C (déplacer vers P953 au lieu de supprimer),
# ne pas exécuter ce batch. Demander la version 12-fix-OptionC à la place.
