import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const projectRoot = path.resolve(__dirname, "..");
const clientDir = path.join(projectRoot, "dist", "client");
const assetsDir = path.join(clientDir, "assets");

const MAIN_ENTRY_PREFIX = "index-";
const CSS_ENTRY_PREFIX = "styles-";

let mainJs = "";
let mainCss = "";

if (fs.existsSync(assetsDir)) {
  const files = fs.readdirSync(assetsDir);
  for (const f of files) {
    if (f.startsWith(MAIN_ENTRY_PREFIX) && f.endsWith(".js") && !mainJs) mainJs = f;
    if (f.startsWith(CSS_ENTRY_PREFIX) && f.endsWith(".css") && !mainCss) mainCss = f;
  }
}

if (!mainJs) {
  console.error("Could not find main JS entry in dist/client/assets/");
  process.exit(1);
}

const cssLink = mainCss ? `    <link rel="stylesheet" href="/assets/${mainCss}" />` : "";

const html = `<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="robots" content="index,follow" />
    <meta name="theme-color" content="#0A0A0A" />
    <title>Kora Lab | Africa's Sovereign AI Lab</title>
${cssLink}
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/assets/${mainJs}"></script>
  </body>
</html>
`;

const outPath = path.join(clientDir, "index.html");

if (fs.existsSync(outPath)) {
  console.log(`ℹ SPA fallback skipped — ${outPath} already exists (prerendered)`);
} else {
  fs.writeFileSync(outPath, html, "utf-8");
  console.log(`✅ SPA fallback HTML generated: ${outPath} (entry: ${mainJs})`);
}
