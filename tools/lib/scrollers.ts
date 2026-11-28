// A scroll container whose content overflows and whose own background is opaque, named. Chromium
// composites such a scroller, and under SwiftShader a full-page capture of a tall page holding one
// stalls: a minute or more a segment, or past the timeout. Readers never see it; the shots that
// prove a deploy do. The fix is to leave the scroller transparent and give the colour to its
// content (site/app/globals.css, .table-wrap and .prose pre). Run in the page.
export function opaqueScrollers(): string[] {
  const out: string[] = [];
  for (const el of document.querySelectorAll("body *")) {
    const cs = getComputedStyle(el);
    const scrolls = (o: string) => o === "auto" || o === "scroll";
    const overflows =
      (scrolls(cs.overflowX) && el.scrollWidth > el.clientWidth + 1) ||
      (scrolls(cs.overflowY) && el.scrollHeight > el.clientHeight + 1);
    if (!overflows) continue;
    const alpha = /^rgba\(.*,\s*([\d.]+)\)$/.exec(cs.backgroundColor);
    const opaque =
      cs.backgroundColor.startsWith("rgb(") || (alpha !== null && Number(alpha[1]) >= 1);
    if (!opaque) continue;
    const cls =
      typeof el.className === "string" && el.className !== ""
        ? `.${el.className.split(" ")[0]}`
        : "";
    out.push(`${el.tagName.toLowerCase()}${cls}`);
  }
  return [...new Set(out)];
}
