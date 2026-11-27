import type { Metadata } from "next";
import { Page } from "@/components/Page";
import { repoLink } from "@/lib/site";
import { sourceHref, sources } from "@/lib/sources";

export const metadata: Metadata = {
  title: "Sources",
  description: "Every source Subcritical cites, each with a DOI, arXiv ID, ISBN or URL.",
  alternates: { canonical: "/sources" },
};

export default function Sources() {
  const all = sources();
  return (
    <Page
      current="/sources"
      eyebrow="Sources"
      title="Every source, with its identifier"
      lead={
        <p>
          A citation in the research resolves to an entry here, and every entry has a DOI, arXiv ID,
          ISBN or URL. A source nobody opened is not cited. The list is kept in{" "}
          <a href={repoLink("research/sources.toml")} rel="noopener">
            research/sources.toml
          </a>
          .
        </p>
      }
    >
      {all.length === 0 ? (
        <p className="callout">
          No sources yet. The survey is under way in ten tracks; each source enters this list once
          its track is merged and the source has been opened and checked.
        </p>
      ) : (
        <ol className="source-list">
          {all.map((s) => {
            const href = sourceHref(s);
            return (
              <li key={s.key} id={s.key} className="source">
                <span className="code">{s.key}</span>
                <span className="title">
                  {href ? (
                    <a href={href} rel="noopener">
                      {s.title}
                    </a>
                  ) : (
                    s.title
                  )}
                </span>
                <span className="muted">
                  {[s.authors, s.year ?? (s.undated ? "undated" : ""), s.type]
                    .filter(Boolean)
                    .join(" · ")}
                </span>
              </li>
            );
          })}
        </ol>
      )}
    </Page>
  );
}
