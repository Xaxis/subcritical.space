import type { Metadata } from "next";
import { Markdown } from "@/components/Markdown";
import { Page } from "@/components/Page";
import { paperSections, verificationReports } from "@/lib/docs";
import { repoLink } from "@/lib/site";

export const metadata: Metadata = {
  title: "The paper",
  description:
    "The research written up as one paper: what superintelligence is and how it forms, the protocol derived from it, and what the proofs, experiments and verification leave standing.",
  alternates: { canonical: "/paper" },
};

const minutes = (words: number) => Math.max(1, Math.round(words / 230));
/** Under two hours in tens of minutes, past it in hours: never "1 hours". */
const reading = (m: number) =>
  m < 120 ? `about ${Math.round(m / 10) * 10} minutes` : `about ${Math.round(m / 60)} hours`;

export default function Paper() {
  const sections = paperSections();
  const words = sections.reduce((n, s) => n + s.words, 0);
  const review = verificationReports().find((d) => /\/l6-[^/]*\.md$/.test(d.file));
  return (
    <Page
      current="/paper"
      eyebrow="A draft"
      title="The paper"
      lead={
        <>
          <p>
            The research written up as one paper, about {Math.round(words / 1000)} thousand words,
            or {reading(minutes(words))} of reading. Numbers link to the ledger and citations to the
            sources, as everywhere on the site.
          </p>
          <p className="callout">
            A draft. It has not yet been through Paperwright&apos;s integrity, reviewer and editor
            desks
            {review ? (
              <>
                . A fresh reviewer read the previous draft, and this one is revised for{" "}
                <a href={`/verification/${review.slug}`}>their report</a>; no second fresh reviewer
                has read it yet.
              </>
            ) : (
              " or a fresh reviewer."
            )}{" "}
            The protocol it describes has never been deployed or tested against a real adversary.
          </p>
        </>
      }
      toc={sections.map((s) => ({ id: s.id, text: s.title }))}
    >
      <article className="prose paper">
        {sections.map((s, i) => (
          <section key={s.id} aria-labelledby={s.id}>
            {(i === 0 || sections[i - 1]?.part !== s.part) && (
              <p className="paper-part">{s.part}</p>
            )}
            <h2 id={s.id}>{s.title}</h2>
            <Markdown md={s.body} shift={1} idPrefix={`${s.id}-`} />
          </section>
        ))}
      </article>
      <p className="file">
        Source:{" "}
        <a href={repoLink("paper/")} rel="noopener">
          paper/
        </a>
        , one file per section; <code>make paper</code> flattens it for Paperwright.
      </p>
    </Page>
  );
}
