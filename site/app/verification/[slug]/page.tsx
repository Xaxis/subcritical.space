import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Markdown } from "@/components/Markdown";
import { Page } from "@/components/Page";
import { verificationReports } from "@/lib/docs";
import { repoLink } from "@/lib/site";

export const dynamicParams = false;

export function generateStaticParams() {
  const reports = verificationReports();
  // A static route needs one page to exist; until a level reports, the placeholder 404s.
  return reports.length > 0 ? reports.map((d) => ({ slug: d.slug })) : [{ slug: "none" }];
}

export async function generateMetadata({
  params,
}: PageProps<"/verification/[slug]">): Promise<Metadata> {
  const { slug } = await params;
  const doc = verificationReports().find((d) => d.slug === slug);
  if (!doc) return {};
  return {
    title: doc.title,
    description: `Verification report: ${doc.title}`,
    alternates: { canonical: `/verification/${slug}` },
  };
}

export default async function Report({ params }: PageProps<"/verification/[slug]">) {
  const { slug } = await params;
  const doc = verificationReports().find((d) => d.slug === slug);
  if (!doc) notFound();
  return (
    <Page
      current="/research"
      eyebrow="Verification report"
      title={doc.title}
      lead={doc.lead ? <Markdown md={doc.lead} asWritten /> : undefined}
      toc={doc.headings}
    >
      <p className="callout">
        Written by a helper that wrote none of the work it checks, and kept as written. A claim that
        fails a level is cut or downgraded in <a href="/research/claims">the claims file</a>, never
        argued around.
      </p>
      <article className="prose">
        <Markdown md={doc.body} asWritten />
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
