import type { MetadataRoute } from "next";
import {
  experimentPlan,
  paperSections,
  researchDocs,
  surveyNotes,
  verificationReports,
} from "@/lib/docs";
import { SITE } from "@/lib/site";

export const dynamic = "force-static";

/** Every public page. tools/site/shots.ts reads this sitemap, so a page listed here gets checked. */
function pages(): string[] {
  return [
    "/",
    ...(paperSections().length > 0 ? ["/paper"] : []),
    "/research",
    ...researchDocs().map((d) => `/research/${d.slug}`),
    ...surveyNotes().map((d) => `/notes/${d.slug}`),
    ...verificationReports().map((d) => `/verification/${d.slug}`),
    ...(experimentPlan() ? ["/experiments"] : []),
    "/numbers",
    "/sources",
  ];
}

export default function sitemap(): MetadataRoute.Sitemap {
  return pages().map((p) => ({ url: `${SITE.url}${p === "/" ? "" : p}` }));
}
