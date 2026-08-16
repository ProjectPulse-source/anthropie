# =============================================================================
# BATCH 15 — Intégration SocArXiv au maillage Wikidata
# Version v3 (2026-05-13) — COMPATIBLE Option B
# =============================================================================
#
# CHANGEMENT MAJEUR vs version précédente :
# Les DOIs SocArXiv sont désormais posés en P953 (URL de l'œuvre complète)
# plutôt qu'en P356 (DOI). Ceci respecte la décision d'Option B prise après
# l'analyse de la contrainte d'unicité de P356.
#
# Justification : P953 accepte plusieurs valeurs sans contrainte. Le maillage
# SocArXiv reste actif (la plateforme indexe les DOIs côté Crossref/OpenAlex).
#
# RÉSOLU dans cette version :
#   ✅ OSF_USER_ID = ymkpj
#   ✅ Q-AWP-01 = Q139771989
#   ✅ Q-AWP-02 = Q139771990
#   ✅ Q-AWP-03 = Q139771991
#   ✅ Q-AWP-04 = Q139771992
#   ✅ Q-AWP-05 = Q139771993
#   ✅ Q-AWP-06 = Q139771994
#   ✅ OSF_DOI_AWP_06 = 10.31235/osf.io/z6x38_v1
#
# RESTE À SUBSTITUER (au fur et à mesure des 5 dépôts SocArXiv) :
#   ⏳ <OSF_DOI_AWP_01>, <OSF_DOI_AWP_02>, <OSF_DOI_AWP_03>,
#      <OSF_DOI_AWP_04>, <OSF_DOI_AWP_05>
#
# NOMS DE LOTS RECOMMANDÉS :
#   - Exécution immédiate (15.1 + 15.7) : Lalut-Anthropie-SocArXiv-2026-05-13
#   - Exécutions ultérieures (15.2 à 15.6) : Lalut-Anthropie-SocArXiv-AWPXX-YYYY-MM-DD
#
# =============================================================================


# -----------------------------------------------------------------------------
# 15.1 — Profil OSF/SocArXiv sur l'item personne Q138909233
# -----------------------------------------------------------------------------
# Cette ligne reste inchangée : sur la personne, P973 (described at URL) est
# la propriété correcte pour pointer vers le profil OSF.

Q138909233	P973	"https://osf.io/ymkpj/"	P407	Q1860	S854	"https://osf.io/ymkpj/"	S813	+2026-05-13T00:00:00Z/11


# -----------------------------------------------------------------------------
# 15.2 — URL SocArXiv sur AWP-01 (à activer après dépôt SocArXiv)
# -----------------------------------------------------------------------------

# Q139771989	P953	"https://doi.org/<OSF_DOI_AWP_01>"	S854	"https://doi.org/<OSF_DOI_AWP_01>"	S813	+2026-05-13T00:00:00Z/11


# -----------------------------------------------------------------------------
# 15.3 — URL SocArXiv sur AWP-02 (à activer après dépôt SocArXiv)
# -----------------------------------------------------------------------------

# Q139771990	P953	"https://doi.org/<OSF_DOI_AWP_02>"	S854	"https://doi.org/<OSF_DOI_AWP_02>"	S813	+2026-05-13T00:00:00Z/11


# -----------------------------------------------------------------------------
# 15.4 — URL SocArXiv sur AWP-03 (à activer après dépôt SocArXiv)
# -----------------------------------------------------------------------------

# Q139771991	P953	"https://doi.org/<OSF_DOI_AWP_03>"	S854	"https://doi.org/<OSF_DOI_AWP_03>"	S813	+2026-05-13T00:00:00Z/11


# -----------------------------------------------------------------------------
# 15.5 — URL SocArXiv sur AWP-04 (à activer après dépôt SocArXiv)
# -----------------------------------------------------------------------------

# Q139771992	P953	"https://doi.org/<OSF_DOI_AWP_04>"	S854	"https://doi.org/<OSF_DOI_AWP_04>"	S813	+2026-05-13T00:00:00Z/11


# -----------------------------------------------------------------------------
# 15.6 — URL SocArXiv sur AWP-05 (à activer après dépôt SocArXiv)
# -----------------------------------------------------------------------------

# Q139771993	P953	"https://doi.org/<OSF_DOI_AWP_05>"	S854	"https://doi.org/<OSF_DOI_AWP_05>"	S813	+2026-05-13T00:00:00Z/11


# -----------------------------------------------------------------------------
# 15.7 — URL SocArXiv sur AWP-06 (EXÉCUTABLE IMMÉDIATEMENT)
# -----------------------------------------------------------------------------
# AWP-06 (Digital Infrastructures) déposé sur SocArXiv le 2026-05-11.
# DOI minté : 10.31235/osf.io/z6x38_v1

Q139771994	P953	"https://doi.org/10.31235/osf.io/z6x38_v1"	S854	"https://doi.org/10.31235/osf.io/z6x38_v1"	S813	+2026-05-13T00:00:00Z/11


# =============================================================================
# FIN BATCH 15 v3
# =============================================================================
# EXÉCUTABLE MAINTENANT : 2 commandes (15.1 + 15.7)
# - 15.1 : profil OSF sur Q138909233
# - 15.7 : URL SocArXiv sur AWP-06
#
# Pas de risque de réintroduire la contrainte d'unicité (P953 n'a pas cette
# contrainte). Pas de réintroduction d'alertes ⓘ sur les items AWP.
#
# PROCÉDURE DE SUBSTITUTION FUTURE (par Stéphane) :
#   1. Après chaque dépôt SocArXiv accepté, récupérer le DOI minté
#      (format 10.31235/osf.io/xxxxx_v1)
#   2. Find/replace dans ce fichier :
#      - <OSF_DOI_AWP_XX> → la valeur réelle (deux occurrences par ligne)
#   3. Retirer le # de début de ligne pour la rendre exécutable
#   4. Sauvegarder
#   5. Exécuter via QuickStatements (peut être batch unique ou par vagues)
