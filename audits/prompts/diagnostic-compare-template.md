# Prompt — Audit diagnostique comparatif

À utiliser à J+30 / J+60 / J+90 depuis l'audit du 23 mai 2026.

---

## Contexte

Tu travailles dans le repo local du site stephane-lalut.com.

L'audit de référence est `audits/diagnostic-2026-05-23.md` (verdict initial : aucun défaut bloquant ; 7 items journalisés post-90j).

Depuis cette date, plusieurs commits post-diagnostic ont été appliqués au site :
- Vague 1 (post-diag-00 à post-diag-03) : audit archivé, sameAs SocArXiv, about Livresque conditionné, ItemList /livres/
- Vague 2 (post-diag-04 à post-diag-06) : section Anthropocène, single-source Phase 1, titre AWP-06 médian
- Post-Vague 2 (post-diag-07 à post-diag-09) : CSS sous-titre AWP-06, outillage GitHub Actions, drafts Phase 2

## Périmètre

Cet audit est COMPARATIF et DIAGNOSTIQUE PUR.
- Aucune modification de fichier
- Aucun patch proposé
- Lecture seule

## Objectif

Produire `audits/diagnostic-compare-AAAA-MM-JJ.md` qui contient :

1. **Récapitulatif des actions appliquées** depuis le 23 mai (lecture du git log entre les commits 5ac05b5 et HEAD)

2. **Re-audit synthétique** des 7 dimensions du rapport initial, avec gravité graduée identique
   - Mettre en évidence : ce qui a été corrigé, ce qui a persisté, ce qui est apparu

3. **Indicateurs externes au jour de l'audit comparatif** :
   - OpenAlex A5130851063 : nombre de works listés, présence d'AWP-01 et AWP-06
   - Téléchargements Zenodo cumulés (lire snapshot le plus récent dans `config/zenodo_awp_records.toml` ou équivalent)
   - SocArXiv : statut des 5 appels (vérifier via osf.io/ymkpj)
   - Search Console : à compléter manuellement (data non accessible en automatisation)
   - GoatCounter : à compléter manuellement

4. **Items du journal post-90j initial** : statut de chacun (fait, en cours, reporté, abandonné)

5. **Anomalies nouvelles** détectées depuis le 23 mai

6. **Recommandations pour la fenêtre suivante** (sans patch proposé) :
   - Ce qui peut continuer en l'état
   - Ce qui mérite une action (avec gravité)
   - Ce qui peut être abandonné comme non-pertinent

## Sortie

Rapport markdown unique dans `audits/diagnostic-compare-AAAA-MM-JJ.md`, structure identique à l'original pour permettre comparaison côte à côte.
