// research/sources.toml, the source list every citation [@key] resolves against.
import "server-only";
import { parse } from "smol-toml";
import { readRepoFile } from "./repo";

export interface Source {
  key: string;
  type: string;
  title: string;
  authors?: string;
  year?: number;
  undated?: boolean;
  doi?: string;
  arxiv?: string;
  isbn?: string;
  url?: string;
  opened?: string;
  /** Other keys the survey tracks gave this work; a note's [@alias] still resolves to it. */
  aliases?: string[];
}

let cached: Source[] | null = null;

export function sources(): Source[] {
  if (!cached) {
    const raw = parse(readRepoFile("research/sources.toml")) as {
      source?: Record<string, Omit<Source, "key">>;
    };
    cached = Object.entries(raw.source ?? {})
      .map(([key, s]) => ({ key, ...s }))
      .sort((a, b) => a.key.localeCompare(b.key));
  }
  return cached;
}

/** Every key and alias, to the source it names. */
export function sourceIndex(): Map<string, Source> {
  const index = new Map<string, Source>();
  for (const s of sources()) {
    index.set(s.key, s);
    for (const a of s.aliases ?? []) index.set(a, s);
  }
  return index;
}

/** Where a reader can open the source: its DOI, arXiv page, URL, or a book search by ISBN. */
export function sourceHref(s: Source): string | null {
  if (s.doi) return `https://doi.org/${s.doi}`;
  if (s.arxiv) return `https://arxiv.org/abs/${s.arxiv}`;
  if (s.url) return s.url;
  if (s.isbn) return `https://openlibrary.org/isbn/${s.isbn.replace(/[^0-9Xx]/g, "")}`;
  return null;
}
