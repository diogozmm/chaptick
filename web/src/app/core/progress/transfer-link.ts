import { ProgressImportError } from './progress.store';

/**
 * Progress carried inside a link: `https://host/#transfer=<token>`. The part after `#` never
 * reaches a server (Cloudflare, analytics), only the browser that opens the link. Used to move
 * progress to another device, or to a new domain, since browsers keep each address's data apart.
 */
export const TRANSFER_PARAM = 'transfer';

// Token prefixes: gzip-compressed (every current browser) or plain, for older ones.
const GZIP = 'z';
const PLAIN = 'j';

export async function encodeTransfer(json: string): Promise<string> {
  const bytes = new TextEncoder().encode(json);
  if (typeof CompressionStream !== 'function') return PLAIN + toBase64Url(bytes);
  const zipped = await new Response(new Response(bytes).body!.pipeThrough(new CompressionStream('gzip'))).arrayBuffer();
  return GZIP + toBase64Url(new Uint8Array(zipped));
}

export async function decodeTransfer(token: string): Promise<string> {
  try {
    const bytes = fromBase64Url(token.slice(1));
    if (token.startsWith(PLAIN)) return new TextDecoder().decode(bytes);
    if (token.startsWith(GZIP)) {
      const stream = new Response(bytes).body!.pipeThrough(new DecompressionStream('gzip'));
      return await new Response(stream).text();
    }
  } catch {
    // Falls through: a cut or edited link.
  }
  throw new ProgressImportError('wrong-format');
}

export const transferLink = (origin: string, token: string): string => `${origin}/#${TRANSFER_PARAM}=${token}`;

/** The token in a location hash like `#transfer=z…`, or null. */
export function transferToken(hash: string): string | null {
  const value = new URLSearchParams(hash.replace(/^#/, '')).get(TRANSFER_PARAM);
  return value || null;
}

function toBase64Url(bytes: Uint8Array): string {
  let binary = '';
  for (let i = 0; i < bytes.length; i += 0x8000) binary += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(binary).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function fromBase64Url(text: string): Uint8Array<ArrayBuffer> {
  const binary = atob(text.replace(/-/g, '+').replace(/_/g, '/'));
  const bytes = new Uint8Array(new ArrayBuffer(binary.length));
  for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
  return bytes;
}
