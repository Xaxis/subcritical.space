// From corerope.space site/components/three/kit.ts, trimmed to what Subcritical's scenes use.
// The engine every 3D scene shares: one renderer per stage, bloom, a loop that runs only while the
// stage is on screen and the tab is visible, and a still mode for readers who asked for less motion.
// Scenes are plain three.js, built in code: no models, textures or images are loaded.
//
// Shaders here: a real GPU returns NaN for pow() of a negative base and for sqrt() below zero, and
// one NaN pixel spreads through the bloom pass and blacks out the whole stage (SwiftShader returns
// a number, so checks pass). Clamp every pow() and sqrt() base. The scenes use stock materials.
import * as THREE from "three";
import { EffectComposer } from "three/examples/jsm/postprocessing/EffectComposer.js";
import { OutputPass } from "three/examples/jsm/postprocessing/OutputPass.js";
import { RenderPass } from "three/examples/jsm/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/examples/jsm/postprocessing/UnrealBloomPass.js";

export { THREE };

/** What the page tells a scene: which story step it is on, and up to two free parameters. */
export type SceneState = { step: number; param: number; param2: number };

export type Frame = {
  /** Seconds since the scene started (frozen in still mode). */
  t: number;
  /** Seconds since the last frame, capped; large in still mode so eased values land at once. */
  dt: number;
  state: SceneState;
  /** The pointer over the stage, -1 to 1 on each axis, eased. */
  pointer: { x: number; y: number };
  /** How much farther the camera should stand so a scene composed for 16:10 still fits. */
  fit: number;
};

/** Pull-back for a stage narrower than the 16:10 a scene is composed for. */
export function fitFor(aspect: number, design = 1.6): number {
  return aspect >= design ? 1 : Math.min(2.2, (design / aspect) ** 0.85);
}

export type Built = {
  scene: THREE.Scene;
  camera: THREE.PerspectiveCamera;
  update(frame: Frame): void;
  resize?(width: number, height: number): void;
  dispose?(): void;
};

export type BuildContext = { width: number; height: number; small: boolean };
export type SceneModule = { build(ctx: BuildContext): Built; bloom?: Partial<Bloom> };
type Bloom = { strength: number; radius: number; threshold: number };

export type Handle = {
  set(state: Partial<SceneState>): void;
  setPlaying(playing: boolean): void;
  dispose(): void;
};

/** The stage colour, also painted by CSS behind the canvas so edges never show. */
export const STAGE = new THREE.Color("#07090c");

/** Eases `current` toward `target`: framerate-independent, `rate` per second. */
export function approach(current: number, target: number, dt: number, rate = 4): number {
  return target + (current - target) * Math.exp(-rate * dt);
}

