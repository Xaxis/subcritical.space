// From corerope.space tools/lib/gutter.ts (itself from paperwright.diy): full-bleed bands are
// allowed, so the check looks at blocks inside .wrap.
// What a phone shot checks beyond sideways scroll: the page's own blocks keep a side gutter, so
// no card or heading runs to the glass. Run in the page; the elements that touch an edge, named.
export function touchingEdges(): string[] {
  const min = 12;
  const width = document.documentElement.clientWidth;
  const out: string[] = [];
  for (const el of document.querySelectorAll("main .wrap > *, main .card, main h1")) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || getComputedStyle(el).position === "fixed") continue;
    if (r.left < min || r.right > width - min) {
      const cls =
        typeof el.className === "string" && el.className !== ""
          ? `.${el.className.split(" ")[0]}`
          : "";
      out.push(
        `${el.tagName.toLowerCase()}${cls} (${Math.round(r.left)} to ${Math.round(r.right)} px)`,
      );
    }
  }
  return out;
}
