// Pure text rules shared by the pages and the tests: how a research file becomes a page address,
// how a heading becomes an anchor, and how citations and cross-links in the Markdown resolve.

/** A heading's anchor, the same rule for the table of contents and the rendered heading. */
/** The text with its first letter capitalised. */
export const capital = (w: string) => w.charAt(0).toUpperCase() + w.slice(1);

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/[*_`]/g, "")
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-");
}

/** research/00-memo.md is /research/memo: the order prefix and extension go. */
export function docSlug(file: string): string {
  const name = file.split("/").pop() ?? file;
  return name.replace(/\.md$/, "").replace(/^\d+-/, "");
}

/** The ledger id a link points at, if it is a ledger link (numbers.md#id, from research/ or paper/). */
export function ledgerId(href: string): string | null {
  const m = /^(?:\.\.\/research\/)?numbers\.md#([a-z0-9-]+)$/.exec(href);
  return m ? (m[1] as string) : null;
}

/** A link from one research file to another becomes a link to that file's page. */
export function docHref(href: string): string | null {
  const m = /^(?:\.\.\/research\/|\.\/)?(\d+-[a-z0-9-]+)\.md(#[\w-]+)?$/.exec(href);
  if (!m) return null;
  return `/research/${docSlug(`${m[1]}.md`)}${m[2] ?? ""}`;
}

// The same patterns as tools/check.py, so the site and the check agree on what a citation is.
const CITE_GROUP = /\[([^[\]]*@[^[\]]*)\](?!\()/g;
const CITE_KEY = /(?<![\w.])@([A-Za-z][\w:-]*[\w])/g;

/**
 * Pandoc citations, [@key] or [@a; @b], become links to the source list, labelled by `label`
 * (author and year). Anything that is already a Markdown link is left alone.
 */
export function linkCitations(
  md: string,
  label: (key: string) => string,
  anchor: (key: string) => string = (k) => k,
): string {
  return md.replace(CITE_GROUP, (whole, inner: string) => {
    const keys = [...inner.matchAll(CITE_KEY)].map((m) => m[1] as string);
    if (keys.length === 0) return whole;
    return `(${keys.map((k) => `[${label(k)}](/sources#${anchor(k)})`).join("; ")})`;
  });
}

/** The experiments research/04-claims.md numbers (its build list), or the memo's eleven before it. */
export function plannedExperiments(claims: string | null): number {
  if (claims === null) return 11;
  const at = claims.search(/^## Experiments\b/m);
  if (at < 0) return 11;
  const list = claims.slice(at).split(/\n## /)[0] ?? "";
  return new Set([...list.matchAll(/^\d+\. \*\*(E\d+)\b/gm)].map((m) => m[1])).size || 11;
}

// A person's name: up to five words, each capitalised, an initial or a surname particle.
const PERSON =
  /^(?:(?:\p{Lu}[\p{L}'’-]*\.?|van|von|de|der|den|da|del|di|la|le|du|bin|ibn|al|el)\s+){1,4}\p{Lu}[\p{L}'’-]+$/u;
// Words that make a capitalised name an organisation's, and acronyms such as METR or IAEA.
const ORG =
  /\b(?:AI|Institute|Agency|Foundation|Department|Council|Commission|Office|Research|Labs?|Laboratory|Group|Centre|Center|University|Committee|Association|Corporation|Inc|Ltd|Company|Bureau|Ministry|Organi[sz]ation|Government|Union|Nations|Board|Authority|Team|Forum|Society|Federation|Holding)\b|(?:^|\s)\p{Lu}{2,}(?:\s|$)/u;

const isPerson = (name: string) => PERSON.test(name) && !ORG.test(name);
// A fragment that only continues a name with a comma in it: "Memphis Light, Gas and Water".
const CONTINUES = /^\p{Lu}[\p{L}'’-]*(?:\s+(?:and|of|for|the|\p{Lu}[\p{L}'’-]*))*$/u;
const continues = (seg: string) => CONTINUES.test(seg) && !isPerson(seg) && !ORG.test(seg);

/**
 * A short in-text label: the first author's surname, or the organisation's name, and the year.
 * Affiliations in brackets are dropped, and "et al." is added only when another person follows.
 */
export function citeLabel(
  s: { authors?: string; year?: number; title: string } | undefined,
  key: string,
): string {
  if (!s) return key;
  const year = s.year ?? "n.d.";
  let authors = (s.authors ?? "").replace(/\s*\([^)]*\)/g, "").trim();
  if (authors === "") return `${s.title.split(/\s+/).slice(0, 3).join(" ")} ${year}`;
  const etAl = /,?\s*et al\.?$/.test(authors);
  authors = authors.replace(/,?\s*et al\.?$/, "");
  const [group = "", ...groups] = authors.split(/\s*;\s*/);
  const segs = group.split(/\s*,\s*/);
  let n = 1;
  while (n < segs.length && continues(segs[n] as string)) n++;
  const name = segs.slice(0, n).join(", ");
  if (n > 1) return `${name} ${year}`;
  const people = name.split(/\s+and\s+/);
  const lead = (people[0] ?? "").replace(/\s+(?:Jr\.?|Sr\.?|II|III|IV)$/, "");
  if (!isPerson(lead)) return `${name} ${year}`;
  const rest = [...segs.slice(n), ...groups];
  const many = etAl || people.length > 1 || rest.some((r) => isPerson(r.replace(/^and\s+/, "")));
  return `${lead.split(/\s+/).at(-1)}${many ? " et al." : ""} ${year}`;
}
