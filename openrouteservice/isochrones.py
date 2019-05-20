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

from openrouteservice import deprecation


def isochrones(client, locations,
               profile='driving-car',
               range_type='time',
               range=None,
               intervals=None,
               segments=None,
               interval=None,
               units=None,
               location_type=None,
               smoothing=None,
               attributes=None,
               validate=True,
               dry_run=None):
    """ Gets travel distance and time for a matrix of origins and destinations.

    :param locations: One pair of lng/lat values.
    :type locations: list or tuple of lng,lat values

    :param profile: Specifies the mode of transport to use when calculating
        directions. One of ["driving-car", "driving-hgv", "foot-walking",
        "foot-hiking", "cycling-regular", "cycling-road", "cycling-mountain",
        "cycling-electric",]. Default "driving-car".
    :type profile: string

    :param range_type: Set 'time' for isochrones or 'distance' for equidistants.
        Default 'time'.
    :type sources: string

    :param intervals: [SOON DEPRECATED] replaced by `range`.
    :type intervals: list of integer(s)

    :param range: Ranges to calculate distances/durations for. This can be
        a list of multiple ranges, e.g. [600, 1200, 1400] or a single value list.
        In the latter case, you can also specify the 'interval' variable to break
        the single value into more isochrones. In meters or seconds.
    :type range: list of integer(s)

    :param segments: [SOON DEPRECATED] replaced by `interval`.
    :type segments: integer

    :param interval: Segments isochrones or equidistants for one 'range' value.
        Only has effect if used with a single value 'range' value.
        In meters or seconds.
    :type interval: integer

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

    :param validate: Specifies whether parameters should be validated before sending the request. Default True.
    :type validate: bool
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean
    
    :raises ValueError: When parameter has invalid value(s).
    
    :rtype: call to Client.request()
    """

    params = {
        "locations": locations
    }

    if profile:
        params["profile"] = profile

    if range_type:
        params["range_type"] = range_type

    if intervals:
        deprecation.warning('intervals', 'range')

    range = range or intervals
    params['range'] = range

    if segments:
        deprecation.warning('segments', 'interval')

    interval = interval or segments
    if interval:
        params['interval'] = interval

    if units:
        params["units"] = units

    if location_type:
        params["location_type"] = location_type

    if smoothing:
        params["smoothing"] = smoothing

    if attributes:
        params["attributes"] = attributes

    return client.request("/v2/isochrones/" + profile + '/geojson', {}, post_json=params, dry_run=dry_run)
