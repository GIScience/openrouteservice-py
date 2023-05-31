# -*- coding: utf-8 -*-

PARAM_POINT = [8.34234, 48.23424]
PARAM_LINE = [[8.688641, 49.420577], [8.680916, 49.415776]]
PARAM_POLY = [[[8.688641, 49.420577], [8.680916, 49.415776]]]

PARAM_INT_BIG = 500
PARAM_INT_SMALL = 50
PARAM_LIST_ONE = [PARAM_INT_SMALL, PARAM_INT_SMALL]
PARAM_LIST_TWO = [PARAM_LIST_ONE, PARAM_LIST_ONE]

PARAM_GEOJSON_POINT = {"type": "Point", "coordinates": PARAM_POINT}
PARAM_GEOJSON_LINE = {"type": "LineString", "coordinates": PARAM_LINE}
PARAM_GEOJSON_POLY = {"type": "Polygon", "coordinates": PARAM_POLY}

ENDPOINT_DICT = {
    "directions": {
        "coordinates": PARAM_LINE,
        "profile": "driving-car",
        "preference": "fastest",
        "format": "geojson",
        "units": "mi",
        "language": "en",
        "geometry": "true",
        "geometry_simplify": "false",
        "maneuvers": True,
        "suppress_warnings": False,
        "instructions": "false",
        "instructions_format": "html",
        "alternative_routes": {
            "share_factor": 0.6,
            "target_count": 2,
            "weight_factor": 1.4,
        },
        "roundabout_exits": "true",
        "attributes": ["avgspeed"],
        "radiuses": PARAM_LIST_ONE,
        "bearings": PARAM_LIST_TWO,
        "skip_segments": [0, 1],
        "elevation": "true",
        "maximum_speed": 95,
        "extra_info": ["roadaccessrestrictions"],
        "optimized": "false",
        "continue_straight": True,
        "options": {"avoid_features": ["highways", "tollways"]},
    },
    "isochrones": {
        "locations": PARAM_LINE,
        "profile": "cycling-regular",
        "range_type": "distance",
        "range": [PARAM_INT_BIG],
        "units": "m",
        "location_type": "destination",
        "attributes": ["area", "reachfactor"],
        "interval": [PARAM_INT_SMALL],
        "intersections": "true",
        "options": {"avoid_features": ["highways", "tollways"]},
    },
    "distance_matrix": {
        "locations": PARAM_LINE,
        "sources": [1],
        "destinations": [0],
        "profile": "driving-car",
        "metrics": ["duration", "distance"],
        "resolve_locations": "true",
        "units": "mi",
        "optimized": "false",
    },
    "elevation_point": {
        "format_in": "geojson",
        "format_out": "point",
        "geometry": PARAM_GEOJSON_POINT,
        "dataset": "srtm",
    },
    "elevation_line": {
        "format_in": "geojson",
        "format_out": "polyline",
        "geometry": PARAM_GEOJSON_LINE,
        "dataset": "srtm",
    },
    "pelias_search": {
        "text": "Heidelberg",
        "focus_point": PARAM_POINT,
        "rect_min_x": PARAM_INT_BIG,
        "rect_min_y": PARAM_INT_BIG,
        "rect_max_x": PARAM_INT_BIG + 1,
        "rect_max_y": PARAM_INT_BIG + 1,
        "circle_point": PARAM_POINT,
        "circle_radius": PARAM_INT_SMALL,
        "sources": ["osm", "wof", "gn"],
        "layers": ["locality", "county", "region"],
        "country": "de",
        "size": PARAM_INT_SMALL,
    },
    "pelias_autocomplete": {
        "text": "Heidelberg",
        "focus_point": PARAM_POINT,
        "rect_min_x": PARAM_INT_BIG,
        "rect_min_y": PARAM_INT_BIG,
        "rect_max_x": PARAM_INT_BIG,
        "rect_max_y": PARAM_INT_BIG,
        "sources": ["osm", "wof", "gn"],
        "layers": ["locality", "county", "region"],
        "country": "de",
    },
    "pelias_structured": {
        "address": "Berliner Straße 45",
        "neighbourhood": "Neuenheimer Feld",
        "borough": "Heidelberg",
        "locality": "Heidelberg",
        "county": "Rhein-Neckar-Kreis",
        "region": "Baden-Württemberg",
        "postalcode": 69120,
        "country": "de",
    },
    "pelias_reverse": {
        "point": PARAM_POINT,
        "circle_radius": PARAM_INT_SMALL,
        "sources": ["osm", "wof", "gn"],
        "layers": ["locality", "county", "region"],
        "country": "de",
        "size": PARAM_INT_SMALL,
    },
    "pois": {
        "request": "pois",
        "geojson": PARAM_GEOJSON_POINT,
        "bbox": PARAM_LINE,
        "buffer": PARAM_INT_SMALL,
        "filter_category_ids": [PARAM_INT_SMALL],
        "filter_category_group_ids": [PARAM_INT_BIG],
        "filters_custom": {
            "name": "Deli",
            "wheelchair": ["yes", "limited"],
            "smoking": ["dedicated", "separated"],
            "fee": ["yes", "no"],
        },
        "limit": PARAM_INT_SMALL,
        "sortby": "distance",
    },
    "optimization": {
        "shipments": [
            {
                "pickup": {
                    "id": 0,
                    "location": [8.688641, 49.420577],
                    "location_index": 0,
                    "service": 500,
                    "time_windows": [[50, 50]],
                },
                "delivery": {
                    "id": 0,
                    "location": [8.688641, 49.420577],
                    "location_index": 0,
                    "service": 500,
                    "time_windows": [[50, 50]],
                },
                "amount": [50],
                "skills": [50, 50],
                "priority": 50,
            },
            {
                "pickup": {
                    "id": 1,
                    "location": [8.680916, 49.415776],
                    "location_index": 1,
                    "service": 500,
                    "time_windows": [[50, 50]],
                },
                "delivery": {
                    "id": 1,
                    "location": [8.680916, 49.415776],
                    "location_index": 1,
                    "service": 500,
                    "time_windows": [[50, 50]],
                },
                "amount": [50],
                "skills": [50, 50],
                "priority": 50,
            },
        ],
        "jobs": [
            {
                "id": 0,
                "location": PARAM_LINE[0],
                "location_index": 0,
                "service": PARAM_INT_BIG,
                "amount": [PARAM_INT_SMALL],
                "skills": PARAM_LIST_ONE,
                "priority": PARAM_INT_SMALL,
                "time_windows": [PARAM_LIST_ONE],
            },
            {
                "id": 1,
                "location": PARAM_LINE[1],
                "location_index": 1,
                "service": PARAM_INT_BIG,
                "amount": [PARAM_INT_SMALL],
                "skills": PARAM_LIST_ONE,
                "priority": PARAM_INT_SMALL,
                "time_windows": [PARAM_LIST_ONE],
            },
        ],
        "vehicles": [
            {
                "id": 0,
                "profile": "driving-car",
                "start": PARAM_LINE[0],
                "start_index": 0,
                "end_index": 0,
                "end": PARAM_LINE[0],
                "capacity": [PARAM_INT_SMALL],
                "skills": PARAM_LIST_ONE,
                "time_window": PARAM_LIST_ONE,
            },
            {
                "id": 1,
                "profile": "driving-car",
                "start": PARAM_LINE[1],
                "start_index": 1,
                "end_index": 1,
                "end": PARAM_LINE[1],
                "capacity": [PARAM_INT_SMALL],
                "skills": PARAM_LIST_ONE,
                "time_window": PARAM_LIST_ONE,
            },
        ],
        "options": {"g": False},
        "matrix": PARAM_LIST_TWO,
    },
}

GPX_RESPONSE = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gpx version="1.0" creator="openrouteservice" xmlns="https://raw.githubusercontent.com/GIScience/openrouteservice-schema/master/gpx/v2/ors-gpx.xsd">
  <metadata>
    <name>openrouteservice directions</name>
    <desc>This is a directions instructions file as GPX, generated from openrouteservice</desc>
    <author><name>openrouteservice</name>
      <email id="support" domain="openrouteservice.heigit.org"/>
      <link href="https://openrouteservice.org/">
        <text>https://openrouteservice.org/</text>
        <type>text/html</type>
      </link>
    </author>
    <copyright author="openrouteservice.org | OpenStreetMap contributors">
      <year>2021</year>
      <license>LGPL 3.0</license>
    </copyright>
    <time>2021-07-25T17:26:59.023Z</time>
    <bounds maxLat="51.501602" maxLon="0.147508" minLat="51.185303" minLon="-0.076743"/>
    <extensions>
      <system-message></system-message>
    </extensions>
  </metadata>
</gpx>
"""
