import type { MetadataRoute } from "next";
import { researchDocs, surveyNotes } from "@/lib/docs";
import { SITE } from "@/lib/site";

export const dynamic = "force-static";

/** Every public page. tools/site/shots.ts reads this sitemap, so a page listed here gets checked. */
function pages(): string[] {
  return [
    "/",
    "/research",
    ...researchDocs().map((d) => `/research/${d.slug}`),
    ...surveyNotes().map((d) => `/notes/${d.slug}`),
    "/numbers",
    "/sources",
  ];
}

export default function sitemap(): MetadataRoute.Sitemap {
  return pages().map((p) => ({ url: `${SITE.url}${p === "/" ? "" : p}` }));
}
