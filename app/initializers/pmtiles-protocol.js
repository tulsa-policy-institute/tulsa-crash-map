import maplibregl from 'maplibre-gl';
import pmtiles from 'pmtiles';

export function initialize() {
  const cache = new pmtiles.ProtocolCache();
  maplibregl.addProtocol('pmtiles', cache.protocol);
}

export default {
  initialize,
};
