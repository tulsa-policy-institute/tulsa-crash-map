# Inspiration
https://incog.maps.arcgis.com/apps/MapSeries/index.html?appid=55f30e03c88b4dd79d2fe0c99d419bd6

# ETL

```bash
ogr2ogr tmp/wrecks.geojson \
  -f GeoJSON "https://services2.arcgis.com/Yl3gDnSPJVdpCPgG/arcgis/rest/services/AGOL_Crash_Map_Features/FeatureServer/0/query?where=objectid%3E0&outfields=*&f=json" ESRIJSON \
  -s_srs EPSG:3857
  -t_srs EPSG:4326
ogr2ogr -f CSV tmp/wrecks.csv tmp/wrecks.geojson
tippecanoe -zg -o tmp/wrecks.mbtiles --drop-densest-as-needed --extend-zooms-if-still-dropping tmp/wrecks.geojson --force
pmtiles-convert tmp/wrecks.mbtiles tmp/wrecks.pmtiles --overwrite
```
