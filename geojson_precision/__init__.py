from shapely.geometry import asShape


def _set_precision(coords, precision):
    result = []
    try:
        return round(coords, int(precision))
    except TypeError:
        for coord in coords:
            result.append(_set_precision(coord, precision))
    return result


def coord_precision(features, precision, validate=True):
    for feature in features:
        coords = _set_precision(feature['geometry']['coordinates'], precision)
        feature['geometry']['coordinates'] = coords
        if validate:
            geom = asShape(feature['geometry'])
            geom.is_valid
        yield feature
