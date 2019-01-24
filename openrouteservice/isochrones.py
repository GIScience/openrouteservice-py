# -*- coding: utf-8 -*-
# Copyright (C) 2018 HeiGIT, University of Heidelberg.
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

"""Performs requests to the ORS isochrones API."""

from openrouteservice import convert, validator


def isochrones(client, locations,
               profile='driving-car',
               range_type='time',
               intervals=None,
               segments=None,
               units=None,
               location_type=None,
               smoothing=None,
               attributes=None,
               # options=None,
               intersections=None,
               dry_run=None):
    """ Gets travel distance and time for a matrix of origins and destinations.

    :param locations: One pair of lng/lat values.
    :type locations: list or tuple of lng,lat values

    :param profile: Specifies the mode of transport to use when calculating
        directions. One of ["driving-car", "driving-hgv", "foot-walking",
        "foot-hiking", "cycling-regular", "cycling-road",
        "cycling-safe", "cycling-mountain", "cycling-tour", 
        "cycling-electric",]. Default "driving-car".
    :type profile: string

    :param range_type: Set 'time' for isochrones or 'distance' for equidistants.
        Default 'time'.
    :type sources: string

    :param intervals: Ranges to calculate distances/durations for. This can be
        a list of multiple ranges, e.g. [600, 1200, 1400] or a single value list.
        In the latter case, you can also specify the 'segments' variable to break
        the single value into more isochrones. In meters or seconds. Default [60].
    :type intervals: list of integer(s)

    :param segments: Segments isochrones or equidistants for one 'intervals' value.
        Only has effect if used with a single value 'intervals' parameter.
        In meters or seconds. Default 20.
    :type segments: integer

    :param units: Specifies the unit system to use when displaying results.
        One of ["m", "km", "m"]. Default "m".
    :type units: string
    
    :param location_type: 'start' treats the location(s) as starting point,
        'destination' as goal. Default 'start'.
    :type location_type: string

    :param smoothing: Applies a level of generalisation to the isochrone polygons generated.
        Value between 0 and 1, whereas a value closer to 1 will result in a more generalised shape.
    :type smoothing: float

    :param attributes: 'area' returns the area of each polygon in its feature
        properties. 'reachfactor' returns a reachability score between 0 and 1.
        'total_pop' returns population statistics from https://ghsl.jrc.ec.europa.eu/about.php.
        One or more of ['area', 'reachfactor', 'total_pop']. Default 'area'.
    :type attributes: list of string(s)

    :param options: not implemented right now.
    :type options: dict
    
    :param intersections: not implented right now.
    :type intersections: boolean
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean
    
    :raises ValueError: When parameter has invalid value(s).
    
    :rtype: call to Client.request()
    """

    validator.validator(locals(), 'isochrones')

    params = {
        "locations": convert._build_coords(locations)
    }

    if profile:
        params["profile"] = profile

    if range_type:
        params["range_type"] = range_type

    if intervals:
        params["range"] = convert._comma_list(intervals)

    if segments:
        params["interval"] = str(segments)
        
    if units:
        # if units and (range_type == None or range_type == 'time'):
        #     raise ValueError("For range_type time, units cannot be specified.")
        params["units"] = units

    if location_type:
        params["location_type"] = location_type

    if smoothing:
        params["smoothing"] = convert._format_float(smoothing)

    if attributes:
        params["attributes"] = convert._pipe_list(attributes)

    return client.request("/isochrones", params, dry_run=dry_run)
