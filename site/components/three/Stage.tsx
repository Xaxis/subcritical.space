"use client";

// From corerope.space site/components/three/Stage.tsx. A dark stage that runs one 3D scene. three.js and the scene load only when the stage nears the
// screen, and the scene is released again when it is far away; it pauses off screen and in a
// hidden tab; a reader can pause it (WCAG 2.2.2), and one who asked for less motion gets a still
// frame. Without WebGL the stage says in words what the scene would show.
import { type ReactNode, useEffect, useRef, useState } from "react";
import type { Handle } from "./kit";

const LOADERS = {
  loops: () => import("./scenes/loops"),
} as const;
export type SceneName = keyof typeof LOADERS;

export function Stage({
  scene,
  step = 0,
  param = 0,
  param2 = 0,
  label,
  className,
  children,
}: {
  scene: SceneName;
  step?: number;
  param?: number;
  param2?: number;
  /** What the scene shows, for screen readers, and in words where WebGL is missing. */
  label: string;
  className?: string;
  /** HTML laid over the scene: captions, readouts, controls. */
  children?: ReactNode;
}) {
  const host = useRef<HTMLDivElement>(null);
  const handle = useRef<Handle | null>(null);
  const live = useRef({ step, param, param2 });
  live.current = { step, param, param2 };
  const [status, setStatus] = useState<"idle" | "ready" | "failed">("idle");
  const [reduced, setReduced] = useState(false);
  const [playing, setPlaying] = useState(true);
  // Read when a released stage is rebuilt, so a reader's pause survives scrolling away and back.
  const playingNow = useRef(playing);
  playingNow.current = playing;

  useEffect(() => {
    const el = host.current;
    if (!el) return;
    const still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    setReduced(still);
    // A page can hold many stages; only the ones near the screen keep a WebGL context. A stage
    // starts within 400px of the screen and is released beyond 1600px, so scrolling to and fro
    // near one does not rebuild it.
    let cancelled = false;
    let failed = false;
    let wanted = false;
    let loading = false;
    const fail = () => {
      failed = true;
      handle.current?.dispose();
      handle.current = null;
      if (!cancelled) setStatus("failed");
    };
    const start = () => {
      wanted = true;
      if (handle.current || loading || failed) return;
      loading = true;
      Promise.all([import("./kit"), LOADERS[scene]()])
        .then(([kit, mod]) => {
          loading = false;
          if (cancelled || !wanted || handle.current) return;
          // mount throws without WebGL. (A probe canvas here once leaked a context per stage.)
          handle.current = kit.mount(el, mod, live.current, { still, onLost: fail });
          if (!still && !playingNow.current) handle.current.setPlaying(false);
          setStatus("ready");
        })
        .catch((e: unknown) => {
          console.error(`stage "${scene}" failed to start:`, e);
          fail();
        });
    };
    const stop = () => {
      wanted = false;
      if (!handle.current) return;
      handle.current.dispose();
      handle.current = null;
      if (!cancelled && !failed) setStatus("idle");
    };
    const near = new IntersectionObserver(
      (entries) => {
        if (entries.some((e) => e.isIntersecting)) start();
      },
      { rootMargin: "400px 0px" },
    );
    const far = new IntersectionObserver(
      (entries) => {
        if (entries.every((e) => !e.isIntersecting)) stop();
      },
      { rootMargin: "1600px 0px" },
    );
    near.observe(el);
    far.observe(el);
    return () => {
      cancelled = true;
      near.disconnect();
      far.disconnect();
      handle.current?.dispose();
      handle.current = null;
      // A new scene starts from nothing: no canvas yet, so no "ready" and no pause button.
      setStatus("idle");
    };
  }, [scene]);

  useEffect(() => {
    handle.current?.set({ step, param, param2 });
  }, [step, param, param2]);

  useEffect(() => {
    handle.current?.setPlaying(playing && !reduced);
  }, [playing, reduced]);

  return (
    <div
      className={`stage${className ? ` ${className}` : ""}`}
      data-status={status}
      data-scene={scene}
    >
      <div className="stage-gl" ref={host} role="img" aria-label={label} />
      {status === "failed" && (
        <div className="stage-fallback">
          <p>{label}</p>
        </div>
      )}
      {children}
      {status === "ready" && !reduced && (
        <button
          type="button"
          className="stage-pause"
          aria-pressed={!playing}
          onClick={() => setPlaying((p) => !p)}
        >
          {/* One name, with the state in aria-pressed: a name that also flipped was read as
              "Play the animation, pressed". */}
          <span aria-hidden="true">{playing ? "❚❚" : "▶"}</span>
          <span className="visually-hidden">Pause the animation</span>
        </button>
      )}
    </div>
  );
}