/** A deterministic random generator, so a scene looks the same on every visit. */
export function rng(seed: number): () => number {
  let s = seed >>> 0;
  return () => {
    s = (s + 0x6d2b79f5) >>> 0;
    let t = s;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** A soft round sprite for points and glows, drawn once into a canvas. */
export function glowTexture(): THREE.Texture {
  const c = document.createElement("canvas");
  c.width = c.height = 64;
  const g = c.getContext("2d");
  if (g) {
    const r = g.createRadialGradient(32, 32, 0, 32, 32, 32);
    r.addColorStop(0, "rgba(255,255,255,1)");
    r.addColorStop(0.25, "rgba(255,255,255,0.55)");
    r.addColorStop(1, "rgba(255,255,255,0)");
    g.fillStyle = r;
    g.fillRect(0, 0, 64, 64);
  }
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}

/** Slow drifting dust, for depth. */
export function dust(count: number, spread: THREE.Vector3, seed = 7): THREE.Points {
  const r = rng(seed);
  const pos = new Float32Array(count * 3);
  for (let i = 0; i < count; i++) {
    pos[i * 3] = (r() - 0.5) * spread.x;
    pos[i * 3 + 1] = (r() - 0.5) * spread.y;
    pos[i * 3 + 2] = (r() - 0.5) * spread.z;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const mat = new THREE.PointsMaterial({
    size: 0.035,
    map: glowTexture(),
    color: new THREE.Color("#8a7d70"),
    transparent: true,
    opacity: 0.55,
    depthWrite: false,
    blending: THREE.AdditiveBlending,
  });
  return new THREE.Points(geo, mat);
}

/** A buffer attribute the scene rewrites every frame. */
export function dynamicAttribute(geo: THREE.BufferGeometry, name: string, data: Float32Array) {
  const attr = new THREE.BufferAttribute(data, 3);
  attr.setUsage(THREE.DynamicDrawUsage);
  geo.setAttribute(name, attr);
  return attr;
}

/**
 * Glowing particles the scene places each frame: call `put` for each one shown, then `flush`.
 * Colours are premultiplied by brightness (additive blending: black is invisible).
 */
export function sprites(max: number, size: number) {
  const pos = new Float32Array(max * 3);
  const col = new Float32Array(max * 3);
  const geo = new THREE.BufferGeometry();
  const posAttr = dynamicAttribute(geo, "position", pos);
  const colAttr = dynamicAttribute(geo, "color", col);
  const points = new THREE.Points(
    geo,
    new THREE.PointsMaterial({
      size,
      map: glowTexture(),
      vertexColors: true,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    }),
  );
  points.frustumCulled = false;
  let n = 0;
  return {
    points,
    put(p: THREE.Vector3, c: THREE.Color, brightness = 1) {
      if (n >= max || brightness <= 0.002) return;
      pos[n * 3] = p.x;
      pos[n * 3 + 1] = p.y;
      pos[n * 3 + 2] = p.z;
      col[n * 3] = c.r * brightness;
      col[n * 3 + 1] = c.g * brightness;
      col[n * 3 + 2] = c.b * brightness;
      n++;
    },
    flush() {
      for (let i = n; i < max; i++) col[i * 3] = col[i * 3 + 1] = col[i * 3 + 2] = 0;
      posAttr.needsUpdate = true;
      colAttr.needsUpdate = true;
      n = 0;
    },
  };
}

/**
 * A camera that eases to one view per step, sways a little, follows the pointer, and stands back
 * on a narrow stage (`fit`).
 */
export function rig(
  camera: THREE.PerspectiveCamera,
  views: { pos: THREE.Vector3; look: THREE.Vector3 }[],
  rate = 1.3,
) {
  const first = views[0] ?? { pos: new THREE.Vector3(0, 3, 7), look: new THREE.Vector3() };
  const pos = first.pos.clone();
  const look = first.look.clone();
  const back = new THREE.Vector3();
  const ease = (v: THREE.Vector3, to: THREE.Vector3, dt: number) =>
    v.set(
      approach(v.x, to.x, dt, rate),
      approach(v.y, to.y, dt, rate),
      approach(v.z, to.z, dt, rate),
    );
  return (step: number, { t, dt, pointer, fit }: Frame) => {
    const v = views[Math.max(0, Math.min(views.length - 1, step))] ?? first;
    ease(pos, v.pos, dt);
    ease(look, v.look, dt);
    // Stand back along the line of sight, so a narrow stage still frames the same thing.
    back.subVectors(pos, look).multiplyScalar(fit);
    camera.position.set(
      look.x + back.x + Math.sin(t * 0.1) * 0.3 + pointer.x * 0.5,
      look.y + back.y - pointer.y * 0.3,
      look.z + back.z,
    );
    camera.lookAt(look);
  };
}

/** Mounts a scene into `host` and runs it. Throws if WebGL is unavailable. */
export function mount(
  host: HTMLElement,
  mod: SceneModule,
  initial: SceneState,
  opts: { still: boolean; onLost?: () => void },
): Handle {
  const small = host.clientWidth < 640;
  let width = Math.max(1, host.clientWidth);
  let height = Math.max(1, host.clientHeight);
  // Built before the renderer, so a scene that throws while building never takes a context.
  const built = mod.build({ width, height, small });
  const renderer = new THREE.WebGLRenderer({
    antialias: true,
    powerPreference: "high-performance",
  });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, small ? 1.5 : 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.setClearColor(STAGE, 1);
  const canvas = renderer.domElement;
  canvas.setAttribute("aria-hidden", "true");
  canvas.style.display = "block";
  canvas.style.width = "100%";
  canvas.style.height = "100%";
  host.appendChild(canvas);

  built.scene.background = STAGE;

  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(built.scene, built.camera));
  const b: Bloom = { strength: 0.9, radius: 0.55, threshold: 0.62, ...mod.bloom };
  const bloom = new UnrealBloomPass(
    new THREE.Vector2(width / 2, height / 2),
    b.strength,
    b.radius,
    b.threshold,
  );
  composer.addPass(bloom);
  composer.addPass(new OutputPass());

  const size = () => {
    width = Math.max(1, host.clientWidth);
    height = Math.max(1, host.clientHeight);
    renderer.setSize(width, height, false);
    composer.setSize(width, height);
    bloom.resolution.set(width / 2, height / 2);
    built.camera.aspect = width / height;
    built.camera.updateProjectionMatrix();
    built.resize?.(width, height);
  };
  size();

  let state: SceneState = { ...initial };
  const pointer = { x: 0, y: 0 };
  const target = { x: 0, y: 0 };
  let t = opts.still ? 2.6 : 0;
  let last = performance.now();
  let raf = 0;
  let onScreen = false;
  let playing = !opts.still;
  let disposed = false;

  const draw = (dt: number) => {
    pointer.x = approach(pointer.x, target.x, dt, 3);
    pointer.y = approach(pointer.y, target.y, dt, 3);
    built.update({ t, dt, state, pointer, fit: fitFor(width / height) });
    composer.render();
  };
  // Still frames: settle eased values by stepping the scene a few times at a fixed time.
  const still = () => {
    for (let i = 0; i < 4; i++)
      built.update({ t, dt: 2, state, pointer, fit: fitFor(width / height) });
    composer.render();
  };
  const loop = (now: number) => {
    raf = 0;
    if (disposed || !onScreen || !playing || document.hidden) return;
    const dt = Math.min(0.05, (now - last) / 1000);
    last = now;
    t += dt;
    draw(dt);
    raf = requestAnimationFrame(loop);
  };
  const kick = () => {
    if (disposed) return;
    if (playing && onScreen && !document.hidden && !raf) {
      last = performance.now();
      raf = requestAnimationFrame(loop);
    } else if (!playing) {
      still();
    }
  };

  const io = new IntersectionObserver((entries) => {
    onScreen = entries.some((e) => e.isIntersecting);
    kick();
  });
  io.observe(host);
  const ro = new ResizeObserver(() => {
    size();
    if (!playing) still();
  });
  ro.observe(host);
  const onMove = (e: PointerEvent) => {
    const r = host.getBoundingClientRect();
    target.x = ((e.clientX - r.left) / r.width) * 2 - 1;
    target.y = ((e.clientY - r.top) / r.height) * 2 - 1;
  };
  const onLeave = () => {
    target.x = 0;
    target.y = 0;
  };
  host.addEventListener("pointermove", onMove);
  host.addEventListener("pointerleave", onLeave);
  const onVis = () => kick();
  document.addEventListener("visibilitychange", onVis);
  canvas.addEventListener("webglcontextlost", (e) => {
    e.preventDefault();
    // Our own dispose releases the context on purpose; only a loss the browser forced is a failure.
    if (!disposed) opts.onLost?.();
  });

  const handle: Handle = {
    set(next) {
      state = { ...state, ...next };
      if (!playing) still();
    },
    setPlaying(p) {
      playing = p;
      kick();
    },
    dispose() {
      disposed = true;
      if (raf) cancelAnimationFrame(raf);
      io.disconnect();
      ro.disconnect();
      host.removeEventListener("pointermove", onMove);
      host.removeEventListener("pointerleave", onLeave);
      document.removeEventListener("visibilitychange", onVis);
      built.dispose?.();
      built.scene.traverse((o) => {
        const m = o as THREE.Mesh;
        m.geometry?.dispose();
        const mats = Array.isArray(m.material) ? m.material : m.material ? [m.material] : [];
        for (const x of mats) {
          for (const v of Object.values(x)) if (v instanceof THREE.Texture) v.dispose();
          x.dispose();
        }
      });
      composer.dispose();
      renderer.dispose();
      // Give the context back now, not at garbage collection: browsers cap live contexts (about 16)
      // and drop the oldest when a page holds more.
      renderer.forceContextLoss();
      canvas.remove();
    },
  };
  // The first frame runs the scene's update; if that throws, give everything back before failing.
  try {
    still();
  } catch (e) {
    handle.dispose();
    throw e;
  }
  return handle;
}
