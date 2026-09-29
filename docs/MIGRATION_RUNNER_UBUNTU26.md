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

## Ce qui reste à faire, dans l'ordre

1. **Avant le 19 octobre 2026** — lancer le banc de test :
   `gh workflow run test-runner-ubuntu26.yml` puis `gh run watch <id> --exit-status`.
2. **S'il est vert** : basculer les 9 déclarations sur `ubuntu-26.04`, relancer
   `dette-insee.yml` une fois à la main pour le constater en réel, puis **supprimer**
   le banc de test et la garde (voir ci-dessous).
3. **S'il est rouge** : la cause est identifiée avant d'être subie. Corriger sous
   `ubuntu-26.04` — le plus probable étant la version de Python par défaut ou une
   dépendance de `cairosvg` — puis reprendre au point 2.

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
