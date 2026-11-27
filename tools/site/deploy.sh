#!/usr/bin/env bash
# Deploys subcritical.space to production on Vercel (project "subcritical", team xaxis-projects) and
# proves the live address serves this commit. From corerope.space tools/site/deploy.sh (itself from
# paperwright.diy), without its API and account checks: this site is static and takes no input.
#
#   tools/site/deploy.sh               deploy HEAD, then check it
#   tools/site/deploy.sh --check       only check that the live address serves HEAD
#   tools/site/deploy.sh --check SHA   only check that the live address serves SHA
#   tools/site/deploy.sh --no-browser  deploy HEAD and run the HTTP checks, but not the browser ones
#
# --no-browser is for a box with no free slot: Vercel builds the site on its own machines, so the
# upload needs none, and the browser checks follow later with `heavy tools/site/deploy.sh --check`.
# A deploy is proven only once that has passed.
#
# What goes up is the committed tree at HEAD (git archive), never the working tree, so the build
# marker names exactly what went live and nothing untracked, like .env, is uploaded. Vercel builds
# it: pnpm installs the workspace from the root lockfile and builds site/, the project's root
# directory, which reads research/ and data/ from the repository root. The project, its settings
# and its domains are set here, so they live in the repo.
#
# Until subcritical.space is registered (it has no nameservers), the domain is not added and the
# site lives at the project's vercel.app address, which site/lib/site.ts names as the canonical URL.
#
# A deploy counts only when a production domain proves it:
#   - / answers 200 with the security headers and this commit's build marker;
#   - its share card, icons, stylesheet, manifest, robots and sitemap answer with their types;
#   - a missing page is a 404;
#   - every page in the sitemap is shot at desktop and phone width, light and dark, none scrolls
#     sideways and axe finds nothing serious (tools/site/shots.ts);
#   - the figures, the theme toggle and the ledger links work in a browser (tools/site/interact.ts).
#
# Needs VERCEL_TOKEN, from the environment or from .env in this checkout or the main checkout
# (worktrees have no .env). The token never goes on a command line or into a log
# (tools/lib/vercel.sh). Run it through ~/.claude/claude-core/bin/heavy: the checks drive a browser.
set -euo pipefail

team="xaxis-projects"
project="subcritical"
apex="subcritical.space"

check_only=0
browser=1
want=""
case "${1:-}" in
"") ;;
--no-browser) browser=0 ;;
--check)
  check_only=1
  want="${2:-}"
  ;;
*)
  echo "usage: tools/site/deploy.sh [--check [SHA] | --no-browser]" >&2
  exit 2
  ;;
esac

root="$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)"
sha="$(git -C "$root" rev-parse --short=7 "${want:-HEAD}^{commit}")" || {
  echo "deploy: $want is not a commit here" >&2
  exit 2
}

fail() {
  echo "deploy FAILED: $*" >&2
  exit 1
}

# --- the token --------------------------------------------------------------------------------
# shellcheck source=tools/lib/vercel.sh
. "$root/tools/lib/vercel.sh"
work="$(mktemp -d "${TMPDIR:-/tmp}/subcritical-site.XXXXXX")"
trap 'rm -rf "$work"' EXIT
sc_vercel_auth "$root" "$work" || fail "no token"
api() { sc_api "$@"; }
body() { sc_body "$@"; }
status() { sc_status "$@"; }

# --- the project and its domains ----------------------------------------------------------------
# Root directory site, with the files outside it (research/, data/, the lockfile) included in the
# build, Next.js, Node 24. Install and build commands stay Vercel's defaults: pnpm install at the
# workspace root (found from pnpm-lock.yaml), then next build in site/.
settings='{"framework":"nextjs","rootDirectory":"site","sourceFilesOutsideRootDirectory":true,"nodeVersion":"24.x","buildCommand":null,"installCommand":null,"outputDirectory":null}'
res="$(api GET "/v9/projects/$project?slug=$team")"
if [[ "$(status "$res")" == 404 && $check_only == 0 ]]; then
  res="$(api POST "/v11/projects?slug=$team" "{\"name\":\"$project\",\"framework\":\"nextjs\"}")"
  [[ "$(status "$res")" == 200 ]] || fail "could not create project $project: $(body "$res" | head -c 400)"
  echo "created project $project"
