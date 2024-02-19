def decode_polyline(polyline, is3d=False):
    """Decodes a Polyline string into a GeoJSON geometry.
    :param polyline: An encoded polyline, only the geometry.
    :type polyline: string
    :param is3d: Specifies if geometry contains Z component.
    :type is3d: boolean
    :returns: GeoJSON Linestring geometry
    :rtype: dict
    """
    points = []
    index = lat = lng = z = 0

    while index < len(polyline):
        result = 1
        shift = 0
        while True:
            b = ord(polyline[index]) - 63 - 1
            index += 1
            result += b << shift
            shift += 5
            if b < 0x1F:
                break
        lat += (~result >> 1) if (result & 1) != 0 else (result >> 1)

        result = 1
        shift = 0
        while True:
            b = ord(polyline[index]) - 63 - 1
            index += 1
            result += b << shift
            shift += 5
            if b < 0x1F:
                break
        lng += ~(result >> 1) if (result & 1) != 0 else (result >> 1)

        if is3d:
            result = 1
            shift = 0
            while True:
                b = ord(polyline[index]) - 63 - 1
                index += 1
                result += b << shift
                shift += 5
                if b < 0x1F:
                    break
            if (result & 1) != 0:
                z += ~(result >> 1)
            else:
                z += result >> 1

            points.append(
                [
                    round(lng * 1e-5, 6),
                    round(lat * 1e-5, 6),
                    round(z * 1e-2, 1),
                ]
            )

        else:
            points.append([round(lng * 1e-5, 6), round(lat * 1e-5, 6)])

    geojson = {u"type": u"LineString", u"coordinates": points}

    return geojson


def todict(obj, classkey=None):
    """Converts an object to a dict
    :param obj: the object to convert
    """
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "to_dict"):
        return obj.to_dict()
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key[1:] if key[0] == "_" else key, todict(getattr(obj, key), classkey)) 
            for key in obj.__dict__])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj
