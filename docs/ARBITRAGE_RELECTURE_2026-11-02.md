# Arbitrage de la contre-expertise sur les 22 pages — 02/11/2026

Pièce arbitrée : `D:\CONTRE_EXPERTISE\2026-11-02_RELECTURE_22_PAGES\Relecture_verbatim.txt`, SHA-256
`5574a45281b8c73a8eb1b94541086534efa1d8dc6de550340f7aa1e816632e0e`. Rien n'est encore modifié sur le site.

**Finalité** : crédibilité des travaux. **Objectif** : qu'aucune conclusion publiée ne dépasse ses preuves. **Vérifié** dans
`data/dette_dynamique.json` (moyennes recalculées), sur le texte du build, et sur Légifrance pour le docteur junior.

## Décisions

| Point | Décision | Preuve |
|---|---|---|
| Ne pas relire les 258 segments, concentrer l'effort | **ACCEPTÉ** | 226 segments sur deux pages |
| P0 : écart 1,70 / 1,90 point | **RÉSOLU, ACCEPTÉ AVEC MODIFICATION** | Solde corrigé (UBLGBP) −1,326 → −3,030 = −1,703 ; structurel (UBLGBPS) −1,082 → −2,995 = −1,913. L'écart de 0,21 vient de la première période (0,24 contre 0,04) : structurel moins corrigé vaut 0,89 point en 2019 seul. L'hypothèse des mesures ponctuelles est confirmée par les séries. La cause précise de 2019 n'est pas établie ici. La page ne dit pas que ces deux soldes diffèrent : à ajouter |
| P0 : 0,22 et 0,23 point | **VÉRIFIÉ, ACCEPTÉ AVEC MODIFICATION** | Observé moins structurel : 0,225 ; FMI : 0,228, moyennes 2022-2025. Ajouter « de PIB ». Mélange de dénominateurs (PIB, PIB potentiel) réel et déjà signalé sous le tableau |
| « d'après 2022 » | **ACCEPTÉ** | 2022 est dans la période. Page et générateur, FR et EN |
| « la conjoncture ne l'explique pas » | **ACCEPTÉ** | Devient « ne suffit pas à l'expliquer » : page, générateur, FR et EN |
| « C'est une différence de définition, non de données » | **ACCEPTÉ AVEC MODIFICATION** | Écart et intérêts reçus proches, mais 0,25 contre 0,18 en 2023 : la phrase est trop catégorique |
| 52,4 % et 46,5 % | **VÉRIFIÉ, SANS CORRECTION** | Ligne Croatie du tableau, identique en FR et EN. Fragments de cellules sortis de leur contexte par le contrôle |
| Citation du docteur junior | **VÉRIFIÉ, SANS CORRECTION** | CSP art. R6153-1-2, en vigueur : mot pour mot. La lecture de la page (recours à tout moment, responsabilité du praticien) suit l'article |
| Citations du référendum à attribuer à la loi organique | **REJETÉ, SANS OBJET** | La page indique déjà « institutional act, art. 9 » |
| Collectivités : statut juridique | **VÉRIFIÉ, SANS CORRECTION** | La page date l'état du texte et le nomme « projet de loi de finances » |
| « coïncidence » (66 et 65,7 milliards) | **REJETÉ** | Mot exact et clair, après l'énoncé des différences d'année, de périmètre et de nature |
| Tableau supplémentaire recettes et dépenses | **REJETÉ** | Les deux comparaisons tiennent dans le paragraphe ; une phrase de plus suffit |
| Rappeler points de PIB potentiel, non euros | **ACCEPTÉ AVEC MODIFICATION** | Déjà dit (« points de PIB potentiel ») ; seule la phrase récente en a besoin |
| « Trois niveaux » observation, décomposition, cause | **ACCEPTÉ, déjà appliqué** | Paragraphe « Ce que ce partage ne dit pas », conservé |
| Exclure les libellés de navigation du contrôle de relecture | **ACCEPTÉ** | Les 11 alertes B en sortent ; correction d'un filtre, pas un nouveau dispositif |
| Classification du risque et contrôle des dépendances | **REJETÉ** | Doctrine R2. Générateur unique, pièces sous SHA-256 et témoins bloquants tiennent déjà la chaîne de preuve |
| Note de traçabilité 6/10 | **REJETÉ** | Jugée sur un relevé d'extraits, pas sur le jeu publié |
| Cohérence avec les diagnostics Commission et FMI de 2026 | **NON VÉRIFIABLE** | Sources non lues ici ; la pièce n'en dit pas assez pour conclure |

## Corrections à appliquer

1. `content/pourquoi-la-dette-publique-augmente/_index.md` et `.en.md` : période, « ne suffit pas à l'expliquer », écart 1,70 / 1,9, « de PIB », définition du solde.
2. `scripts/update_dette_dynamique.py` (`montre_cs`, FR et EN), puis `data/figures_dynamique.json`.
3. `scripts/check-relecture.py` : retirer la ligne d'appartenance.
4. Relecture humaine des pages du groupe A, instantanés mis à jour ensuite.

## Limites

Les estimations AMECO, FMI et OCDE sont reprises des pièces archivées, pas réestimées. Les 226 segments des deux pages longues
n'ont pas été relus un à un par ce contrôle : ils restent à la relecture de l'auteur.
