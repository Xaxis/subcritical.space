"use client";
// Y3, coupled loops, in 3D with its readout: set each loop's own gain and how strongly the loops
// feed one another, and see that loops which are each subcritical can run away together.
import { useId, useState } from "react";
import { Stage } from "@/components/three/Stage";
import { LOOPS, radiusUniform } from "@/lib/loops";

const N = LOOPS.length;

export function CoupledLoops({ cite }: { cite: { href: string; label: string }[] }) {
  const [g, setG] = useState(0.7);
  const [c, setC] = useState(0.05);
  const gid = useId();
  const cid = useId();
  const radius = radiusUniform(N, g, c);
  const alone = g < 1;
  const together = radius < 1;
  const head = together ? "Subcritical together." : "Supercritical together.";
  const body = `Each loop alone has gain ${g.toFixed(2)}, ${alone ? "below" : "at or above"} 1. Coupled, the system's gain is g + ${N - 1}c = ${radius.toFixed(2)}, so ${
    together
      ? "the loops settle at a level the human-held inputs set."
      : alone
        ? "they run away together although none would alone."
        : "they run away."
  }`;
  const label = `Five improvement loops, ${LOOPS.join(", ")}, drawn as rings with light running round them and links carrying what each feeds the others. ${head} ${body}`;
  return (
    <figure className={`figure loops3d ${together ? "is-sub" : "is-critical"}`}>
      <div className="figure-controls">
        <label htmlFor={gid}>
          Each loop&apos;s own gain <var>g</var>
        </label>
        <input
          id={gid}
          type="range"
          min={0.3}
          max={1.1}
          step={0.01}
          value={g}
          onChange={(e) => setG(Number(e.target.value))}
          aria-valuetext={`g = ${g.toFixed(2)}`}
        />
        <output htmlFor={gid} className="mono">
          {g.toFixed(2)}
        </output>
      </div>
      <div className="figure-controls">
        <label htmlFor={cid}>
          Coupling <var>c</var>
        </label>
        <input
          id={cid}
          type="range"
          min={0}
          max={0.2}
          step={0.005}
          value={c}
          onChange={(e) => setC(Number(e.target.value))}
          aria-valuetext={`c = ${c.toFixed(3)}`}
        />
        <output htmlFor={cid} className="mono">
          {c.toFixed(3)}
        </output>
      </div>
      <Stage scene="loops" param={g} param2={c} label={label} className="stage-loops" />
      <p className="loop-names">
        Clockwise from the top: {LOOPS.join(", ")}. The glow in the middle is the capability gained.
      </p>
      <figcaption>
        <strong className="state">{head}</strong> {body}{" "}
        <span className="muted">
          An illustration with every loop alike, not a measurement. The condition, a spectral radius
          of 1, is prior work (
          {cite.map((x, i) => (
            <span key={x.href}>
              {i > 0 && "; "}
              <a className="cite" href={x.href}>
                {x.label}
              </a>
            </span>
          ))}
          ). Part I measures each loop&apos;s gain and coupling.
        </span>
      </figcaption>
    </figure>
  );
}
