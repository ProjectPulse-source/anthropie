# =============================================================================
# BATCH 16 — Maillage OpenLibrary ↔ Wikidata
# Version 2026-05-13 — 4 commandes (1 personne + 3 livres)
# =============================================================================
#
# CONTEXTE
# --------
# Stéphane Lalut a créé 4 fiches livre sur OpenLibrary le 2026-05-13 :
#   - Livresque des mots          → OL45424544W
#   - L'Odyssée des idées         → OL45424562W
#   - ANTHROPIE                   → OL45424565W
#   - Dette Publique              → OL45424600W
#
# Ainsi que sa page auteur :
#   - Author Stéphane Lalut       → OL16378291A
#
# Ce batch ajoute la propriété P648 (Open Library ID) sur les items Wikidata
# correspondants pour créer le pont OpenLibrary ↔ Wikidata.
#
# LIVRESQUE DES MOTS n'a pas d'item Wikidata → aucune ligne pour ce livre.
# Le maillage côté OpenLibrary existe néanmoins (lien site officiel).
#
# CINÉTIQUE
# ---------
# À exécuter immédiatement (pas de dépendance externe). Volume : 4 commandes,
# durée < 15 secondes.
#
# NOM DU LOT (à coller dans QuickStatements) :
#   Lalut-Anthropie-OpenLibrary-2026-05-13
#
# =============================================================================
# 16.1 — Q138909233 (Stéphane Lalut, personne) → Author ID
# =============================================================================
# Format Author ID : OL<n>A (suffixe A pour Author).

Q138909233	P648	"OL16378291A"	S854	"https://openlibrary.org/authors/OL16378291A"	S813	+2026-05-13T00:00:00Z/11


# =============================================================================
# 16.2 — Q138827344 (ANTHROPIE — Ordre ici. Dette ailleurs.) → Work ID
# =============================================================================
# Format Work ID : OL<n>W (suffixe W pour Work).
# Convention Wikidata : on lie l'item Book (conceptuel) au Work OpenLibrary
# (conceptuel aussi). L'Edition ID (OL...M) reste optionnel et pourrait être
# ajouté plus tard via une propriété distincte si besoin.

Q138827344	P648	"OL45424565W"	S854	"https://openlibrary.org/works/OL45424565W"	S813	+2026-05-13T00:00:00Z/11


# =============================================================================
# 16.3 — Q138910896 (Dette Publique : Qui paie vraiment ?) → Work ID
# =============================================================================

Q138910896	P648	"OL45424600W"	S854	"https://openlibrary.org/works/OL45424600W"	S813	+2026-05-13T00:00:00Z/11


# =============================================================================
# 16.4 — Q138911733 (L'Odyssée des idées) → Work ID
# =============================================================================

Q138911733	P648	"OL45424562W"	S854	"https://openlibrary.org/works/OL45424562W"	S813	+2026-05-13T00:00:00Z/11


# =============================================================================
# FIN BATCH 16
# =============================================================================
# Statut final attendu : 100% (4) de 4 fait, 0 erreur.
#
# Après exécution, vérifier :
#   - Q138909233 affiche bien P648 = OL16378291A (cliquable, mène à la page auteur)
#   - Les 3 items livres affichent leur Work ID respectif
#   - Aucune alerte ⓘ (pas de contrainte d'unicité ni de qualifier interdit)
#
# Note : Livresque des mots n'a pas d'item Wikidata, donc pas de ligne dans
# ce batch. Le maillage OpenLibrary ↔ Wikidata reste cohérent : on lie ce qui
# existe des deux côtés, on ne crée pas d'item Wikidata juste pour le pont.
