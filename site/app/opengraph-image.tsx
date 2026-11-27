import { ImageResponse } from "next/og";
import { GENERATIONS } from "@/components/Logo";
import { SITE } from "@/lib/site";

export const alt = `${SITE.name}: ${SITE.tagline}`;
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export const dynamic = "force-static";

const FILLS = ["#6cb6ff", "#4a94e6", "#2f6cb5"];

export default function OpenGraphImage() {
  return new ImageResponse(
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        background: "#0a0d12",
        color: "#e8ecf2",
        padding: "64px 72px",
        fontFamily: "sans-serif",
      }}
    >
      <div
        style={{ display: "flex", alignItems: "center", gap: 18, fontSize: 32, fontWeight: 700 }}
      >
        {/* biome-ignore lint/a11y/noSvgWithoutTitle: drawn into a PNG, never part of a page */}
        <svg width="52" height="52" viewBox="0 0 32 32">
          {GENERATIONS.map((g, i) => (
            <circle key={g.cx} cx={g.cx} cy="16" r={g.r} fill={FILLS[i]} />
          ))}
        </svg>
        {SITE.name}
      </div>
      <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            fontSize: 76,
            fontWeight: 700,
            lineHeight: 1.05,
            letterSpacing: "-0.03em",
          }}
        >
          <div>Prevent superintelligence.</div>
          <div style={{ color: "#6cb6ff" }}>Keep useful AI.</div>
        </div>
        <div style={{ display: "flex", fontSize: 28, color: "#a7b0bd", maxWidth: 980 }}>
          Measurable definitions, the mechanisms that form superintelligence, and verification that
          trusts no single party.
        </div>
      </div>
      <div
        style={{ display: "flex", justifyContent: "space-between", fontSize: 24, color: "#a7b0bd" }}
      >
        <div style={{ display: "flex" }}>An open research program. A design, not yet tested.</div>
        <div style={{ display: "flex", color: "#6cb6ff", fontWeight: 600 }}>{SITE.domain}</div>
      </div>
    </div>,
    size,
  );
}
