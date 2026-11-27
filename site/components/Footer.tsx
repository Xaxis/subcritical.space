import { repoLink, SITE } from "@/lib/site";

export function Footer() {
  const build = process.env.SUBCRITICAL_BUILD ?? "dev";
  return (
    <footer className="site-footer">
      <div className="wrap footer-row">
        <p>
          {SITE.name} is a design, begun {SITE.started}. Nothing in it has been deployed or tested
          against a real adversary.
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
          . Every number is computed in the{" "}
          <a href={SITE.repo} rel="noopener">
            open repository
          </a>{" "}
          and reruns from it. Build <code>{build}</code>.
        </p>
      </div>
    </footer>
  );
}
