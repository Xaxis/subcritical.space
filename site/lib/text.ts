// Pure text rules shared by the pages and the tests: how a research file becomes a page address,
// how a heading becomes an anchor, and how citations and cross-links in the Markdown resolve.

/** A heading's anchor, the same rule for the table of contents and the rendered heading. */
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
