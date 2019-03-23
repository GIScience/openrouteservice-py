# -*- coding: utf-8 -*-
# Copyright 2014 Google Inc. All rights reserved.
#
# Modifications Copyright (C) 2018 HeiGIT, University of Heidelberg.
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

"""Converts Python types to string representations suitable for ORS API server.
"""


def _pipe_list(arg):
    """Convert list of values to pipe-delimited string"""
    if not _is_list(arg):
        raise TypeError(
            "Expected a list or tuple, "
            "but got {}".format(type(arg).__name__))
    return "|".join(map(str, arg))


def _comma_list(arg):
    """Convert list to comma-separated string"""
    if not _is_list(arg):
        raise TypeError(
            "Expected a list or tuple, "
            "but got {}".format(type(arg).__name__))
    return ",".join(map(str, arg))


def _convert_bool(boolean):
    """Convert to stringified boolean"""

    return str(boolean).lower()


def _format_float(arg):
    """Formats a float value to be as short as possible.

    Trims extraneous trailing zeros and period to give API
    args the best possible chance of fitting within 2000 char
    URL length restrictions.

    For example:

    format_float(40) -> "40"
    format_float(40.0) -> "40"
    format_float(40.1) -> "40.1"
    format_float(40.001) -> "40.001"
    format_float(40.0010) -> "40.001"

    :param arg: The lat or lng float.
    :type arg: float

    :rtype: string
    """
    return ("{}".format(round(float(arg), 6)).rstrip("0").rstrip("."))


def _build_coords(arg):
    """Converts one or many lng/lat pair(s) to a comma-separated, pipe 
    delimited string. Coordinates will be rounded to 5 digits.

    For example:

    convert.build_coords([(151.2069902,-33.8674869),(2.352315,48.513158)])
    # '151.20699,-33.86749|2.35232,48.51316'

    :param arg: The lat/lon pair(s).
    :type arg: list or tuple
    
    :rtype: str
    """
    if _is_list(arg):
        return _pipe_list(_concat_coords(arg))
    else:
        raise TypeError(
            "Expected a list or tuple of lng/lat tuples or lists, "
            "but got {}".format(type(arg).__name__))


def _concat_coords(arg):
    """Turn the passed coordinate tuple(s) in comma separated coordinate tuple(s).
    
    :param arg: coordinate pair(s)
    :type arg: list or tuple
    
    :rtype: list of strings
    """
    if all(_is_list(tup) for tup in arg):
        # Check if arg is a list/tuple of lists/tuples
        return [_comma_list(map(_format_float, tup)) for tup in arg]
    else:
        return [_comma_list(_format_float(coord) for coord in arg)]


def _is_list(arg):
    """Checks if arg is list-like."""
    if isinstance(arg, dict):
        return False
    if isinstance(arg, str):  # Python 3-only, as str has __iter__
        return False
    return (not _has_method(arg, "strip")
            and _has_method(arg, "__getitem__")
            or _has_method(arg, "__iter__"))


def _has_method(arg, method):
    """Returns true if the given object has a method with the given name.

    :param arg: the object

    :param method: the method name
    :type method: string

    :rtype: bool
    """
    return hasattr(arg, method) and callable(getattr(arg, method))


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
            if b < 0x1f:
                break
        lat += (~result >> 1) if (result & 1) != 0 else (result >> 1)

        result = 1
        shift = 0
        while True:
            b = ord(polyline[index]) - 63 - 1
            index += 1
            result += b << shift
            shift += 5
            if b < 0x1f:
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
                if b < 0x1f:
                    break
            if (result & 1) != 0:
                z += ~(result >> 1)
            else:
                z += (result >> 1)

            points.append([round(lng * 1e-5, 6), round(lat * 1e-5, 6), round(z * 1e-2, 1)])

        else:
            points.append([round(lng * 1e-5, 6), round(lat * 1e-5, 6)])

    geojson = {u'type': u'LineString', u'coordinates': points}

    return geojson
