#!/usr/bin/env bash
# audit_scholar.sh — Audit balises Google Scholar sur pages AWP du site live
# Référence : brief « Audit balises Google Scholar — pages AWP » (20/04/2026)
# Exécute : bash audit_scholar.sh
# Dépendances : curl, grep, sed (présents sur Git Bash / WSL / Linux / macOS)

set -u
BASE="https://stephane-lalut.com"
REPORT="audit_scholar_$(date +%Y%m%d_%H%M).md"

# Table de vérité : chemin | DOI attendu | AWP-NN | langue
# Source : brief section 7
declare -a AWPS=(
  "/awp/awp-01/|10.5281/zenodo.19266862|AWP-01|fr"
  "/awp/awp-02/|10.5281/zenodo.19268037|AWP-02|fr"
  "/awp/awp-03/|10.5281/zenodo.19268769|AWP-03|fr"
  "/awp/awp-04/|10.5281/zenodo.19269244|AWP-04|fr"
  "/awp/awp-05/|10.5281/zenodo.19269486|AWP-05|fr"
  "/en/awp/awp-01/|10.5281/zenodo.19431208|AWP-01|en"
  "/en/awp/awp-02/|10.5281/zenodo.19433086|AWP-02|en"
  "/en/awp/awp-03/|10.5281/zenodo.19434094|AWP-03|en"
  "/en/awp/awp-04/|10.5281/zenodo.19439921|AWP-04|en"
  "/en/awp/awp-05/|10.5281/zenodo.19440866|AWP-05|en"
)

OBLIGATORY=(citation_title citation_author citation_publication_date citation_pdf_url)
RECOMMENDED=(citation_doi citation_technical_report_number citation_technical_report_institution citation_language citation_keywords citation_abstract)

extract_meta() {
  local html="$1" name="$2"
  # 1. Aplatir les retours ligne (HTML minifié ou pas)
  # 2. Isoler chaque <meta …>
  # 3. Ne garder que celles qui ont name=<X> avec frontière (guillemets ou espace ou >)
  # 4. Extraire content=<valeur>, en gérant "…", '…' et valeur sans guillemets (mono-mot)
  # 5. Dégager les guillemets
  echo "$html" \
    | tr '\n\r\t' '   ' \
    | grep -oE '<meta[[:space:]][^>]+>' \
    | grep -E "[[:space:]]name=[\"']?${name}([[:space:]>\"'/]|\$)" \
    | head -1 \
    | grep -oE "content=(\"[^\"]*\"|'[^']*'|[^ >]+)" \
    | head -1 \
    | sed -E 's/^content=//' \
    | sed -E "s/^[\"']//; s/[\"']\$//"
}

extract_h1() {
  echo "$1" \
    | tr '\n\r\t' '   ' \
    | grep -oE '<h1[^>]*>[^<]*</h1>' \
    | head -1 \
    | sed -E 's/<[^>]+>//g; s/^ +| +$//g'
}

row() { printf "| %s | %s | %s |\n" "$1" "$2" "$3"; }