fi
[[ "$(status "$res")" == 200 ]] || fail "project $project: $(status "$res") $(body "$res" | head -c 300)"
project_id="$(body "$res" | jq -er .id)"
org_id="$(body "$res" | jq -er .accountId)"

if [[ $check_only == 0 ]]; then
  res="$(api PATCH "/v9/projects/$project_id?slug=$team" "$settings")"
  [[ "$(status "$res")" == 200 ]] || fail "could not apply project settings: $(body "$res" | head -c 400)"
  have="$(body "$(api GET "/v9/projects/$project_id/domains?slug=$team")" | jq -r '.domains[].name')"
  add_domain() { # add_domain JSON NAME
    grep -qxF "$2" <<<"$have" && return 0
    local r
    r="$(api POST "/v10/projects/$project_id/domains?slug=$team" "$1")"
    [[ "$(status "$r")" == 200 ]] || fail "could not add $2: $(body "$r" | head -c 400)"
    echo "added domain $2"
  }
  if [[ -n "$(dig +short NS "$apex" 2>/dev/null)" ]]; then
    add_domain "{\"name\":\"$apex\"}" "$apex"
    add_domain "{\"name\":\"www.$apex\",\"redirect\":\"$apex\",\"redirectStatusCode\":308}" "www.$apex"
  else
    echo "note: $apex has no nameservers yet (not registered?); serving from the vercel.app address"
  fi
fi

# --- deploy -----------------------------------------------------------------------------------
if [[ $check_only == 0 ]]; then
  if [[ -n "$(git -C "$root" status --porcelain -- site research data tools/site package.json pnpm-lock.yaml pnpm-workspace.yaml)" ]]; then
    echo "note: uncommitted changes are not deployed; HEAD ($sha) is"
  fi
  mkdir "$work/src"
  git -C "$root" archive --format=tar HEAD | tar -x -C "$work/src"
  mkdir "$work/src/.vercel"
  printf '{"projectId":"%s","orgId":"%s"}\n' "$project_id" "$org_id" >"$work/src/.vercel/project.json"

  sc_vercel_cli
  echo "deploying $sha to $project (production) ..."
  if ! "${sc_vercel[@]}" deploy --prod --yes --global-config "$work/vercel" --cwd "$work/src" \
    --build-env "SUBCRITICAL_BUILD=$sha" --meta "commit=$sha" >"$work/deploy.log" 2>&1; then
    tail -n 40 "$work/deploy.log" >&2
    fail "vercel deploy"
  fi
  deployment="$(grep -oE 'https://[a-zA-Z0-9.-]+\.vercel\.app' "$work/deploy.log" | sed -n 1p || true)"
  echo "deployed: ${deployment:-unknown}"
fi

# The browser checks come from the same commit as the site they prove. Run from the working tree,
# an uncommitted edit to a check (this session's or another's) was tested against a site without
# it, and failed a good deploy. The archive borrows the checkout's node_modules (after the upload).
tools="$root/tools/site"
if [[ $check_only == 0 ]]; then
  ln -s "$root/node_modules" "$work/src/node_modules"
  tools="$work/src/tools/site"
fi

