// The repository the site is built from: research/ and data/ are read at build time, never copied
// into the site. Server only.
import "server-only";
import { existsSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";

/** The repository root. Next builds from site/, so it is one level up. */
export const ROOT = path.resolve(process.cwd(), "..");

export function readRepoFile(file: string): string {
  return readFileSync(path.join(ROOT, file), "utf8");
}

export function repoFileExists(file: string): boolean {
  return existsSync(path.join(ROOT, file));
}

/** The Markdown files in a folder of the repository, sorted by name. */
export function markdownIn(folder: string): string[] {
  const dir = path.join(ROOT, folder);
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter((f) => f.endsWith(".md"))
    .sort()
    .map((f) => `${folder}/${f}`);
}
