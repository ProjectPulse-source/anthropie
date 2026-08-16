# =============================================================================
# Phase A — Corrections et enrichissements d'items Wikidata existants
# Source : wikidata_maillage_lalut_v1.md §A.1-A.6 (verbatim) + croisement repo
# Format : QuickStatements V2 (TAB-separated)
# =============================================================================
#
# Cinétique : à exécuter en PREMIER. Pas de création nouvelle. Risque très faible.
# Volume : ~70 déclarations. Durée Laura : ~30 min validation + exécution.
# Attendre ≥ 48 h après Phase A avant d'exécuter Phase B.
#
# CONVENTION QS V2 :
#   - Lignes commentaires : début par `#`
#   - Déclaration : `Qxxx  TAB  Pyyy  TAB  valeur  [TAB  Saaa  TAB  source]`
#   - Source URL = S854 ; date = S813 ; références = stabilisent face aux patrouilleurs
#   - `Lfr`/`Len`/`Dfr`/`Den` = labels et descriptions (multilingual)
#
# CROISEMENT REPO (substitutions appliquées depuis wikidata_maillage_lalut_v1.md) :
#   - URL EN concept = "/en/what-is-anthropy/" (slug confirmé content/quest-ce-que-lanthropie/_index.en.md ligne 3)
#   - URL EN série AWP = "/en/serie-awp/" (CORRIGÉ : le maillage v1 proposait "/en/awp-series/"
#     mais aucun slug ni alias EN "awp-series" n'existe dans le repo. Le menu EN hugo.toml
#     pointe explicitement vers /en/serie-awp/ et content/serie-awp/_index.en.md déclare
#     aliases: ["/en/awp/"]. URL effective Hugo = /en/serie-awp/.)
#   - ASIN livre ANTHROPIE = B0FQ9PG246 (data/works.yaml ligne 275)
#   - ISBN livre Dette Publique = 978-2-9586347-3-5 (data/works.yaml ligne 300)
#   - Pages livre ANTHROPIE = 622 (data/works.yaml ligne 272)
#   - DOIs/URLs/dates AWPs = data/works.yaml + content/awp/*.md (concordance verbatim)
#
# Les `[À VÉRIFIER]` portant sur des Q-IDs/P-IDs Wikidata externes restent
# inchangés — Laura valide.

# =============================================================================
# A.1 — Stéphane Lalut (Q138909233)
# =============================================================================

# === Ajouts identité ===
Q138909233	P735	Q3501543	# given name: Stéphane
Q138909233	P734	"Lalut"	# family name (texte si pas d'item Wikidata)
Q138909233	P21	Q6581097	# sex or gender: male [confirmer avant exécution]

# === Champs de travail (P101) ===
Q138909233	P101	Q8134	# field of work: economics
Q138909233	P101	Q274490	# field of work: public finance
Q138909233	P101	Q1049066	# field of work: ecological economics
Q138909233	P101	Q138827949	# field of work: anthropy (auto-référentiel mais légitime — théoricien d'un concept)

# === Notable works additionnels ===
Q138909233	P800	Q138911733	# notable work: L'Odyssée des Idées
Q138909233	P800	Q138827949	# notable work: anthropie (concept)
Q138909233	P800	Q139040913	# notable work: Anthropie Working Papers (série)

# === Pas de P569 (date de naissance) — non publique, NE PAS INVENTER ===


# =============================================================================
# A.2 — Anthropy (Q138827949)
# =============================================================================

# === Reclassification du P31 ===
# P31 actuel = concept (Q151885) → conserver, ajouter qualificatif théorique
Q138827949	P31	Q17737	# add: theory
Q138827949	P31	Q41719	# add: hypothesis

# === Champ disciplinaire ===
Q138827949	P101	Q8134	# field: economics
Q138827949	P101	Q1554076	# field: political ecology
Q138827949	P101	Q34749	# field: social sciences

# === Inspirations (relations conceptuelles) ===
Q138827949	P941	Q45003	# inspired by: entropy (thermodynamique)
# Note : NE PAS écrire que l'anthropie EST l'entropie. Relation = inspiration analogique.

