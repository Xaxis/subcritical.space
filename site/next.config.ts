import path from "node:path";
import type { NextConfig } from "next";

// The repository root: the site reads research/ and data/ from it at build time, and it holds the
// workspace lockfile. Naming it stops Next from guessing in worktrees.
const repoRoot = path.join(import.meta.dirname, "..");

// Every page is static and the site takes no input, so the policy is strict about where things
// load from. Next inlines its hydration data and the theme script, which a static page cannot give
// a nonce, so scripts allow 'unsafe-inline' from this origin only.
const CSP = [
  "default-src 'self'",
  `script-src 'self' 'unsafe-inline'${process.env.NODE_ENV === "development" ? " 'unsafe-eval'" : ""}`,
  "style-src 'self' 'unsafe-inline'",
  "img-src 'self' data:",
  "font-src 'self'",
  "connect-src 'self'",
  "frame-ancestors 'none'",
  "base-uri 'self'",
  "form-action 'self'",
  "object-src 'none'",
  "upgrade-insecure-requests",
].join("; ");

const nextConfig: NextConfig = {
  poweredByHeader: false,
  reactStrictMode: true,
  turbopack: { root: repoRoot },
  outputFileTracingRoot: repoRoot,
  outputFileTracingIncludes: { "/**": ["../data/**", "../research/**"] },
  // The commit a deploy was built from, printed in every page's head (tools/site/deploy.sh checks it).
  env: { SUBCRITICAL_BUILD: process.env.SUBCRITICAL_BUILD?.trim() || "dev" },
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "Content-Security-Policy", value: CSP },
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "X-Frame-Options", value: "DENY" },
          { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
          { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains" },
        ],
      },
    ];
  },
};

export default nextConfig;
