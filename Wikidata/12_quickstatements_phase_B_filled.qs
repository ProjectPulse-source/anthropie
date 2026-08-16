# =============================================================================
# Phase B — CREATE 6 items Wikidata pour AWP-01 à AWP-06
# Source : wikidata_maillage_lalut_v1.md §B.1-B.6 (verbatim) + croisement repo
# Format : QuickStatements V2 (TAB-separated)
# =============================================================================
#
# Cinétique : à exécuter ≥ 48 h APRÈS Phase A. Volume : 6 items × ~15 = ~90 déclarations.
# Le maillage v1 §13 recommande Laura de fractionner en **3 sous-batches de 2 items**
# espacés de 3 jours (J+3, J+7, J+10) pour ne pas déclencher pattern de mass-editing.
# Durée Laura : 45 min × 3 sessions = ~135 min cumulées.
#
# PRÉALABLE OBLIGATOIRE (§B.0 du maillage) — Recherche doublons via toolforge :
#   https://hub.toolforge.org/P356:10.5281/zenodo.19266862   # AWP-01
#   https://hub.toolforge.org/P356:10.5281/zenodo.19268037   # AWP-02
#   https://hub.toolforge.org/P356:10.5281/zenodo.19268769   # AWP-03
#   https://hub.toolforge.org/P356:10.5281/zenodo.19269244   # AWP-04
#   https://hub.toolforge.org/P356:10.5281/zenodo.19269486   # AWP-05
#   https://hub.toolforge.org/P356:10.5281/zenodo.20025421   # AWP-06
# Si un QID est retourné → NE PAS CREATE, mais enrichir l'item existant
#   (substituer le bloc CREATE par le QID retourné).
# Si "no match" sur tous → exécuter le batch ci-dessous tel quel.

# =============================================================================
# B.1 — AWP-01
# =============================================================================
CREATE
LAST	Lfr	"Qu'est-ce que l'anthropie ? Principes d'une hypothèse"
LAST	Len	"What is anthropy? Principles of a hypothesis"
LAST	Dfr	"Working paper de Stéphane Lalut sur les fondements théoriques de l'anthropie (AWP-01, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on the theoretical foundations of anthropy (AWP-01, 2026)"
LAST	P31	Q13442814	# scholarly article
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19266862"	S854	"https://doi.org/10.5281/zenodo.19266862"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19431208"	P407	Q1860	# DOI version EN (qualifié langue anglaise)
LAST	P356	"10.2139/ssrn.6543618"	# DOI SSRN
LAST	P407	Q150	# language: French (principal)
LAST	P577	+2026-02-01T00:00:00Z/11	# publication date FR
LAST	P921	Q138827949	# main subject: anthropy
LAST	P361	Q139040913	# part of: Anthropie Working Papers
LAST	P953	"https://zenodo.org/records/19266862"	# full work URL
LAST	P953	"https://stephane-lalut.com/awp/awp-01/"	P407	Q150	# canonical site URL FR
LAST	P953	"https://stephane-lalut.com/en/awp/awp-01/"	P407	Q1860	# canonical site URL EN

# =============================================================================
# B.2 — AWP-02
# =============================================================================
CREATE
LAST	Lfr	"3,3 millions d'années en un principe : l'anthropie en longue durée"
LAST	Len	"3.3 million years in one principle: anthropy in the longue durée"
LAST	Dfr	"Working paper de Stéphane Lalut appliquant l'anthropie à l'histoire longue (AWP-02, 2026)"
LAST	Den	"Working paper by Stéphane Lalut applying anthropy to long-term history (AWP-02, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19268037"	S854	"https://doi.org/10.5281/zenodo.19268037"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19433086"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615059"
LAST	P407	Q150
LAST	P577	+2026-02-15T00:00:00Z/11
LAST	P921	Q138827949	# main subject: anthropy
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19268037"
LAST	P953	"https://stephane-lalut.com/awp/awp-02/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-02/"	P407	Q1860

# =============================================================================
# B.3 — AWP-03
# =============================================================================
CREATE
LAST	Lfr	"Dette publique et anthropie : qui paie vraiment le désordre ?"
LAST	Len	"Public debt and anthropy: who really pays for disorder?"
LAST	Dfr	"Working paper de Stéphane Lalut sur la dette publique comme transfert anthropique (AWP-03, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on public debt as anthropic transfer (AWP-03, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19268769"	S854	"https://doi.org/10.5281/zenodo.19268769"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19434094"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615278"
LAST	P407	Q150
LAST	P577	+2026-03-01T00:00:00Z/11
LAST	P921	Q138827949	# anthropy
LAST	P921	Q3024789	# government debt
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19268769"
LAST	P953	"https://stephane-lalut.com/awp/awp-03/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-03/"	P407	Q1860

