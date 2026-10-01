import 'fake-indexeddb/auto';
import { TestBed } from '@angular/core/testing';

import { SITE } from '../../site.config';
import { TransferService } from './transfer.service';

describe('TransferService', () => {
  afterEach(() => (SITE.canonicalOrigin = ''));

  const service = () => {
    TestBed.resetTestingModule();
    return TestBed.inject(TransferService);
  };

  it('stays quiet while no canonical address is set', () => {
    expect(service().movedTo).toBeNull();
  });

  it('points to the canonical address from any other one', () => {
    SITE.canonicalOrigin = 'https://chaptick.example';
    expect(service().movedTo).toBe('https://chaptick.example');
  });

  it('does not ask to move when already on the canonical address', () => {
    SITE.canonicalOrigin = location.origin;
    expect(service().movedTo).toBeNull();
  });

  it('builds links that open on a given address', async () => {
    const link = await service().createLink('https://chaptick.example');
    expect(link).toMatch(/^https:\/\/chaptick\.example\/#transfer=z/);
  });
});
