# -*- coding: utf-8 -*-
"""Date de relevé d'un jeu publié : elle ne change qu'avec une DONNÉE.

MOTIF (17/10/2026, contre-expertise anthropie-site-20261017-030435, § 6 de l'arbitrage). Sept générateurs comparaient le
fichier entier, blocs de texte compris, pour décider « rien écrit », et posaient sinon la date du jour. Une correction
du seul texte avançait donc `releve_le`, et le bandeau de la page annonçait « Données mises à jour le » sans donnée
nouvelle (constaté sur dette_baisse le 17/10). Trois générateurs avaient déjà corrigé le défaut chacun à sa manière
(inflation et générations : comparaison hors affichage ; collectivités : grandeurs publiées). Les deux premiers adoptent
cet organe ; collectivités garde son critère, plus fin (exclusion déclarée).

RÈGLE. Les données d'un jeu = le fichier privé de toute clé « releve_le » (à toute profondeur), de « _licence », des
blocs de texte TEXTE et des textes de méthode `meta.definitions`. Données identiques au fichier en place : on garde son relevé, même si le texte change. La date de
la PAGE suit alors par data/dates_affichage.json (scripts/dates-affichage.py --ecrire ou --forme).

Ce qui n'est pas exclu reste daté prudemment : un texte rangé hors des blocs TEXTE (définitions, noms de gardes) avance
encore le relevé. Le défaut inverse, un relevé qui ne bouge pas avec une donnée, est impossible par construction : seule
une clé de TEXTE ou une date est retirée de la comparaison.

Contrôle bloquant : scripts/dates-affichage.py refuse un relevé avancé à données identiques (témoin 3).
"""
import json
from pathlib import Path

TEXTE = ("affichage", "affichage_en")


def _sans_dates(x):
    if isinstance(x, dict):
        return {k: _sans_dates(v) for k, v in x.items() if k != "releve_le"}
    if isinstance(x, list):
        return [_sans_dates(v) for v in x]
    if isinstance(x, float):
        # Bruit de calcul au 15e chiffre (ordre de sommation non déterministe : 73.94083458807205 contre …208, mesuré le
        # 17/10/2026 sur dette_dynamique, dette_monde et dette_generations) : ce n'est pas une donnée nouvelle.
        return float("%.12g" % x)
    return x


def donnees(jeu: dict) -> str:
    """Empreinte des données d'un jeu : sans dates de relevé, sans licence, sans blocs de texte."""
    c = json.loads(json.dumps(jeu, ensure_ascii=False, default=str))
    c = {k: v for k, v in c.items() if k != "_licence" and k not in TEXTE}
    if isinstance(c.get("meta"), dict):   # textes de méthode (repris de update_dette_generations.py, 11/10/2026)
        c["meta"] = {k: v for k, v in c["meta"].items() if k != "definitions"}
    return json.dumps(_sans_dates(c), ensure_ascii=False, sort_keys=True)


def releve_de(jeu: dict):
    """Relevé déclaré d'un jeu : à la racine, sinon dans `meta`."""
    return jeu.get("releve_le") or (jeu.get("meta") or {}).get("releve_le")


def releve(chemin, payload: dict, aujourdhui: str) -> str:
    """Relevé à écrire : celui du fichier en place si ses données sont celles de `payload`, sinon `aujourdhui`."""
    try:
        prev = json.loads(Path(chemin).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return aujourdhui
    anc = releve_de(prev) if isinstance(prev, dict) else None
    return anc if anc and donnees(prev) == donnees(payload) else aujourdhui
