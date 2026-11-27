import type { ReactNode } from "react";
import { Footer } from "./Footer";
import { Header } from "./Header";

/** An inner page: the header with this page marked, a title block, the content, the footer. */
export function Page(p: {
  current?: string;
  eyebrow?: string;
  title: string;
  lead?: ReactNode;
  children: ReactNode;
  toc?: { id: string; text: string }[];
}) {
  return (
    <>
      <Header current={p.current} />
      <main id="main">
        <div className="wrap page-head">
          {p.eyebrow && <p className="eyebrow">{p.eyebrow}</p>}
          <h1>{p.title}</h1>
          {p.lead && <div className="lead">{p.lead}</div>}
        </div>
        <div className={`wrap page-body${p.toc && p.toc.length > 1 ? " with-toc" : ""}`}>
          {p.toc && p.toc.length > 1 && (
            <nav className="toc" aria-label="On this page">
              <p className="toc-title">On this page</p>
              <ol>
                {p.toc.map((h) => (
                  <li key={h.id}>
                    <a href={`#${h.id}`}>{h.text}</a>
                  </li>
                ))}
              </ol>
            </nav>
          )}
          <div className="page-main">{p.children}</div>
        </div>
      </main>
      <Footer />
    </>
  );
}
