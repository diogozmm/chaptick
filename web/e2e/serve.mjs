// Serves the production build like Cloudflare Pages does (SPA fallback), but takes /content/
// from the e2e fixtures so tests never depend on the real game data.
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';

const APP = new URL('../dist/web/browser/', import.meta.url).pathname;
const CONTENT = new URL('./.content/', import.meta.url).pathname;
const PORT = Number(process.env.PORT ?? 4310);
const updateTest = process.env.CONTENT_UPDATE_TEST === '1';
let deployment = 'before';
const TYPES = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.webmanifest': 'application/manifest+json', '.svg': 'image/svg+xml', '.png': 'image/png',
};

async function resolve(pathname) {
  const contentRoot = updateTest ? join(CONTENT, 'update', deployment) + '/' : CONTENT;
  const [root, rel] = pathname.startsWith('/content/') ? [contentRoot, pathname.slice('/content/'.length)] : [APP, pathname];
  const file = normalize(join(root, rel));
  if (!file.startsWith(root)) return null;
  try {
    if ((await stat(file)).isFile()) return file;
  } catch {}
  return extname(pathname) ? null : join(APP, 'index.html');
}

createServer(async (req, res) => {
  // Only the isolated update-test server exposes deployment switching; never shipped to the app.
  if (updateTest && req.method === 'POST' && req.url === '/__test/deploy-after') {
    deployment = 'after';
    return res.writeHead(204).end();
  }
  const file = await resolve(decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!file) return res.writeHead(404).end();
  res.writeHead(200, { 'content-type': TYPES[extname(file)] ?? 'application/octet-stream', 'cache-control': 'no-cache' });
  res.end(await readFile(file));
}).listen(PORT, '127.0.0.1', () => console.log(`e2e server on http://127.0.0.1:${PORT}`));
