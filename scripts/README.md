# Scripts utilitaires — anthropie-site

Outils Python pour interagir avec l'API Zenodo et maintenir le graphe de related_identifiers du corpus AWP (Anthropie Working Papers).

Tous les scripts necessitent la variable d'environnement `ZENODO_TOKEN` : token personnel Zenodo avec scopes `deposit:write` et `deposit:actions`. Obtenir un token : <https://zenodo.org/account/settings/applications/>

Sur Windows, stocker en variable User persistante (une seule fois) :

    [System.Environment]::SetEnvironmentVariable("ZENODO_TOKEN", "TOKEN_ICI", "User")

Le token reste disponible dans toutes les sessions PowerShell suivantes. Eviter absolument de le coller en clair dans l'historique.

## audit_zenodo.py

Audit en lecture seule des 10 records Zenodo AWP (5 FR + 5 EN). Inventorie l'etat des related_identifiers et signale les anomalies.

Usage :

    PYTHONIOENCODING=utf-8 python scripts/audit_zenodo.py

Sortie : rapport Markdown avec tableau des records et inventaire des related_identifiers par record.

Utile pour :
- Verifier la coherence du graphe avant/apres une operation d'ecriture
- Detecter les DOIs malformes ou les relations asymetriques
- Audit periodique (trimestriel recommande)

Le script utilise l'endpoint public /api/records/{id} (lecture seule). Un token valide est quand meme requis (le script le lit depuis ZENODO_TOKEN).

## zenodo_add_ssrn_links.py

Ajoute de facon idempotente les relations `isIdenticalTo` de chaque AWP EN Zenodo vers son pendant SSRN. Ne pose la relation que si le DOI SSRN resout publiquement (test HEAD sur doi.org).

Relation utilisee : `IsIdenticalTo` — justifiee par le fait que SSRN ne modifie pas les PDFs deposes (pas de page de garde ajoutee). Le fichier SSRN et le fichier Zenodo sont la meme ressource bit-a-bit. Verifie manuellement sur AWP-01 EN le 21/04/2026.

Usage :

    # Dry-run (obligatoire avant --apply)
    PYTHONIOENCODING=utf-8 python scripts/zenodo_add_ssrn_links.py
    
    # Application reelle (apres validation du dry-run)
    PYTHONIOENCODING=utf-8 python scripts/zenodo_add_ssrn_links.py --apply

Le script est idempotent : relancable autant de fois que necessaire sans effet indesirable. A chaque execution, les DOIs nouvellement publies sont traites, les autres skippes avec un warning explicite.

Workflow type : relancer a chaque mail SSRN "Your paper has been Accepted" recu sur les 4 AWP EN encore en PRELIMINARY_UPLOAD (AWP-02, AWP-03, AWP-04, AWP-05).

Etat initial (21/04/2026) : 1 AWP EN deja lie (AWP-01 EN -> SSRN 6543618), 4 en attente APPROVED.

Garde-fous internes :
- Test de resolution DOI via HEAD sur doi.org avant toute ecriture
- Verification d'idempotence (pas de double-pose)
- Dry-run par defaut (--apply requis pour ecrire)
- Preservation totale des related_identifiers existants (jamais d'ecrasement)
- Utilisation exclusive de /api/deposit/depositions/ pour les ecritures (format plat)

## audit_geo_v2.py

Audit GEO (Generative Engine Optimization) en lecture seule du site stephane-lalut.com. Version 2 refactoree suite a la contre-analyse methodologique du 20/04/2026.

Ameliorations v2 vs v1 :
- Phase de decouverte : les URLs a auditer sont derivees des sitemaps effectifs (fr/sitemap.xml, en/sitemap.xml), plus aucun chemin en dur
- Parsing JSON-LD en Python avec gestion correcte des structures imbriquees (@graph, sameAs en string ou array)
- Extraction des liens BibTeX/RIS/PDF depuis les pages HTML, au lieu de supposer des endpoints conventionnels
- Structure a deux parties : Partie A "on-site reproductible" / Partie B "annexe ecosysteme dates"
- Echelle a trois etats : present / manquant vs contrat / opportunite GEO 2026

Usage :

    PYTHONIOENCODING=utf-8 python scripts/audit_geo_v2.py > scripts/audit_geo_v2_latest.md
    
Sortie : rapport Markdown complet. Ne modifie rien sur le site.

Utile pour :
- Baseline comparative avant/apres chantier GEO
- Detection des leviers restants (PublicationSeries, isPartOf, citation, mainEntityOfPage, feed RSS, markdown endpoints)
- Audit trimestriel de la coherence semantique du corpus

## Notes techniques

Endpoints Zenodo :
- `/api/records/{id}` : lecture publique, metadonnees au format enrichi, non compatible PUT
- `/api/deposit/depositions/{id}` : lecture + ecriture proprietaire, format plat, obligatoire pour PUT

Sequence d'edition d'un record publie :
1. `POST /api/deposit/depositions/{id}/actions/edit` : ouvre brouillon
2. `PUT /api/deposit/depositions/{id}` avec `{"metadata": {...}}` : met a jour
3. `POST /api/deposit/depositions/{id}/actions/publish` : republie

Pattern DOI SSRN : `10.2139/ssrn.{abstract_id}` — strict, confirme sur papers SSRN de 2007 a 2024.

## Historique

- **21/04/2026** : creation initiale apres consolidation Phase 2 Zenodo.
  - audit_zenodo.py livre : 10/10 records accessibles, 60 related_identifiers inventories
  - zenodo_add_ssrn_links.py valide en dry-run (0 ajoute, 4 skippes DOI non resolu, 1 skippe deja pose)
  - En attente d'APPROVED SSRN pour AWP-02/03/04/05 EN
