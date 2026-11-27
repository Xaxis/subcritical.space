import { NAV, SITE } from "@/lib/site";
import { Logo } from "./Logo";
import { ThemeToggle } from "./ThemeToggle";

export function Header({ current }: { current?: string }) {
  return (
    <header className="site-header">
      <div className="wrap header-row">
        <a className="brand" href="/" aria-label={`${SITE.name}, home`}>
          <Logo />
          <span>{SITE.name}</span>
        </a>
        <nav aria-label="Site">
          {NAV.map((n) => (
            <a key={n.href} href={n.href} aria-current={current === n.href ? "page" : undefined}>
              {n.label}
            </a>
          ))}
        </nav>
        <ThemeToggle />
      </div>
    </header>
  );
}
