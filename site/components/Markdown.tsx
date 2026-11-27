// Research Markdown as a page. Ledger links show the model's value (never the text typed in the
// file), citations link to the source list, and links between research files go to their pages.
import type { ReactNode } from "react";
import ReactMarkdown, { type Components } from "react-markdown";
import remarkGfm from "remark-gfm";
import { entry, ledger } from "@/lib/ledger";
import { sourceIndex } from "@/lib/sources";
import { citeLabel, docHref, ledgerId, linkCitations, slugify } from "@/lib/text";

/** A number from the ledger, linked to its entry; its basis shows in its style and its title. */
export function Num({ id }: { id: string }) {
  const e = entry(id);
  return (
    <a
      className={`num basis-${e.basis}`}
      href={`/numbers#${id}`}
      title={`${e.label} (${e.basis}${e.basis === "assumption" ? ", not yet sourced" : ""})`}
    >
      {e.display}
    </a>
  );
}

function text(children: ReactNode): string {
  if (typeof children === "string" || typeof children === "number") return String(children);
  if (Array.isArray(children)) return children.map(text).join("");
  if (children && typeof children === "object" && "props" in children)
    return text((children as { props: { children?: ReactNode } }).props.children);
  return "";
}

function components(inline: boolean, asWritten: boolean): Components {
  return {
    a({ href = "", children }) {
      const id = ledgerId(href);
      if (id && asWritten) {
        const now = ledger()[id];
        if (!now)
          return (
            <span
              className="num as-written"
              title="As written; the ledger no longer has this number"
            >
              {children}
            </span>
          );
        return (
          <a
            className="num as-written"
            href={`/numbers#${id}`}
            title={`As written when this level ran. The ledger now shows ${now.display}.`}
          >
            {children}
          </a>
        );
      }
      if (id && ledger()[id]) return <Num id={id} />;
      const doc = docHref(href);
      if (doc) return <a href={doc}>{children}</a>;
      if (href.startsWith("/sources#"))
        return (
          <a className={text(children).length > 28 ? "cite cite-long" : "cite"} href={href}>
            {children}
          </a>
        );
      if (/^https?:/.test(href))
        return (
          <a href={href} rel="noopener">
            {children}
          </a>
        );
      return <a href={href}>{children}</a>;
    },
    h2: ({ children }) => <h2 id={slugify(text(children))}>{children}</h2>,
    h3: ({ children }) => <h3 id={slugify(text(children))}>{children}</h3>,
    pre: ({ children }) => (
      // biome-ignore lint/a11y/noNoninteractiveTabindex: a wide code block scrolls, and a keyboard must reach it
      <pre tabIndex={0}>{children}</pre>
    ),
    table: ({ children }) => (
      // biome-ignore lint/a11y/noNoninteractiveTabindex: a wide table scrolls, and a keyboard must reach it
      <div className="table-wrap" tabIndex={0}>
        <table>{children}</table>
      </div>
    ),
    ...(inline ? { p: ({ children }) => <>{children}</> } : {}),
  };
}

/**
 * Research Markdown. `asWritten` is for records (the verification reports): their ledger links keep
 * the value written when the level ran, and say what the ledger shows now.
 */
export function Markdown({
  md,
  inline = false,
  asWritten = false,
}: {
  md: string;
  inline?: boolean;
  asWritten?: boolean;
}) {
  const byKey = sourceIndex();
  const withCites = linkCitations(
    md,
    (k) => citeLabel(byKey.get(k), k),
    (k) => byKey.get(k)?.key ?? k,
  );
  return (
    <ReactMarkdown remarkPlugins={[remarkGfm]} components={components(inline, asWritten)}>
      {withCites}
    </ReactMarkdown>
  );
}
