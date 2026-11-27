import { ImageResponse } from "next/og";
import { GENERATIONS } from "@/components/Logo";

// The home-screen icon: iOS does not use SVG icons, so the mark is drawn into a PNG.
export const size = { width: 180, height: 180 };
export const contentType = "image/png";
export const dynamic = "force-static";

const FILLS = ["#1d5fbf", "#3b82d6", "#7fb2ea"];

export default function AppleIcon() {
  return new ImageResponse(
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "#f6f4ef",
      }}
    >
      {/* biome-ignore lint/a11y/noSvgWithoutTitle: drawn into a PNG, never part of a page */}
      <svg width="140" height="140" viewBox="0 0 32 32">
        {GENERATIONS.map((g, i) => (
          <circle key={g.cx} cx={g.cx} cy="16" r={g.r} fill={FILLS[i]} />
        ))}
      </svg>
    </div>,
    size,
  );
}
