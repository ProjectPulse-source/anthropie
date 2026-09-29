# Migration des runners GitHub vers Ubuntu 26.04 — dossier de suivi

**Source, lue le 2026-09-29** : `actions/runner-images#14748`. Verbatim :
« This change will be rolled out over a period of several weeks beginning
**October 19, 2026**. We plan to complete the migration by **November 19, 2026**. »
Repli documenté par GitHub : `ubuntu-24.04`. Test anticipé possible : `ubuntu-26.04`.

**Mesuré le 2026-09-29** sur le run `36543868062` : `ubuntu-latest` servait alors
`Image: ubuntu-24.04` (release `ubuntu24/20260920.314`).

## Le risque, et pourquoi il valait un geste

Pendant la fenêtre du 19/10 au 19/11, un même workflow peut tomber un jour sur
Ubuntu 24.04 et le lendemain sur 26.04, **sans aucun changement de code**. L'échec
serait donc **intermittent**, et on l'attribuerait à la donnée, au réseau ou au
hasard avant de penser à l'image. C'est la classe « état déclaré ≠ état réel »
appliquée à l'infrastructure : rien ne casse à l'endroit où la cause se trouve.

Les surfaces exposées ici ne sont pas décoratives : `dette-insee.yml` publie des
données officielles et déclenche le déploiement ; `hugo.yml` est le seul chemin par
lequel une page atteint le lecteur.

**Ce qui aurait été insuffisant** : attendre l'issue automatique du workflow. Elle
existe (job `alerte`), mais elle arrive *après* une publication manquée, et elle ne
dirait pas que la cause est l'image.

## Ce qui est fait

- **Épinglage sur `ubuntu-24.04`** de toutes les déclarations `runs-on`, dans les
  deux dépôts qui en portent : `anthropie-site` (7) et `monitoring` (2). C'était un
  changement **sans effet fonctionnel** au moment où il a été fait, puisque
  `ubuntu-latest` servait déjà 24.04 : il ne fige pas un comportement, il supprime
  seulement le non-déterminisme à venir.
- **Banc de test** `test-runner-ubuntu26.yml`, déclenchement **manuel uniquement**.
  Il rejoue les étapes qui peuvent casser — installation de Hugo Extended par
  `dpkg`, build `hugo --minify`, version de Python, import du script de données et
  ses dépendances — sur `ubuntu-26.04`, **sans rien publier ni déployer**.
- **Garde `scripts/check-runner-image.py`**, dans `check-all` hors `--ci` : elle
  vérifie que l'épinglage tient, signale tout retour à un label flottant, et rappelle
  l'échéance avec une insistance proportionnée au temps restant.

## Le banc a déjà tourné, et il est VERT — run `36545145119`, 2026-09-29

Mesuré sur `ubuntu-26.04`, en 21 secondes :

| Ce qui pouvait casser | Résultat |
|---|---|
| Image | `Ubuntu 26.04.1 LTS` |
| Python par défaut | **3.14.4** (contre 3.12 sur 24.04) |
| glibc — Hugo Extended en dépend | `2.43` |
| Hugo Extended par `dpkg`, puis `hugo --minify` | **passe**, `v0.147.0 extended` |
| `cairosvg` + gardes de `update_dette_insee.py --check` | **passent** |
| Porte bloquante `check-all.py --ci` | **passe** |

**Ce que cela règle** : la migration ne coûtera rien. Le saut de Python 3.12 à 3.14,
qui était le risque le plus plausible, ne casse ni le script de données ni les
contrôles.

**Ce que cela ne règle pas** : un run vert le 29/09 ne dit rien du 19/11. L'image
26.04 continuera d'évoluer jusqu'à la fin de la bascule — c'est précisément pourquoi
le banc reste en place et se relance en une commande.

## Ce qui reste à faire, dans l'ordre

1. **Rester sur `ubuntu-24.04` jusqu'à la fin de la bascule (19/11/2026).** Arbitrage :
   l'épinglage sur 24.04 est aujourd'hui strictement équivalent au comportement
   courant, alors que 26.04 est une image jeune qui bougera deux mois encore.
   Basculer maintenant échangerait un risque connu et nul contre un risque inconnu,
   sur la chaîne qui publie des données officielles.
2. **Relancer le banc après le 19/11** : `gh workflow run test-runner-ubuntu26.yml`,
   puis `gh run watch <id> --exit-status`.
3. **S'il est encore vert** : basculer les 9 déclarations sur `ubuntu-26.04` (7 ici,
   2 dans `monitoring`), relancer `dette-insee.yml` une fois à la main pour le
   constater en réel, puis **supprimer** le banc, la garde et ce dossier.
4. **S'il est rouge** : la cause est identifiée avant d'être subie, et il reste des
   semaines pour la traiter — c'est tout le bénéfice d'avoir testé tôt.

## Condition de mort — prédicat, jamais date

Ce dossier, le banc de test et la garde **disparaissent ensemble** le jour où les
neuf déclarations portent une image ≥ 26.04 et où un run vert l'a constaté. La garde
l'annonce d'elle-même quand c'est le cas : « MIGRATION TERMINEE […] SUPPRIMER ».

Tant que ces fichiers existent, c'est qu'il reste quelque chose à faire. Un dispositif
de transition qui survit à sa transition devient un décor, et le décor ne se lit plus.

## Reprise en une commande

À coller dans une session Claude Code ouverte sous `D:\PRO` :

```
Migration runners Ubuntu 26 : lis 01_SITE/anthropie-site/docs/MIGRATION_RUNNER_UBUNTU26.md, puis exécute le point 1 « ce qui reste à faire ».
```
