// Y3 as a live model: five improvement loops (software, hardware, economic, experiential,
// acquisitive) on a ring, each with light running around it as bright as its level, and links
// between every pair carrying what one loop feeds another. The page sets each loop's own gain g
// (param) and the coupling c (param2). The levels follow x' = G x + u from lib/loops.ts, one round
// every ROUND seconds: below a spectral radius of 1 they settle, blue; at 1 and above they run to
// the cap, amber, even when every loop's own gain is under 1. An illustration, not a measurement.
import { LOOPS, radiusUniform, step, uniformCoupling } from "@/lib/loops";
import { type BuildContext, type Built, dust, type Frame, rig, sprites, THREE } from "../kit";

const N = LOOPS.length;
const R = 2.35; // ring of loops
const r = 0.62; // each loop's radius
const ROUND = 0.45; // seconds per round
const DRIVE = 0.12; // the steady input human-held resources give each loop each round
const CAP = 8; // a runaway is drawn up to here
const PER_LOOP = 6; // pulses running around each loop

const SUB = new THREE.Color("#79b6f4");
const SUPER = new THREE.Color("#f0a35e");
const DIM = new THREE.Color("#1c2633");

/** How bright a level looks: rises fast, saturates, never exceeds 1. */
const shown = (x: number) => 1 - Math.exp(-x / 0.75);

export function build({ small }: BuildContext): Built {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(small ? 48 : 40, 1.6, 0.1, 100);
  // Step 0 frames the figure's wide stage; step 1 stands closer, for the hero's squarer stage.
  const view = rig(camera, [
    { pos: new THREE.Vector3(0, 4.6, 6.4), look: new THREE.Vector3(0, -0.2, 0) },
    { pos: new THREE.Vector3(0, 3.7, 5.1), look: new THREE.Vector3(0, -0.2, 0) },
  ]);

  const centres = LOOPS.map((_, i) => {
    const a = (i / N) * Math.PI * 2 - Math.PI / 2;
    return new THREE.Vector3(Math.cos(a) * R, 0, Math.sin(a) * R);
  });

  // The loops: flat rings whose colour warms with their level.
  const ringMats = centres.map(() => new THREE.MeshBasicMaterial({ color: DIM.clone() }));
  centres.forEach((c, i) => {
    const ring = new THREE.Mesh(new THREE.TorusGeometry(r, 0.022, 10, 96), ringMats[i]);
    ring.rotation.x = -Math.PI / 2;
    ring.position.copy(c);
    scene.add(ring);
  });

  // The couplings: a curve between every pair, rising over the middle.
  const links: { from: number; to: number; curve: THREE.QuadraticBezierCurve3 }[] = [];
  const linkMat = new THREE.LineBasicMaterial({
    color: DIM.clone(),
    transparent: true,
    opacity: 0.6,
  });
  for (let i = 0; i < N; i++)
    for (let j = i + 1; j < N; j++) {
      const a = centres[i] as THREE.Vector3;
      const b = centres[j] as THREE.Vector3;
      const mid = a.clone().add(b).multiplyScalar(0.25).setY(0.9);
      const curve = new THREE.QuadraticBezierCurve3(a, mid, b);
      links.push({ from: i, to: j, curve });
      const geo = new THREE.BufferGeometry().setFromPoints(curve.getPoints(48));
      scene.add(new THREE.Line(geo, linkMat));
    }

  const pulses = sprites(N * PER_LOOP + links.length * 2, small ? 0.34 : 0.3);
  const core = sprites(1, small ? 3.2 : 2.8);
  scene.add(pulses.points, core.points, dust(small ? 160 : 320, new THREE.Vector3(14, 6, 12), 11));

  // The model's state: each loop's level, stepped once a round, and the eased level drawn.
  let levels = new Array<number>(N).fill(DRIVE);
  const drawn = new Array<number>(N).fill(0);
  let clock = 0;
  const p = new THREE.Vector3();
  const colour = new THREE.Color();

  return {
    scene,
    camera,
    update(frame: Frame) {
      const { t, dt, state } = frame;
      const g = state.param;
      const c = state.param2;
      const radius = radiusUniform(N, g, c);
      const G = uniformCoupling(N, g, c);
      clock += dt;
      while (clock >= ROUND) {
        clock -= ROUND;
        levels = step(levels, G, DRIVE, CAP);
      }
      const runaway = radius >= 1;
      colour.copy(runaway ? SUPER : SUB);

      for (let i = 0; i < N; i++) {
        drawn[i] =
          (drawn[i] ?? 0) + (shown(levels[i] ?? 0) - (drawn[i] ?? 0)) * Math.min(1, dt * 3);
        const lit = drawn[i] ?? 0;
        (ringMats[i] as THREE.MeshBasicMaterial).color.copy(DIM).lerp(colour, 0.25 + 0.6 * lit);
        const centre = centres[i] as THREE.Vector3;
        for (let k = 0; k < PER_LOOP; k++) {
          const a = t * (0.9 + 0.12 * i) + (k / PER_LOOP) * Math.PI * 2;
          p.set(centre.x + Math.cos(a) * r, 0.02, centre.z + Math.sin(a) * r);
          pulses.put(p, colour, 0.25 + 1.4 * lit);
        }
      }
      // What each loop feeds another travels both ways along the link, as bright as c times the
      // sender's level.
      links.forEach((l, k) => {
        const u = (t * 0.32 + k * 0.137) % 1;
        l.curve.getPoint(u, p);
        pulses.put(p, colour, Math.min(1.6, c * 9 * (drawn[l.from] ?? 0)));
        l.curve.getPoint(1 - u, p);
        pulses.put(p, colour, Math.min(1.6, c * 9 * (drawn[l.to] ?? 0)));
      });
      pulses.flush();

      const mean = drawn.reduce((s, x) => s + x, 0) / N;
      core.put(p.set(0, 0.35, 0), colour, 0.15 + 1.25 * mean);
      core.flush();
      linkMat.color.copy(DIM).lerp(colour, Math.min(0.7, c * 3));
      view(state.step, frame);
    },
  };
}

export const bloom = { strength: 0.85, radius: 0.5, threshold: 0.55 };
