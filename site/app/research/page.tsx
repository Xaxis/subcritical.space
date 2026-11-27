import type { Metadata } from "next";
import { Markdown } from "@/components/Markdown";
import { Page } from "@/components/Page";
import { researchDocs, surveyNotes, TRACKS } from "@/lib/docs";
import { tracksReported } from "@/lib/progress";
import { repoLink } from "@/lib/site";

export const metadata: Metadata = {
  title: "Research",
  description: "The research documents and the survey notes, rendered from the repository.",
  alternates: { canonical: "/research" },
};

export default function Research() {
  const docs = researchDocs();
  const notes = surveyNotes();
  const reported = tracksReported();
  return (
    <Page
      current="/research"
      eyebrow="Research"
      title="The research, as written"
      lead={
        <p>
          Every page here is rendered from a Markdown file in the repository. Numbers come from the
          ledger and citations from the source list; neither is typed into the page.
        </p>
      }
    >
      <h2 id="documents">Documents</h2>
      <ul className="doc-list">
        {docs.map((d) => (
          <li key={d.file} className="card">
            <h3>
              <a href={`/research/${d.slug}`}>{d.title}</a>
            </h3>
            {d.lead && (
              <div className="muted">
                <Markdown md={d.lead} />
              </div>
            )}
            <p className="file">
              <a href={repoLink(d.file)} rel="noopener">
                {d.file}
              </a>
            </p>
          </li>
        ))}
      </ul>
      <h2 id="survey">The survey, ten tracks</h2>
      <p>
        Each track is a separate literature survey, written by a helper that opens every source
        before writing about it. The notes are raw research, kept as written; the documents above
        cite sources through the source list, not through the notes.
      </p>
      <ol className="tracks">
        {TRACKS.map(([n, slug, name]) => {
          const note = notes.find((x) => x.file.endsWith(`/${n}-${slug}.md`));
          return (
            <li key={n} className={reported.has(n) ? "reported" : "pending"}>
              <span className="code">{n}</span>{" "}
              {note ? <a href={`/notes/${note.slug}`}>{name}</a> : name}{" "}
              <span className="muted">{reported.has(n) ? "reported" : "in progress"}</span>
            </li>
          );
        })}
      </ol>
    </Page>
  );
}
