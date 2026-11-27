# shellcheck shell=bash
# From corerope.space tools/lib/vercel.sh (itself from paperwright.diy); prefix sc_.
# Sourced by the deploy scripts (tools/site/deploy.sh): the Vercel
# token and the REST API, without the token ever reaching a command line, a log or the repo.
#
# Needs VERCEL_TOKEN, from the environment or from .env in this checkout or the main checkout
# (worktrees have no .env). Some Vercel CLI versions ignore VERCEL_TOKEN, so the CLI gets it from
# a private config directory (--global-config "$work/vercel") and curl from a private config
# file ($work/curl.cfg). Both live in a mode-700 folder the caller deletes on exit.

# sc_vercel_auth <repo root> <work dir>: writes <work>/vercel/auth.json and <work>/curl.cfg, then
# unsets VERCEL_TOKEN. Returns 1, saying why, when there is no token.
sc_vercel_auth() {
  local root="$1" work="$2" main_checkout env_file line
  if [[ -z "${VERCEL_TOKEN:-}" ]]; then
    main_checkout="$(dirname "$(git -C "$root" rev-parse --path-format=absolute --git-common-dir)")"
    for env_file in "$root/.env" "$main_checkout/.env"; do
      [[ -f "$env_file" ]] || continue
      line="$(grep -E '^VERCEL_TOKEN=' "$env_file" | tail -n 1 || true)"
      VERCEL_TOKEN="${line#VERCEL_TOKEN=}"
      VERCEL_TOKEN="${VERCEL_TOKEN%\"}" && VERCEL_TOKEN="${VERCEL_TOKEN#\"}"
      VERCEL_TOKEN="${VERCEL_TOKEN%\'}" && VERCEL_TOKEN="${VERCEL_TOKEN#\'}"
      [[ -n "$VERCEL_TOKEN" ]] && break
    done
  fi
  if [[ -z "${VERCEL_TOKEN:-}" ]]; then
    echo "no VERCEL_TOKEN in the environment or in .env" >&2
    return 1
  fi
  chmod 700 "$work"
  (
    umask 077
    mkdir -p "$work/vercel"
    printf '{"token":"%s"}\n' "$VERCEL_TOKEN" >"$work/vercel/auth.json"
    printf 'header = "Authorization: Bearer %s"\n' "$VERCEL_TOKEN" >"$work/curl.cfg"
  )
  unset VERCEL_TOKEN
  sc_vercel_work="$work"
}

# sc_api METHOD PATH [JSON]: the response body, then its HTTP status on the last line.
sc_api() {
  local args=(-sS --max-time 60 -K "$sc_vercel_work/curl.cfg" -X "$1" -w '\n%{http_code}')
  [[ $# -ge 3 ]] && args+=(-H 'Content-Type: application/json' --data "$3")
  curl "${args[@]}" "https://api.vercel.com$2"
}
sc_body() { sed '$d' <<<"$1"; }
sc_status() { tail -n 1 <<<"$1"; }

# sc_vercel_cli: sets sc_vercel to the Vercel CLI command (the installed one, else npx).
sc_vercel_cli() {
  sc_vercel=(vercel)
  command -v vercel >/dev/null || sc_vercel=(npx --yes vercel@61)
}

# sc_production_domains <project id> <team>: the project's verified domains that serve it
# (not redirects), one per line. People visit these; per-deployment URLs sit behind Vercel's
# deployment protection and prove nothing about the public site.
sc_production_domains() {
  local res
  res="$(sc_api GET "/v9/projects/$1/domains?slug=$2")"
  if [[ "$(sc_status "$res")" != 200 ]]; then
    echo "could not list domains: $(sc_body "$res" | head -c 400)" >&2
    return 1
  fi
  sc_body "$res" | jq -r '.domains[] | select(.verified and (.redirect == null)) | .name'
}
