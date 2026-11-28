import { NAV, repoLink, SITE } from "@/lib/site";
import { Logo } from "./Logo";

export function Footer() {
  const build = process.env.SUBCRITICAL_BUILD ?? "dev";
  return (
    <footer className="site-footer">
      <div className="wrap footer-row">
        <div>
          <p className="footer-brand">
            <Logo />
            {SITE.name}
          </p>
          <p>
            A design, begun {SITE.started}. Nothing in it has been deployed or tested against a real
            adversary.
          </p>
          <p>
            Text and data{" "}
            <a href={repoLink("LICENSE-CC-BY-4.0")} rel="noopener">
              CC BY 4.0
            </a>
            , code{" "}
            <a href={repoLink("LICENSE")} rel="noopener">
              MIT
            </a>
            . Every number is computed in the open repository and reruns from it. Build{" "}
            <code>{build}</code>.
          </p>
        </div>
        <nav aria-label="Footer">
          <ul className="footer-nav">
            <li>
              <a href="/">Home</a>
            </li>
            {NAV.map((n) => (
              <li key={n.href}>
                <a href={n.href}>{n.label}</a>
              </li>
            ))}
            <li>
              <a href="/#findings">What the tests found</a>
            </li>
            <li>
              <a href={SITE.repo} rel="noopener">
                Repository
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </footer>
  );
}
