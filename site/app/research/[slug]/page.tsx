import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Markdown } from "@/components/Markdown";
import { Page } from "@/components/Page";
import { researchDocs } from "@/lib/docs";
import { repoLink } from "@/lib/site";

export const dynamicParams = false;

export function generateStaticParams() {
  return researchDocs().map((d) => ({ slug: d.slug }));
}

export async function generateMetadata({
  params,
}: PageProps<"/research/[slug]">): Promise<Metadata> {
  const { slug } = await params;
  const doc = researchDocs().find((d) => d.slug === slug);
  if (!doc) return {};
  return {
    title: doc.title,
    description: doc.lead.replace(/[*_`[\]]|\([^)]*\)/g, "").slice(0, 200),
    alternates: { canonical: `/research/${slug}` },
  };
}

export default async function ResearchDoc({ params }: PageProps<"/research/[slug]">) {
  const { slug } = await params;
  const doc = researchDocs().find((d) => d.slug === slug);
  if (!doc) notFound();
  return (
    <Page
      current="/research"
      eyebrow="Research"
      title={doc.title}
      lead={doc.lead ? <Markdown md={doc.lead} /> : undefined}
      toc={doc.headings}
    >
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
