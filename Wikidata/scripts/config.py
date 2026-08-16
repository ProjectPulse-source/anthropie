# -*- coding: utf-8 -*-
"""
Constantes Q-IDs et P-IDs validées pour le dispositif Lalut/Anthropie.

Toutes les valeurs sont vérifiées au 2026-05-13 contre Wikidata.
Aucune invention. Source : maillage_lalut_v1 + batches 11_/12_/13_ exécutés.

Pour ajouter une nouvelle valeur : vérifier sur wikidata.org, noter ici
avec un commentaire indiquant la source de vérification.
"""

# =============================================================================
# Q-IDs ENTITÉS LALUT (validés par création Wikidata réelle)
# =============================================================================

# Personne et œuvres principales
STEPHANE_LALUT = "Q138909233"
ANTHROPY_CONCEPT = "Q138827949"
AWP_SERIES = "Q139040913"

# Livres
BOOK_ANTHROPIE = "Q138827344"           # ANTHROPIE - Ordre ici. Dette ailleurs
BOOK_DETTE_PUBLIQUE = "Q138910896"      # Dette Publique : Qui paie vraiment ?
BOOK_ODYSSEE = "Q138911733"             # L'Odyssée des Idées

# 6 AWPs créés en Phase B (2026-05-12)
AWP_01 = "Q139771989"
AWP_02 = "Q139771990"
AWP_03 = "Q139771991"
AWP_04 = "Q139771992"
AWP_05 = "Q139771993"
AWP_06 = "Q139771994"

# =============================================================================
# Q-IDs CONCEPTS WIKIDATA (validés)
# =============================================================================

HUMAN = "Q5"
FRANCE = "Q142"
FRENCH = "Q150"
ENGLISH = "Q1860"
SCHOLARLY_ARTICLE = "Q13442814"
BOOK = "Q571"
ECONOMIST = "Q188094"
WRITER = "Q36180"
ESSAYIST = "Q11774202"                   # essayiste
STEPHANE_GIVEN_NAME = "Q3501543"         # corrigé en v2.1 du maillage
ZENODO = "Q22661177"                     # corrigé en v2.1 du maillage

# Sujets AWP (validés en v2 du maillage)
GOVERNMENT_DEBT = "Q3024789"
ENERGY_TRANSITION = "Q795757"
DATA_CENTER = "Q671224"
AI_DATA_CENTER = "Q137571914"
ARTIFICIAL_INTELLIGENCE = "Q11660"

# =============================================================================
# P-IDs PROPRIÉTÉS WIKIDATA (validés)
# =============================================================================

# Métadonnées générales
INSTANCE_OF = "P31"
AUTHOR = "P50"
OCCUPATION = "P106"
COUNTRY_OF_CITIZENSHIP = "P27"
LANGUAGE_OF_WORK = "P407"
PUBLICATION_DATE = "P577"
MAIN_SUBJECT = "P921"
PART_OF = "P361"
HAS_PART = "P527"
DOI = "P356"
FULL_WORK_URL = "P953"
DESCRIBED_AT_URL = "P973"
NOTABLE_WORK = "P800"
PUBLISHED_IN = "P1433"

# Identifiants externes
ORCID = "P496"
GOOGLE_SCHOLAR = "P1960"
SSRN_AUTHOR = "P5587"
OPENALEX = "P10283"
IDREF = "P269"
ZENODO_COMMUNITY = "P9934"   # ATTENTION : main value only, pas qualifier
AMAZON_ASIN = "P5749"
ISBN_13 = "P212"
ISBN_10 = "P957"

# Sources (préfixe S dans QuickStatements)
REF_URL = "S854"
REF_RETRIEVED = "S813"

# =============================================================================
# REGEX DE VALIDATION
# =============================================================================

REGEX_DOI = r"^10\.[0-9]{4,9}\/[-._;()/:A-Za-z0-9]+$"
REGEX_ISBN_13 = r"^97[89]-?\d{1,5}-?\d{1,7}-?\d{1,7}-?\d$"
REGEX_ZENODO_COMMUNITY = r"^[a-z0-9][-a-z0-9_]*$"

# =============================================================================
# PROPRIÉTÉS À PORTÉE RESTREINTE (NE PAS UTILISER COMME QUALIFIER)
# =============================================================================

# Ces propriétés ont un scope = "main value only" et NE DOIVENT JAMAIS
# apparaître comme qualifier (préfixe P) ni comme source qualifier (préfixe S)
# dans les batches QuickStatements.
MAIN_VALUE_ONLY = {
    ZENODO_COMMUNITY,  # P9934 - cf. bug Phase A 2026-05-12
}

# Qualifiers INVALIDES pour des propriétés données
# Format : {propriété: [liste des qualifiers à interdire]}
FORBIDDEN_QUALIFIERS = {
    DOI: [LANGUAGE_OF_WORK],  # P407 sur P356 - cf. bug Phase B 2026-05-12
}
