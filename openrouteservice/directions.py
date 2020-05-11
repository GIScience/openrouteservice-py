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

"""Performs requests to the ORS directions API."""

from openrouteservice import deprecation
from openrouteservice.optimization import optimization, Job, Vehicle

import warnings


def directions(client,
               coordinates,
               profile='driving-car',
               format_out=None,
               format='json',
               preference=None,
               units=None,
               language=None,
               geometry=None,
               geometry_simplify=None,
               instructions=None,
               instructions_format=None,
               alternative_routes=None,
               roundabout_exits=None,
               attributes=None,
               maneuvers=None,
               radiuses=None,
               bearings=None,
               skip_segments=None,
               continue_straight=None,
               elevation=None,
               extra_info=None,
               suppress_warnings=None,
               optimized=None,
               optimize_waypoints=None,
               options=None,
               validate=True,
               dry_run=None):
    """Get directions between an origin point and a destination point.

    For more information, visit https://go.openrouteservice.org/documentation/.

    :param coordinates: The coordinates tuple the route should be calculated
        from. In order of visit.
    :type origin: list or tuple of coordinate lists or tuples

    :param profile: Specifies the mode of transport to use when calculating
        directions. One of ["driving-car", "driving-hgv", "foot-walking",
        "foot-hiking", "cycling-regular", "cycling-road","cycling-mountain",
        "cycling-electric",]. Default "driving-car".
    :type profile: string

    :param format: Specifies the response format. One of ['json', 'geojson', 'gpx']. Default "json".
        Geometry format for "json" is Google's encodedpolyline. The GPX schema the response is validated
        against can be found here:
        https://raw.githubusercontent.com/GIScience/openrouteservice-schema/master/gpx/v1/ors-gpx.xsd.
    :type format: str

    :param format_out: DEPRECATED.
    :type format: str

    :param preference: Specifies the routing preference. One of ["fastest, "shortest",
        "recommended"]. Default "fastest".
    :type preference: string

    :param units: Specifies the distance unit. One of ["m", "km", "mi"]. Default "m".
    :type units: string

    :param language: Language for routing instructions. One of ["en", "de", "cn",
        "es", "ru", "dk", "fr", "it", "nl", "br", "se", "tr", "gr"]. Default "en".
    :type language: string

    :param language: The language in which to return results.
    :type language: string

    :param geometry: Specifies whether geometry should be returned. Default True.
    :type geometry: boolean

    :param geometry_simplify: Specifies whether to simplify the geometry.
        Default False.
    :type geometry_simplify: boolean

    :param instructions: Specifies whether to return turn-by-turn instructions.
        Default True.
    :type instructions: boolean

    :param instructions_format: Specifies the the output format for instructions.
        One of ["text", "html"]. Default "text".
    :type instructions_format: string

    :param alternative_routes: Specifies whether alternative routes are computed,
        and parameters for the algorithm determining suitable alternatives. Expects
        3 keys: share_factor (float), target_count (int), weight_factor (float).
        More on https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/geojson/post.
    :type alternative_routes: dict[int|float]

    :param roundabout_exits: Provides bearings of the entrance and all passed
        roundabout exits. Adds the 'exit_bearings' array to the 'step' object
        in the response. Default False.
    :type roundabout_exits: boolean

    :param attributes: Returns route attributes on ["detourfactor", "percentage"].
        Must be a list of strings. Default None.
    :type attributes: list or tuple of strings

    :param maneuvers: Specifies whether the maneuver object is included into the step object or not. Default: false.
    :type maneuvers bool

    :param radiuses: A list of maximum distances (measured in
        meters) that limit the search of nearby road segments to every given waypoint.
        The values must be greater than 0, the value of -1 specifies no limit in
        the search. The number of radiuses must correspond to the number of waypoints.
        Default None.
    :type radiuses: list or tuple

    :param bearings: Specifies a list of pairs (bearings and
        deviations) to filter the segments of the road network a waypoint can
        snap to. For example bearings=[[45,10],[120,20]]. Each pair is a
        comma-separated list that can consist of one or two float values, where
        the first value is the bearing and the second one is the allowed deviation
        from the bearing. The bearing can take values between 0 and 360 clockwise
        from true north. If the deviation is not set, then the default value of
        100 degrees is used. The number of pairs must correspond to the number
        of waypoints. Setting optimized=false is mandatory for this feature to
        work for all profiles. The number of bearings corresponds to the length
        of waypoints-1 or waypoints. If the bearing information for the last waypoint
        is given, then this will control the sector from which the destination
        waypoint may be reached.
    :type bearings: list or tuple or lists or tuples

    :param skip_segments: Specifies the segments that should be skipped in the route calculation.
        A segment is the connection between two given coordinates and the counting starts with 1
        for the connection between the first and second coordinate.
    :type skip_segments: list[int]

    :param continue_straight: Forces the route to keep going straight at waypoints
        restricting u-turns even if u-turns would be faster. This setting
        will work for all profiles except for driving-*. In this case you will
        have to set optimized=false for it to work. True or False. Default False.
    :type continue_straight: boolean

    :param elevation: Specifies whether to return elevation values for points.
        Default False.
    :type elevation: boolean

    :param extra_info: Returns additional information on ["steepness", "suitability",
        "surface", "waycategory", "waytype", "tollways", "traildifficulty", "roadaccessrestrictions"].
        Must be a list of strings. Default None.
    :type extra_info: list or tuple of strings

    :param suppress_warnings: Tells the system to not return any warning messages and corresponding extra_info.
        For false the extra information can still be explicitly requested by adding it with the extra_info parameter.
    :type suppress_warnings: bool

    :param optimized: If set False, forces to not use Contraction Hierarchies.
    :type optimized: bool

    :param options: Refer to https://openrouteservice.org/dev/#/api-docs/v2/directions/{profile}/geojson/post for
        detailed documentation. Construct your own dict() following the example
        of the minified options object. Will be converted to json automatically.
    :type options: dict

    :param optimize_waypoints: If True, a `Vroom <https://github.com/VROOM-Project/vroom>`_ instance (ORS optimization
        endpoint) will optimize the `via` waypoints, i.e. all coordinates between the first and the last. It assumes
        the first coordinate to be the start location and the last coordinate to be the end location. Only requests with
        a minimum of 4 coordinates, no routing options and fastest weighting. Default False.
    :type optimize_waypoints: bool

    :param validate: Specifies whether parameters should be validated before sending the request. Default True.
    :type validate: bool
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean

    :raises ValueError: When parameter has wrong value.
    :raises TypeError: When parameter is of wrong type.

    :returns: sanitized set of parameters
    :rtype: call to Client.request()
    """

    # call optimization endpoint and get new order of waypoints
    if optimize_waypoints is not None and not dry_run:
        if len(coordinates) <= 3:
            warnings.warn("Less than 4 coordinates, nothing to optimize!", UserWarning)
        elif options:
            warnings.warn("Options are not compatible with optimization.", UserWarning)
        elif preference == 'shortest':
            warnings.warn("Shortest is not compatible with optimization.", UserWarning)
        else:
            coordinates = _optimize_waypoint_order(client, coordinates, profile)

    params = {"coordinates": coordinates}

    if format_out:
        deprecation.warning('format_out', 'format')

    format = format_out or format

    if preference:
        params["preference"] = preference

    if units:
        params["units"] = units

    if language:
        params["language"] = language

    if geometry is not None:
        params["geometry"] = geometry

    if geometry_simplify is not None:
        params["geometry_simplify"] = geometry_simplify

    if instructions is not None:
        params["instructions"] = instructions

    if instructions_format:
        params["instructions_format"] = instructions_format

    if alternative_routes:
        params["alternative_routes"] = alternative_routes

    if roundabout_exits is not None:
        params["roundabout_exits"] = roundabout_exits

    if attributes:
        params["attributes"] = attributes

    if radiuses:
        params["radiuses"] = radiuses

    if maneuvers is not None:
        params['maneuvers'] = maneuvers

    if bearings:
        params["bearings"] = bearings

    if skip_segments:
        params["skip_segments"] = skip_segments

    if continue_straight is not None:
        params["continue_straight"] = continue_straight

    if elevation is not None:
        params["elevation"] = elevation

    if extra_info:
        params["extra_info"] = extra_info

    if suppress_warnings is not None:
        params['suppress_warnings'] = suppress_warnings

    if optimized is not None:
        if (bearings or continue_straight) and optimized in (True, 'true'):
            params["optimized"] = 'false'
            print("Set optimized='false' due to incompatible parameter settings.")
        else:
            params["optimized"] = optimized

    if options:
        params['options'] = options

    return client.request("/v2/directions/" + profile + '/' + format, {}, post_json=params, dry_run=dry_run)


def _optimize_waypoint_order(client, coordinates, profile):

    start = coordinates[0]
    end = coordinates[-1]
    veh = [Vehicle(
        id=0,
        profile=profile,
        start=start,
        end=end
    )]

    jobs = []
    for idx, coord in enumerate(coordinates[1:-1]):
        jobs.append(Job(
            id=idx,
            location=coord
        ))

    params = {
        'jobs': jobs,
        'vehicles': veh
    }

    optimization_res = optimization(client, **params)

    coordinates = []
    for step in optimization_res['routes'][0]['steps']:
        coordinates.append(step['location'])

    return coordinates
