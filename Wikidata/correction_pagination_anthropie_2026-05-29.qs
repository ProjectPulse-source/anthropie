# =============================================================================
# Correction pagination ANTHROPIE — Q138827344, P1104 (number of pages)
# 606 -> 622 (mise a jour de l'edition)
# =============================================================================
#
# Etat verifie le 2026-05-29 via l'API Wikidata (Special:EntityData/Q138827344.json) :
#   - 1 seule claim P1104, valeur +606, unite 1 (sans dimension), rang normal,
#   - AUCUN qualificatif ni reference attache -> remove/add sans perte.
#
# Outil : https://quickstatements.toolforge.org  (compte Wikidata requis).
#   Alternative plus rapide pour une seule claim : edition directe dans l'UI
#   Wikidata (modifier la valeur 606 -> 622 sur l'enonce "nombre de pages").
#
# STATUT : DIFFERE. A executer plus tard, en batch avec les prochaines mises a
#   jour Wikidata. Source canonique de la valeur : data/works.yaml
#   (works > book-anthropie > pages = 622).
#
# QuickStatements V1 : une ligne prefixee "-" retire l'enonce ; sans prefixe, ajoute.
#
# --- 1) retirer l'ancienne valeur -------------------------------------------
-Q138827344	P1104	+606
# --- 2) ajouter la nouvelle valeur ------------------------------------------
Q138827344	P1104	+622