# === Œuvres notables qui traitent du concept ===
Q138827949	P800	Q138827344	# notable work: ANTHROPIE livre
Q138827949	P800	Q138910896	# notable work: Dette Publique livre
Q138827949	P800	Q139040913	# notable work: Anthropie Working Papers série

# === Sources et URLs supplémentaires ===
# URL EN concept : slug "what-is-anthropy" déclaré dans content/quest-ce-que-lanthropie/_index.en.md ligne 3
Q138827949	P973	"https://stephane-lalut.com/en/what-is-anthropy/"	P407	Q1860	# described at URL (EN)

# === Description en plus de langues (si pas déjà fait) ===
Q138827949	Dit	"Meccanismo per cui i sistemi sociali spostano il disordine invece di risolverlo"
Q138827949	Den	"Mechanism by which social systems displace disorder rather than resolving it"
# Note : labels FR/EN/ES déjà présents selon fiche actuelle.


# =============================================================================
# A.3 — ANTHROPIE — Ordre ici. Dette ailleurs (Q138827344)
# =============================================================================

# === Compléments métadonnées ===
Q138827344	P1104	+622	# number of pages: 622 (data/works.yaml ligne 272) — VALEUR CORRIGÉE 2026-05-29 (606→622). NB : l'entité Wikidata vivante porte encore 606 ; correction externe requise (retirer +606 / ajouter +622).
Q138827344	P136	Q35760	# genre: essay
Q138827344	P291	Q142	# place of publication: France

# === Reference URL (sourcing renforcé) ===
# ASIN Kindle B0FQ9PG246 (data/works.yaml ligne 275)
Q138827344	P953	"https://www.amazon.fr/dp/B0FQ9PG246"	# [À VÉRIFIER si propriété P953 acceptée pour Amazon]


# =============================================================================
# A.4 — Dette Publique : Qui paie vraiment ? (Q138910896)
# =============================================================================

# === Ajout ISBN (manquant sur la fiche actuelle) ===
Q138910896	P212	"978-2-9586347-3-5"	S854	"https://stephane-lalut.com/livres/dette-publique-qui-paie-vraiment/"	S813	+2026-05-11T00:00:00Z/11

# === Compléments métadonnées ===
Q138910896	P136	Q35760	# genre: essay
Q138910896	P407	Q150	# language: French (manque sur fiche)
Q138910896	P291	Q142	# place of publication: France


# =============================================================================
# A.5 — L'Odyssée des Idées (Q138911733) — CORRECTIONS CRITIQUES
# =============================================================================

# === RÉVISION P31 (v2.1) — pas de suppression nécessaire ===
# Maillage v1 préconisait de supprimer P31=Q3331189 (version, edition or translation).
# CORRECTION v2.1 : cette valeur DOIT être conservée car elle est dans la liste
# de classes autorisées pour P5749 (ASIN). On AJOUTE simplement Q47461344 et Q571
# en complément, sans toucher à Q3331189 existant.
Q138911733	P31	Q47461344	# instance of: written work (ajout en complément, conserve Q3331189)
Q138911733	P31	Q571	# instance of: book (ajout en complément, conserve Q3331189)

# === AJOUT AUTEUR (P50 absent — maillage cassé) ===
# Sourcé sur l'URL Amazon FR (fournie par utilisateur 2026-05-11) plutôt que sur
# stephane-lalut.com (où le livre n'a pas de page) : Amazon affiche l'auteur en
# clair sur la page produit, source primaire vérifiable par patrouilleur Wikidata.
Q138911733	P50	Q138909233	S854	"https://www.amazon.fr/Lodyssée-idées-philosophie-lintelligence-artificielle/dp/295863471X"	S813	+2026-05-11T00:00:00Z/11

# === Compléments ===
Q138911733	P136	Q35760	# genre: essay (existe déjà ? — sinon ajouter)
Q138911733	P291	Q142	# place of publication: France