{
  echo "# Audit balises Google Scholar — pages AWP"
  echo
  echo "Généré : $(date '+%Y-%m-%d %H:%M')  "
  echo "Base : \`${BASE}\`"
  echo
  echo "---"
  echo

  # -------- 1. robots.txt --------
  echo "## 1. robots.txt"
  echo
  ROBOTS=$(curl -sS "${BASE}/robots.txt" || echo "")
  if echo "$ROBOTS" | grep -qE "^[[:space:]]*Disallow:[[:space:]]*/awp"; then
    echo "❌ \`/awp/\` bloqué dans robots.txt"
  elif echo "$ROBOTS" | grep -qE "^[[:space:]]*Disallow:[[:space:]]*/[[:space:]]*\$"; then
    echo "❌ \`Disallow: /\` global détecté"
  else
    echo "✅ \`/awp/\` non bloqué"
  fi
  if echo "$ROBOTS" | grep -qiE "^[[:space:]]*Sitemap:"; then
    echo "✅ Directive Sitemap présente"
  else
    echo "⚠️ Pas de directive Sitemap"
  fi
  echo
  echo "\`\`\`"
  echo "$ROBOTS"
  echo "\`\`\`"
  echo

  # -------- 2. sitemap.xml --------
  echo "## 2. sitemap.xml — présence des 10 URLs AWP"
  echo
  SITEMAP=$(curl -sS "${BASE}/sitemap.xml" || echo "")
  echo "| URL AWP | Présent |"
  echo "|---|---|"
  for entry in "${AWPS[@]}"; do
    IFS='|' read -r path _ _ _ <<< "$entry"
    if echo "$SITEMAP" | grep -qF "${BASE}${path}"; then
      echo "| \`${path}\` | ✅ |"
    else
      echo "| \`${path}\` | ❌ |"
    fi
  done
  echo

  # -------- 3. Balises par page --------
  echo "## 3. Balises citation_* par page AWP"
  echo

  for entry in "${AWPS[@]}"; do
    IFS='|' read -r path expected_doi expected_awp expected_lang <<< "$entry"
    full_url="${BASE}${path}"
    echo "### ${expected_awp} · ${expected_lang} · \`${path}\`"
    echo

    HTTP_CODE=$(curl -sS -L -o /dev/null -w "%{http_code}" "${full_url}")
    if [[ "$HTTP_CODE" != "200" ]]; then
      echo "❌ **HTTP ${HTTP_CODE}** — page inaccessible, contrôles sautés"
      echo
      continue
    fi
    HTML=$(curl -sS -L "${full_url}")
    echo "✅ HTTP 200"
    echo
    echo "| Balise | Statut | Valeur (tronquée 80 car.) |"
    echo "|---|---|---|"

    # Obligatoires — présence
    for tag in "${OBLIGATORY[@]}"; do
      val=$(extract_meta "$HTML" "$tag")
      if [[ -z "$val" ]]; then row "\`${tag}\`" "❌ ABSENT" "—"
      else row "\`${tag}\`" "✅" "\`${val:0:80}\`"
      fi
    done

    # Recommandées — présence + valeur pour les 3 qui ont une vérité attendue
    for tag in "${RECOMMENDED[@]}"; do
      val=$(extract_meta "$HTML" "$tag")
      case "$tag" in
        citation_doi)
          if [[ -z "$val" ]]; then row "\`${tag}\`" "❌ ABSENT" "—"
          elif [[ "$val" == "$expected_doi" ]]; then row "\`${tag}\`" "✅" "\`${val}\`"
          else row "\`${tag}\`" "⚠️ VALEUR" "\`${val}\` — attendu \`${expected_doi}\`"
          fi ;;
        citation_technical_report_number)
          if [[ -z "$val" ]]; then row "\`${tag}\`" "❌ ABSENT" "—"
          elif [[ "$val" == "$expected_awp" ]]; then row "\`${tag}\`" "✅" "\`${val}\`"
          else row "\`${tag}\`" "⚠️ VALEUR" "\`${val}\` — attendu \`${expected_awp}\`"
          fi ;;
        citation_language)
          if [[ -z "$val" ]]; then row "\`${tag}\`" "❌ ABSENT" "—"
          elif [[ "$val" == "$expected_lang" ]]; then row "\`${tag}\`" "✅" "\`${val}\`"
          else row "\`${tag}\`" "⚠️ VALEUR" "\`${val}\` — attendu \`${expected_lang}\`"
          fi ;;
        *)
          if [[ -z "$val" ]]; then row "\`${tag}\`" "❌ ABSENT" "—"
          else row "\`${tag}\`" "✅" "\`${val:0:80}\`"
          fi ;;
      esac
    done

    # Contrôles de format
    author=$(extract_meta "$HTML" "citation_author")
    if [[ "$author" == "Lalut, Stéphane" ]]; then row "*format auteur*" "✅" "\`Lalut, Stéphane\`"
    elif [[ -n "$author" ]]; then row "*format auteur*" "⚠️" "\`${author}\` — attendu \`Lalut, Stéphane\`"
    fi

    date_val=$(extract_meta "$HTML" "citation_publication_date")
    if [[ "$date_val" =~ ^[0-9]{4}(/[0-9]{2}){0,2}$ ]]; then row "*format date*" "✅" "\`${date_val}\`"
    elif [[ -n "$date_val" ]]; then row "*format date*" "⚠️" "\`${date_val}\` — attendu YYYY/MM/DD, YYYY/MM ou YYYY"
    fi

    # Nombre de balises citation_author (doit être 1)
    n_authors=$(echo "$HTML" | grep -ocE "<meta[^>]*name=[\"']citation_author[\"']")
    if [[ "$n_authors" -eq 1 ]]; then row "*unicité auteur*" "✅" "1 balise"
    else row "*unicité auteur*" "⚠️" "${n_authors} balises citation_author"
    fi

    # <h1> présent et non égal au nom du site
    H1=$(extract_h1 "$HTML")
    if [[ -z "$H1" ]]; then row "*&lt;h1&gt;*" "❌ ABSENT" "—"
    elif [[ "$H1" =~ ^St[ée]phane\ Lalut ]]; then row "*&lt;h1&gt;*" "⚠️" "\`${H1}\` — risque : Scholar peut prendre le nom du site pour titre"
    else row "*&lt;h1&gt;*" "✅" "\`${H1:0:80}\`"
    fi

    # PDF URL accessible
    pdf_url=$(extract_meta "$HTML" "citation_pdf_url")
    if [[ -n "$pdf_url" ]]; then
      pdf_code=$(curl -sS -L -o /dev/null -w "%{http_code}" "$pdf_url")
      if [[ "$pdf_code" == "200" ]]; then row "*PDF accessible*" "✅" "HTTP 200"
      else row "*PDF accessible*" "❌" "HTTP ${pdf_code} — \`${pdf_url:0:60}\`"
      fi
    fi

    echo
  done

  # -------- 4. Résumé --------
  echo "## 4. Résumé"
  echo
  echo "Audit terminé. Vérifier les ❌ et ⚠️ ci-dessus."
  echo

} > "$REPORT"

echo "Rapport généré : $REPORT"
