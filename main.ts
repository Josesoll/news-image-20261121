// Entry program for the 21 November 2026 front page.
//
// The picture itself is finished work: it sits in this repository as
// entry.png, next to this file. All this program has to do is deliver
// those exact bytes to the place the grader looks for them. It does
// no drawing, no downloading and no deciding — copying a finished
// file is what keeps every run byte-for-byte the same.
//
// Where the copy lands:
//   - MAKEFUN_OUTPUT_DIR, when the caller sets it (local test runs)
//   - /output otherwise (the grader's container)
// The destination folder is created first, so a bare environment
// with no /output yet is not a problem.

import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const sourceFile = resolve(repoRoot, "entry.png");

const targetFolder = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const targetFile = resolve(targetFolder, "entry.png");

const pictureBytes = await readFile(sourceFile);

await mkdir(targetFolder, { recursive: true });
await writeFile(targetFile, pictureBytes);
