// The memo (research/00-memo.md) read as structure, so the home page shows the memo's own words
// and cannot drift from it: the organising idea, the mechanisms by perspective, the candidate
// definitions, the pathway ranking and the protocol's shape. Pure: the tests run it on the file.

export interface Mechanism {
  code: string;
  title: string;
  /** Markdown. */
  text: string;
}
export interface Perspective {
  name: string;
  mechanisms: Mechanism[];
}
export interface Definition {
  code: string;
  title: string;
  text: string;
}
export interface Plank {
  title: string;
  text: string;
}
export interface Memo {
  written: string;
  idea: string;
  perspectives: Perspective[];
  definitions: Definition[];
  pathways: { header: string[]; rows: string[][]; reasons: string };
  protocol: Plank[];
  strongest: string;
}

/** The body of the `## ` section whose heading starts with `start`. */
function section(text: string, start: string): string {
  const lines = text.split("\n");
  const at = lines.findIndex((l) => l.startsWith(`## ${start}`));
  if (at < 0) throw new Error(`the memo has no section "## ${start}"`);
  const rest = lines.slice(at + 1);
  const end = rest.findIndex((l) => l.startsWith("## "));
  return (end < 0 ? rest : rest.slice(0, end)).join("\n").trim();
}

function paragraphs(body: string): string[] {
  return body
    .split(/\n\s*\n/)
    .map((p) => p.replace(/\n\s*/g, " ").trim())
    .filter(Boolean);
}

/** List items, each with its continuation lines joined. */
function items(body: string): string[] {
  const out: string[] = [];
  for (const line of body.split("\n")) {
    if (/^\s*- /.test(line)) out.push(line.replace(/^\s*- /, "").trim());
    else if (/^\s{2,}\S/.test(line) && out.length > 0)
      out[out.length - 1] = `${out[out.length - 1]} ${line.trim()}`;
  }
  return out;
}

export function parseMemo(text: string): Memo {
  const written = /Written (\d{4}-\d{2}-\d{2})/.exec(text)?.[1] ?? "";
  const idea = paragraphs(section(text, "The organising idea")).join("\n\n");

  const perspectives: Perspective[] = [];
  for (const block of section(text, "The anatomy").split(/\n(?=\*\*[^*]+\.\*\*\s*\n)/)) {
    const head = /^\*\*([^*]+)\.\*\*\s*\n/.exec(block);
    if (!head) continue;
    const mechanisms = items(block.slice(head[0].length)).map((it) => {
      const m = /^\*([A-Z]\d) ([^*]+?)\.?\*\s*(.*)$/.exec(it);
      if (!m) throw new Error(`a mechanism the memo does not name like "*P1 Title.*": ${it}`);
      return {
        code: m[1] as string,
        title: (m[2] as string).replace(/:$/, ""),
        text: m[3] as string,
      };
    });
    perspectives.push({ name: head[1] as string, mechanisms });
  }

  const definitions = paragraphs(section(text, "Candidate definitions")).flatMap((p) => {
    const m = /^\*\*(D\d)\. ([^*]+?)\.\*\* (.*)$/.exec(p);
    return m ? [{ code: m[1] as string, title: m[2] as string, text: m[3] as string }] : [];
  });

  const pathwaysBody = section(text, "The five candidate pathways");
  const tableLines = pathwaysBody.split("\n").filter((l) => l.startsWith("|"));
  const cells = (l: string) =>
    l
      .replace(/^\||\|$/g, "")
      .split("|")
      .map((c) => c.trim());
  const header = cells(tableLines[0] ?? "");
  const rows = tableLines.slice(2).map(cells);
  const reasons = paragraphs(
    pathwaysBody
      .split("\n")
      .filter((l) => !l.startsWith("|"))
      .join("\n"),
  ).join("\n\n");

  const protocol = items(section(text, "The protocol's shape")).map((it) => {
    const m = /^\*\*([^*]+?)\.\*\* (.*)$/.exec(it);
    if (!m) throw new Error(`a protocol plank the memo does not name like "**Title.**": ${it}`);
    return { title: m[1] as string, text: m[2] as string };
  });

  const strongest = section(text, "What looks strongest now");

  return {
    written,
    idea,
    perspectives,
    definitions,
    pathways: { header, rows, reasons },
    protocol,
    strongest,
  };
}
