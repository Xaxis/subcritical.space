import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Markdown } from "@/components/Markdown";
import { Page } from "@/components/Page";
import { surveyNotes } from "@/lib/docs";
import { repoLink } from "@/lib/site";

export const dynamicParams = false;

export function generateStaticParams() {
  const notes = surveyNotes();
  // A static route needs one page to exist; until a track reports, the placeholder 404s.
  return notes.length > 0 ? notes.map((d) => ({ slug: d.slug })) : [{ slug: "none" }];
}

export async function generateMetadata({ params }: PageProps<"/notes/[slug]">): Promise<Metadata> {
  const { slug } = await params;
  const doc = surveyNotes().find((d) => d.slug === slug);
  if (!doc) return {};
  return {
    title: doc.title,
    description: `Survey notes: ${doc.title}`,
    alternates: { canonical: `/notes/${slug}` },
  };
}

export default async function Note({ params }: PageProps<"/notes/[slug]">) {
  const { slug } = await params;
  const doc = surveyNotes().find((d) => d.slug === slug);
  if (!doc) notFound();
  return (
    <Page
      current="/research"
      eyebrow="Survey notes, raw"
      title={doc.title}
      lead={doc.lead ? <Markdown md={doc.lead} /> : undefined}
      toc={doc.headings}
    >
      <p className="callout">
        Raw research notes, kept as the survey helper wrote them. The research documents cite
        sources through the source list, not through these notes.
      </p>
      <article className="prose">
        <Markdown md={doc.body} />
      </article>
      <p className="file">
        Source:{" "}
        <a href={repoLink(doc.file)} rel="noopener">
          {doc.file}
        </a>
      </p>
    </Page>
  );
}
