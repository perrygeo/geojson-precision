# poly-point-simplify

Command line interface to process GeoJSON features, replacing geometries smaller than a certain area threshold with points.

```
$ cat collection.geojson | geojson-summary
177 multipolygons

$ poly-point-simplify --min-area 2 collection.geojson | geojson-summary
24 points and 153 multipolygons
```

Why? If you're making choropleth maps, small polygons may disappear or become impossible to interpret. You can employ this handy cartographic technique to ensure all features' data are still represented on the map. 

<img src="https://pbs.twimg.com/media/Ca2cb3fWAAAJZkV.jpg">

Install with

```
git clone https://github.com/perrygeo/poly-point-simplify.git
cd poly-point-simplify
pip install -e .
```
