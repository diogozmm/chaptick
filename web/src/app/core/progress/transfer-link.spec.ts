import { ProgressImportError } from './progress.store';
import { decodeTransfer, encodeTransfer, transferLink, transferToken } from './transfer-link';

describe('transfer link', () => {
  const json = JSON.stringify({
    schemaVersion: 1,
    app: 'chaptick',
    games: [{ gameId: 'sc', currentChapter: 'sc-ch3', doneItems: Array.from({ length: 400 }, (_, i) => `sc-ch3-co-09#step-${i}`) }],
  });

  it('round-trips progress through a compact, URL-safe token', async () => {
    const token = await encodeTransfer(json);
    expect(token).toMatch(/^z[A-Za-z0-9_-]+$/);
    expect(token.length).toBeLessThan(json.length / 4);
    expect(await decodeTransfer(token)).toBe(json);
  });

  it('builds and reads the link without sending the data to the server', async () => {
    const token = await encodeTransfer(json);
    const link = transferLink('https://chaptick.example', token);
    const url = new URL(link);
    expect(url.pathname).toBe('/');
    expect(url.search).toBe('');
    expect(transferToken(url.hash)).toBe(token);
    expect(transferToken('#other=1')).toBeNull();
    expect(transferToken('')).toBeNull();
  });

  it('rejects a cut or edited link', async () => {
    const token = await encodeTransfer(json);
    await expect(decodeTransfer(token.slice(0, 40))).rejects.toBeInstanceOf(ProgressImportError);
    await expect(decodeTransfer('x123')).rejects.toBeInstanceOf(ProgressImportError);
  });
});
