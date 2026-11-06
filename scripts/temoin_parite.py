#!/usr/bin/env python3
"""Témoin positif des gardes de parité téléphone (06/11/2026).

Une garde `parite_mobile(figs)` vérifie que chaque valeur dessinée dans la version téléphone d'une figure figure dans la
description de sa version détaillée, et que la police ne descend pas sous le minimum. Dans les générateurs du dossier
Promesses, elle n'avait jamais été vue mordre : un contrôle sans témoin positif est réputé absent (R5).

`exercer(parite_mobile, figs, log)` lui fait subir deux mutations sur la première figure « -m.svg » : une valeur
inconnue injectée dans une étiquette de classe « val », puis une police d'un pixel. Chacune doit l'arrêter, avec le motif
attendu (« absentes », « police »), sinon `RuntimeError`. Les figures réelles ne sont pas touchées (copie du dict).

Portée : les générateurs dont les valeurs dessinées portent `class="val"` (Adopter, Délais, Référendum). Les générateurs
du dossier École repèrent leurs valeurs autrement : point ouvert nommé dans PROJECT_STATUS.md (06/11/2026).
"""
from __future__ import annotations

MUTATIONS = (
    ("valeur inconnue", lambda s: s.replace('<text class="val"', '<text class="val">987654</text><text class="val"', 1), "absentes"),
    ("police d'un pixel", lambda s: s.replace('font-size="', 'font-size="1" data-temoin="', 1), "police"),
)


def exercer(parite_mobile, figs: dict, log) -> None:
    cle = next((k for k in figs if k.endswith("-m.svg") and '<text class="val"' in figs[k]), None)
    if cle is None:
        raise RuntimeError("temoin parite : aucune figure telephone avec une valeur de classe « val » (temoin inapplicable)")
    for nom, muter, motif in MUTATIONS:
        f2 = dict(figs)
        f2[cle] = muter(figs[cle])
        try:
            parite_mobile(f2)
        except Exception as e:  # la classe d'arrêt est propre à chaque générateur
            if motif not in str(e):
                raise RuntimeError("temoin parite (%s) : arret par une autre condition : %s" % (nom, e))
            log("autotest : la mutation a mordu : parite mobile, %s -> %s" % (nom, str(e)[:80]))
            continue
        raise RuntimeError("temoin parite (%s) : aucune garde n'a mordu, controle ABSENT" % nom)