# The canonical address the pages name (share cards, sitemap): site/lib/site.ts's SITE.url.
canonical="$(git -C "$root" show "$sha:site/lib/site.ts" | sed -nE 's/^  url: "(https:[^"]+)",$/\1/p')"
[[ -n "$canonical" ]] || fail "no SITE.url in site/lib/site.ts"

# --- prove it ---------------------------------------------------------------------------------
# The production domains are what people visit. Per-deployment URLs sit behind Vercel's
# deployment protection, so they prove nothing about the public site.
listing="$(sc_production_domains "$project_id" "$team")" || fail "no domain listing"
mapfile -t domains <<<"$listing"
[[ -n "${domains[0]:-}" ]] || fail "the project has no production domain"

# A custom domain counts once its DNS points at Vercel; until then, say what it needs.
dns_todo=()
live=()
for domain in "${domains[@]}"; do
  if [[ "$domain" == *.vercel.app ]]; then
    live+=("$domain")
    continue
  fi
  cfg="$(body "$(api GET "/v6/domains/$domain/config?slug=$team")")"
  if [[ "$(jq -r '.misconfigured' <<<"$cfg")" == "false" ]]; then
    live+=("$domain")
  else
    dns_todo+=("$domain")
  fi
done
[[ -n "${live[0]:-}" ]] || fail "no production domain is reachable yet"

shots="${TMPDIR:-/tmp}/subcritical-site-$sha"
mkdir -p "$shots"
find "${TMPDIR:-/tmp}" -maxdepth 1 -type d -name 'subcritical-site-*' ! -path "$shots" -mmin +1440 \
  -exec rm -rf {} + 2>/dev/null || true
checks=0

expect_asset() { # expect_asset URL CONTENT-TYPE-PREFIX
  local h
  h="$(curl -sS --max-time 20 -D - -o /dev/null "$1")"
  grep -qE '^HTTP/[0-9.]+ 200' <<<"$h" || fail "$1: $(head -n 1 <<<"$h")"
  grep -qi "^content-type: $2" <<<"$h" || fail "$1: content-type is not $2"
  grep -qi '^x-content-type-options: nosniff' <<<"$h" || fail "$1: no X-Content-Type-Options"
  echo "  ok  $1 (200, $2)"
  checks=$((checks + 1))
}

for domain in "${live[@]}"; do
  url="https://$domain"
  echo "checking $url"
  # Aliasing a new production deployment takes a moment; wait up to two minutes for the marker.
  marker="<meta name=\"subcritical-build\" content=\"$sha\"/>"
  for _ in $(seq 1 24); do
    curl -sS --max-time 20 -D "$work/page.headers" -o "$work/page.html" "$url/" || true
    grep -qF "$marker" "$work/page.html" 2>/dev/null && break
    sleep 5
  done
  grep -qE '^HTTP/[0-9.]+ 200' "$work/page.headers" || fail "$url/: $(head -n 1 "$work/page.headers")"
  grep -qF "$marker" "$work/page.html" ||
    fail "$url/ does not serve $sha (it has: $(grep -oE 'subcritical-build" content="[^"]*"' "$work/page.html" || echo 'no marker'))"
  grep -qi '^x-content-type-options: nosniff' "$work/page.headers" || fail "$url/: no X-Content-Type-Options"
  grep -qi '^referrer-policy: strict-origin-when-cross-origin' "$work/page.headers" || fail "$url/: wrong Referrer-Policy"
  grep -qi '^x-frame-options: DENY' "$work/page.headers" || fail "$url/: no X-Frame-Options DENY"
  grep -qi "^content-security-policy: default-src 'self'" "$work/page.headers" || fail "$url/: no Content-Security-Policy"
  echo "  ok  $url/ (200, build $sha, nosniff, referrer-policy, frame DENY, CSP)"
  checks=$((checks + 1))

  # (sed -n 1p, not head: head exits early, and under pipefail the SIGPIPE fails the script.)
  og="$(grep -oE '<meta property="og:image" content="[^"]+"' "$work/page.html" | sed -nE '1s/.*content="([^"]+)"/\1/p' | sed 's/&amp;/\&/g' || true)"
  [[ "$og" == "$canonical/"* ]] || fail "og:image is not on $canonical: ${og:-missing}"
  expect_asset "$url${og#"$canonical"}" "image/png"
  css="$(grep -oE 'href="/_next/static/[^"]+\.css"' "$work/page.html" | sed -nE '1s/href="([^"]+)"/\1/p' || true)"
  [[ -n "$css" ]] || fail "no stylesheet linked from $url/"
  expect_asset "$url$css" "text/css"
  expect_asset "$url/icon.svg" "image/svg+xml"
  touch_icon="$(grep -oE '<link rel="apple-touch-icon" href="[^"]+"' "$work/page.html" | sed -nE '1s/.*href="([^"]+)"/\1/p' | sed 's/&amp;/\&/g' || true)"
  [[ -n "$touch_icon" ]] || fail "$url/ names no apple-touch-icon"
  expect_asset "$url$touch_icon" "image/png"
  expect_asset "$url/manifest.webmanifest" "application/manifest+json"
  expect_asset "$url/robots.txt" "text/plain"
  expect_asset "$url/sitemap.xml" "application/xml"

  code="$(curl -sS --max-time 20 -o /dev/null -w '%{http_code}' "$url/no-such-page")"
  [[ "$code" == 404 ]] || fail "$url/no-such-page returned $code, not 404"
  echo "  ok  $url/no-such-page (404)"
  checks=$((checks + 1))

  if [[ $browser == 0 ]]; then
    echo "  --  browser checks skipped (--no-browser): run heavy tools/site/deploy.sh --check"
    continue
  fi

  # Shots to look at: every page at desktop and phone width, light and dark, whole.
  name="${domain//./-}"
  if ! node "$tools/shots.ts" --url "$url" --out "$shots/$name" \
    >"$work/shots.log" 2>"$work/shots.err"; then
    cat "$work/shots.err" >&2
    fail "the pages' shots on $url (tools/site/shots.ts; shots in $shots/$name)"
  fi
  echo "  ok  every page answers as it should, no sideways scroll at 390 px, axe clean; shots in $shots/$name"
  checks=$((checks + 1))

  if ! node "$tools/interact.ts" --url "$url" >"$work/interact.log" 2>&1; then
    cat "$work/interact.log" >&2
    fail "the interactive checks on $url (tools/site/interact.ts)"
  fi
  echo "  ok  the figures, theme toggle and ledger links work on $url"
  checks=$((checks + 1))