# =============================================================================
# B.4 — AWP-04
# =============================================================================
CREATE
LAST	Lfr	"Transition énergétique ou transfert entropique ?"
LAST	Len	"Energy transition or entropic transfer?"
LAST	Dfr	"Working paper de Stéphane Lalut sur la transition énergétique comme déplacement de désordre (AWP-04, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on energy transition as displacement of disorder (AWP-04, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19269244"	S854	"https://doi.org/10.5281/zenodo.19269244"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19439921"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615305"
LAST	P407	Q150
LAST	P577	+2026-03-10T00:00:00Z/11
LAST	P921	Q138827949	# anthropy
LAST	P921	Q795757	# main subject: energy transition
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19269244"
LAST	P953	"https://stephane-lalut.com/awp/awp-04/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-04/"	P407	Q1860

# =============================================================================
# B.5 — AWP-05
# =============================================================================
CREATE
LAST	Lfr	"Penser hors les murs : notes sur la recherche indépendante en économie"
LAST	Len	"Thinking beyond the walls: notes on independent research in economics"
LAST	Dfr	"Working paper de Stéphane Lalut sur la recherche indépendante en économie (AWP-05, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on independent research in economics (AWP-05, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.19269486"	S854	"https://doi.org/10.5281/zenodo.19269486"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.19440866"	P407	Q1860
LAST	P356	"10.2139/ssrn.6615438"
LAST	P407	Q150
LAST	P577	+2026-03-20T00:00:00Z/11
LAST	P921	Q138827949
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/19269486"
LAST	P953	"https://stephane-lalut.com/awp/awp-05/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-05/"	P407	Q1860

# =============================================================================
# B.6 — AWP-06
# =============================================================================
CREATE
LAST	Lfr	"Infrastructures numériques et dette technologique : data centers, IA et déplacement du désordre"
LAST	Len	"Digital infrastructures and technological debt: data centers, AI, and the displacement of disorder"
LAST	Dfr	"Working paper de Stéphane Lalut sur les infrastructures numériques comme nouveau site de transfert anthropique (AWP-06, 2026)"
LAST	Den	"Working paper by Stéphane Lalut on digital infrastructures as new locus of anthropic transfer (AWP-06, 2026)"
LAST	P31	Q13442814
LAST	P50	Q138909233	S854	"https://orcid.org/0009-0002-1794-4895"
LAST	P356	"10.5281/zenodo.20025421"	S854	"https://doi.org/10.5281/zenodo.20025421"	S813	+2026-05-11T00:00:00Z/11
LAST	P356	"10.5281/zenodo.20077993"	P407	Q1860
LAST	P356	"10.2139/ssrn.6735581"
LAST	P407	Q150
LAST	P577	+2026-05-07T00:00:00Z/11
LAST	P921	Q138827949	# anthropy
LAST	P921	Q671224	# main subject: data center
# Alternative plus précise : Q137571914 (AI data center) — décision Laura.
# Recommandation : poser les DEUX (Q671224 classe parente + Q137571914 classe spécifique).
# Pour ajouter Q137571914, dé-commenter la ligne ci-dessous :
# LAST	P921	Q137571914	# main subject: AI data center (spécialisé IA)
LAST	P921	Q11660	# main subject: artificial intelligence
LAST	P361	Q139040913
LAST	P953	"https://zenodo.org/records/20025421"
LAST	P953	"https://stephane-lalut.com/awp/awp-06/"	P407	Q150
LAST	P953	"https://stephane-lalut.com/en/awp/awp-06/"	P407	Q1860

# =============================================================================
# FIN PHASE B
# =============================================================================
# Après exécution, NOTER les 6 QIDs auto-attribués :
#   AWP-01 → Q______
#   AWP-02 → Q______
#   AWP-03 → Q______
#   AWP-04 → Q______
#   AWP-05 → Q______
#   AWP-06 → Q______
# → reporter dans 13_quickstatements_phase_C_filled.qs (placeholders Q-AWP-NN)
#
# Notes de prudence (§ 12 du maillage v1) :
# - AWP-06 statut MPRA "Under Review" — la notabilité peut être questionnée
#   tant que MPRA n'a pas approuvé. Créer maintenant ; défendre via les
#   4 plateformes (Zenodo + SSRN + MPRA + OpenAlex) si patrouilleur.
# - Si annulation : EditGroups (chaque batch est traçable + rollback en 1 clic).