# === Sourcing P212 ISBN existant (renforcer la déclaration P212 déjà posée) ===
# L'ISBN-13 978-2-9586347-1-1 est déjà sur Q138911733 selon 09_. Renforcer par
# une source URL Amazon FR confirmée par l'utilisateur 2026-05-11.
# NB QS V2 : la syntaxe ci-dessous AJOUTE la même valeur avec une source ;
# si Wikidata dédoublonne, la source vient se rattacher à la déclaration existante.
Q138911733	P212	"978-2-9586347-1-1"	S854	"https://www.amazon.fr/Lodyssée-idées-philosophie-lintelligence-artificielle/dp/295863471X"	S813	+2026-05-11T00:00:00Z/11

# === Page site (à activer SI une page dédiée existe — pas dans le repo au 2026-05-11) ===
# La page content/livres/lodyssee-des-idees.md est ABSENTE du repo
# (cf. 00_inventory_audit.md §3). Activer si Stéphane crée la page.
# Q138911733	P856	"https://stephane-lalut.com/livres/lodyssee-des-idees/"	# [À VÉRIFIER que la page existe]

# === ASIN Amazon papier (P5749) — recommandation Wikidata sur identifiant dédié ===
# Pour les livres papier, ASIN = ISBN-10. L'ISBN-13 978-2-9586347-1-1 correspond à
# l'ISBN-10 295863471X. Source utilisateur 2026-05-11 (URL Amazon FR).
Q138911733	P5749	"295863471X"	S854	"https://www.amazon.fr/Lodyssée-idées-philosophie-lintelligence-artificielle/dp/295863471X"	S813	+2026-05-11T00:00:00Z/11

# === URL marchande Amazon : RÉSOLU en v2.1 ===
# Doctrine Wikidata : si identifiant dédié existe (P5749 ASIN), ne pas dupliquer
# avec une URL générique (P973). La déclaration P5749 ci-dessus suffit ; les
# patrouilleurs reconstruiront l'URL via le format Amazon standard.


# =============================================================================
# A.6 — Anthropie Working Papers série (Q139040913)
# =============================================================================

# === P31 série AWP — RECONDUIT v2.3 (ne pas toucher) ===
# Recommandation #6 du fichier 14_remaining_decisions_for_laura.md confirmée
# par l'utilisateur 2026-05-11 : aucun Q-ID concept standard satisfaisant n'a
# été trouvé pour « working paper series » sur Wikidata (Q1711593 = edited
# volume, Q5633421 = scientific journal — tous deux inadaptés). On NE TOUCHE
# PAS au P31=Q13442814 actuellement présent. Si une meilleure classe émerge
# ultérieurement (recherche Wikidata SPARQL), Laura applique la correction
# en deux temps (ajout puis suppression manuelle) à ce moment-là.

# === Compléments ===
Q139040913	P407	Q150	# language: French (principal)
Q139040913	P407	Q1860	# language: English (versions traduites)
Q139040913	P9934	"anthropie-working-papers"	# Zenodo communities ID (data/author.toml ligne 31)
Q139040913	P101	Q8134	# field of work: economics
Q139040913	P101	Q138827949	# field of work: anthropy
Q139040913	P50	Q138909233	# author already present — skip if exists

# === URL EN série — CORRECTION repo vs maillage v1 ===
# Le maillage v1 propose "/en/awp-series/" mais ce slug n'existe pas dans le repo.
# URL réelle Hugo = "/en/serie-awp/" (config/_default/hugo.toml ligne 27-29 menu EN).
Q139040913	P856	"https://stephane-lalut.com/en/serie-awp/"	# canonical EN URL

# === Diffusion / has parts ===
# Note : le lien parent→enfants se fait depuis chaque AWP via P361 en Phase B,
# et inversement par P527 en Phase C (cf. 13_).


# =============================================================================
# FIN PHASE A
# =============================================================================
# Vérifications post-batch (cf. § 10 du maillage v1) :
#   - H+1  : chaque QID modifié, vérifier absence d'undo dans "View history"
#   - H+24 : vérifier absence de bannière "Proposed for deletion"
#   - H+72 : check global. Si suppression proposée → défendre via sources
#            Zenodo + SSRN + MPRA + OpenAlex (4 plateformes indépendantes).
# Rollback éventuel : https://editgroups.toolforge.org/
