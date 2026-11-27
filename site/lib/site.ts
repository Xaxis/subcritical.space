// What the site is called and where it lives. Until subcritical.space is registered the site is
// served from its Vercel preview address; switch `url` (and nothing else) the day the domain is live.
export const SITE = {
  name: "Subcritical",
  url: "https://subcritical.vercel.app",
  domain: "subcritical.space",
  tagline: "Prevent superintelligence. Keep useful AI.",
  description:
    "An open research program on a protocol that prevents the development of artificial superintelligence while useful AI stays allowed and keeps improving: measurable definitions, the mechanisms that form superintelligence, and verification that trusts no single party.",
  repo: "https://github.com/Xaxis/subcritical.space",
  started: "2026-11-26",
};

/** The header's links, in order. */
export const NAV = [
  { href: "/research", label: "Research" },
  { href: "/experiments", label: "Experiments" },
  { href: "/numbers", label: "Numbers" },
  { href: "/sources", label: "Sources" },
] as const;

/** A file in the repository, on GitHub, at a line when given. */
export function repoLink(file: string, line?: number): string {
  return `${SITE.repo}/blob/main/${file}${line ? `#L${line}` : ""}`;
}