done

# www only redirects, so it is not a production domain above; check it once its DNS is right.
registered() { [[ -n "$(dig +short NS "$apex" 2>/dev/null)" ]]; }
dns_ok() { [[ "$(body "$(api GET "/v6/domains/$1/config?slug=$team")" | jq -r .misconfigured)" == "false" ]]; }
if registered && dns_ok "www.$apex"; then
  code="$(curl -sS --max-time 20 -o /dev/null -w '%{http_code} %{redirect_url}' "https://www.$apex/" || true)"
  [[ "$code" == "308 https://$apex/" ]] || fail "https://www.$apex/ answers '$code', not a 308 to https://$apex/"
  echo "  ok  https://www.$apex/ (308 to https://$apex/)"
  checks=$((checks + 1))
elif registered; then
  dns_todo+=("www.$apex")
fi

if [[ $browser == 1 ]]; then
  echo "site ok: $sha is live at ${live[*]/#/https://} ($checks checks passed)"
else
  echo "site up, not yet proven: $sha is live at ${live[*]/#/https://} ($checks HTTP checks passed; browser checks pending)"
fi
if ! registered; then
  echo "waiting for the owner: $apex is not registered yet; once it is, rerun this to add it"
fi
for domain in "${dns_todo[@]}"; do
  cfg="$(body "$(api GET "/v6/domains/$domain/config?slug=$team")")"
  if [[ "$domain" == "$apex" ]]; then
    echo "waiting for DNS: $domain needs an A record for the bare domain (host @):"
    jq -r '.recommendedIPv4 // [] | map(select(.rank == 1)) | .[].value[] | "    A      @    \(.)"' <<<"$cfg"
  else
    echo "waiting for DNS: $domain needs a CNAME record (host www):"
    jq -r '.recommendedCNAME // [] | map(select(.rank == 1)) | .[].value | "    CNAME  www  \(.)"' <<<"$cfg"
  fi
done
