// From corerope.space tools/lib/chromium.ts (itself from paperwright.diy).
// How every browser run here launches Chromium: on SwiftShader, never the box's GPU, which other
// projects' renders hold (CLAUDE.md, "Share the box").
export const CHROMIUM_ARGS = ["--use-angle=swiftshader", "--disable-gpu-watchdog"];
