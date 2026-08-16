# =============================================================================
# BATCH 13 — Phase C : Rétro-liens et maillage final
# Version substituée 2026-05-13 (6 QIDs réels intégrés)
# =============================================================================
#
# Objectif : compléter le maillage Wikidata entre la série AWP (Q139040913)
# et les 6 items AWP créés en Phase B. Ce batch ajoute :
#
#   1. Rétro-liens P527 (has part) sur Q139040913 : la série Anthropie Working
#      Papers déclare ses 6 parties constitutives.
#
#   2. Notable work P800 sur Q138909233 (Stéphane Lalut) : les 6 AWPs comme
#      œuvres remarquables de l'auteur.
#
# CINÉTIQUE
# ---------
# À exécuter idéalement à H+72 après Phase B (donc 16 mai matin), mais peut
# être exécuté plus tôt si Phase B est stable (pas de revert / pas de message
# patrouilleur dans les 12-24 premières heures).
#
# NOM DU LOT (à coller dans QuickStatements) :
#   Lalut-Anthropie-PhaseC-2026-05-13
#
# Volume : 12 commandes (6 has-part + 6 notable-work).
# Durée d'exécution : < 30 secondes.
#
# =============================================================================
# 13.1 — Rétro-liens P527 (has part) sur la série AWP
# =============================================================================
# La série Anthropie Working Papers déclare formellement ses 6 parties.
# Cela complète le maillage bidirectionnel : chaque AWP a déjà P361 (part of)
# vers Q139040913 (posé en Phase B), maintenant la série connait ses parties.

Q139040913	P527	Q139771989	S854	"https://stephane-lalut.com/serie-awp/"	S813	+2026-05-13T00:00:00Z/11
Q139040913	P527	Q139771990	S854	"https://stephane-lalut.com/serie-awp/"	S813	+2026-05-13T00:00:00Z/11
Q139040913	P527	Q139771991	S854	"https://stephane-lalut.com/serie-awp/"	S813	+2026-05-13T00:00:00Z/11
Q139040913	P527	Q139771992	S854	"https://stephane-lalut.com/serie-awp/"	S813	+2026-05-13T00:00:00Z/11
Q139040913	P527	Q139771993	S854	"https://stephane-lalut.com/serie-awp/"	S813	+2026-05-13T00:00:00Z/11
Q139040913	P527	Q139771994	S854	"https://stephane-lalut.com/serie-awp/"	S813	+2026-05-13T00:00:00Z/11


# =============================================================================
# 13.2 — Notable work P800 sur Stéphane Lalut
# =============================================================================
# Les 6 AWPs sont déclarés comme œuvres remarquables de l'auteur.
# Cela renforce le maillage personne ↔ publications côté Q138909233.

Q138909233	P800	Q139771989	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-13T00:00:00Z/11
Q138909233	P800	Q139771990	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-13T00:00:00Z/11
Q138909233	P800	Q139771991	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-13T00:00:00Z/11
Q138909233	P800	Q139771992	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-13T00:00:00Z/11
Q138909233	P800	Q139771993	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-13T00:00:00Z/11
Q138909233	P800	Q139771994	S854	"https://orcid.org/0009-0002-1794-4895"	S813	+2026-05-13T00:00:00Z/11


# =============================================================================
# FIN BATCH 13
# =============================================================================
# Après exécution, vérifier :
#   - Q139040913 contient 6 déclarations P527 (parts) vers les 6 AWPs
#   - Q138909233 contient 6 déclarations P800 (notable works) vers les 6 AWPs
#   - Chaque AWP voit son réseau bidirectionnel complet
#
# Statut final attendu : 100% (12) de 12 fait, 0 erreur.
