import type { Metadata } from "next";
import { Page } from "@/components/Page";
import {
  type Doc,
  paperSections,
  researchDocs,
  surveyNotes,
  TRACKS,
  verificationReports,
} from "@/lib/docs";
import { tracksReported } from "@/lib/progress";
import { repoLink } from "@/lib/site";

export const metadata: Metadata = {
  title: "Research",
  description: "The research documents and the survey notes, rendered from the repository.",
  alternates: { canonical: "/research" },
};

/** A lead as plain text, for a card that is itself one link: no links, citations or marks inside. */
const plain = (md: string) =>
  md
    .replace(/\s*\[@[^\]]*\]/g, "")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/[*_`]/g, "");

const minutes = (md: string) =>
  Math.max(1, Math.round(md.split(/\s+/).filter(Boolean).length / 230));

/** Which part of the work a research file belongs to, by its number. */
const GROUPS: { id: string; title: string; gloss: string; files: RegExp }[] = [
  {
    id: "part-i",
    title: "Part I: what superintelligence is and how it forms",
    gloss:
      "The definitions, then the mechanisms that form superintelligence from five perspectives, each defined and measured, and the pathways ranked on that evidence.",
    files: /^research\/(01-|01\d-|02-)/,
  },
  {
    id: "part-ii",
    title: "Part II: the protocol",
    gloss:
      "Derived from the mechanisms: each limit, the channel that verifies it, what that channel cannot see and what it costs useful AI.",
    files: /^research\/06-/,
  },
  {
    id: "part-iii",
    title: "Part III: what holds",
    gloss:
      "What is new and what is prior work, the claims with their tests, the proofs, and the record of every claim at every level.",
    files: /^research\/0[3457]-/,
  },
  {
    id: "before",
    title: "Before the survey",
    gloss: "The memo the work started from: candidates, not findings.",
    files: /^research\/00-/,
  },
];

function DocCard({ d, href }: { d: Doc; href: string }) {
  return (
    <li className="doc-card">
      <a className="doc-card-inner" href={href}>
        <span className="doc-card-title">{d.title}</span>
        {d.lead && <span className="doc-card-lead">{plain(d.lead)}</span>}
        <span className="doc-card-meta">
          {minutes(`${d.lead} ${d.body}`)} min read <span aria-hidden="true">·</span>{" "}
          <code>{d.file}</code>
        </span>
      </a>
    </li>
  );
}

export default function Research() {
  const docs = researchDocs();
  const notes = surveyNotes();
  const reports = verificationReports();
  const spot = notes.find((x) => x.file.endsWith("/11-spot-check.md"));
  const reported = tracksReported();
  const paper = paperSections();
  const paperWords = paper.reduce((n, s) => n + s.words, 0);
  return (
    <Page
      current="/research"
      eyebrow="Research"
      title="The research, as written"
      lead={
        <p>
          Every page here is rendered from a Markdown file in the{" "}
          <a href={repoLink("research/")} rel="noopener">
            repository
          </a>
          . Numbers come from the ledger and citations from the source list; neither is typed into
          the page.
        </p>
      }
    >
      {paper.length > 0 && (
        <a className="paper-cta" href="/paper">
          <span className="exp-label">Start here</span>
          <span className="paper-cta-title">The paper</span>
          <span className="paper-cta-text">
            All of it in one read: Part I, the protocol, and what the proofs, experiments and
            verification leave standing. About {Math.round(paperWords / 1000)} thousand words.
          </span>
        </a>
      )}
      {GROUPS.map((g) => {
        const members = docs.filter((d) => g.files.test(d.file));
        if (members.length === 0) return null;
        return (
          <section key={g.id} aria-labelledby={g.id} className="doc-group">
            <h2 id={g.id}>{g.title}</h2>
            <p className="doc-group-gloss">{g.gloss}</p>
            <ul className="doc-cards">
              {members.map((d) => (
                <DocCard key={d.file} d={d} href={`/research/${d.slug}`} />
              ))}
            </ul>
          </section>
        );
      })}
      {reports.length > 0 && (
        <section aria-labelledby="verification" className="doc-group">
          <h2 id="verification">Verification reports</h2>
          <p className="doc-group-gloss">
            The levels run by helpers who wrote none of the work, each report kept as written. Each
            claimed contribution must pass six levels or be cut.
          </p>
          <ul className="doc-cards">
            {reports.map((d) => (
              <DocCard key={d.file} d={d} href={`/verification/${d.slug}`} />
            ))}
          </ul>
        </section>
      )}
      <section aria-labelledby="survey" className="doc-group">
        <h2 id="survey">The survey, ten tracks</h2>
        <p className="doc-group-gloss">
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
        {spot && (
          <p className="doc-group-gloss">
            An independent checker, who wrote none of the notes, then fetched the sources behind the
            claims each note leans on most and recorded what holds:{" "}
            <a href={`/notes/${spot.slug}`}>the spot-check</a>. The research does not rely on what
            it marks distorted.
          </p>
        )}
      </section>
    </Page>
  );
}
