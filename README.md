# geojson-precision

Python function and command line interface to adjust the precision of GeoJSON coordinate positions.

The GeoJSON specification recommends no more than 6 decimal places for latitude and longitude.
This equates to roughly 10cm of precision. You may need slightly more for certain applications.

But many GeoJSON writers provide excessive precision, up to 15 decimal places which is not only
so microscopically small as to be irrelevant for any geospatial application, it also inflates
file sizes, wastes bandwidth, and increases the chances for floating-point inconsistencies.

So instead of 
```
{
    "geometry": {
      "type": "Point",
      "coordinates": [
        100.2380000001,
        5.3120000001
      ]
    },
    "type": "Feature",
    "properties": {}
}
```

Use `geojson-precision` to make coordinate precision a bit more reasonable

```
$ geojson-precision -p 2 < example.geojson

{
  "type": "FeatureCollection",
  "features": [
    {
      "geometry": {
        "type": "Point",
        "coordinates": [
          100.24,
          5.31
        ]
      },
      "type": "Feature",
      "properties": {}
    }
  ]
}
```

For some large geojson feature collections, going from 15 to 6 decimal places can reduce the file size
by roughly 50%.
