// Serves the production build like Cloudflare Pages does (SPA fallback), but takes /content/
// from the e2e fixtures so tests never depend on the real game data.
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';

const APP = new URL('../dist/web/browser/', import.meta.url).pathname;
const CONTENT = new URL('./.content/', import.meta.url).pathname;
const PORT = Number(process.env.PORT ?? 4310);
const TYPES = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.webmanifest': 'application/manifest+json', '.svg': 'image/svg+xml', '.png': 'image/png',
};

async function resolve(pathname) {
  const [root, rel] = pathname.startsWith('/content/') ? [CONTENT, pathname.slice('/content/'.length)] : [APP, pathname];
  const file = normalize(join(root, rel));
  if (!file.startsWith(root)) return null;
  try {
    if ((await stat(file)).isFile()) return file;
  } catch {}
  return extname(pathname) ? null : join(APP, 'index.html');
}

createServer(async (req, res) => {
  const file = await resolve(decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!file) return res.writeHead(404).end();
  res.writeHead(200, { 'content-type': TYPES[extname(file)] ?? 'application/octet-stream', 'cache-control': 'no-cache' });
  res.end(await readFile(file));
}).listen(PORT, '127.0.0.1', () => console.log(`e2e server on http://127.0.0.1:${PORT}`));
