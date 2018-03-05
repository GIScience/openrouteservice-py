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

"""Performs requests to the ORS Matrix API."""

from openrouteservice import convert


def distance_matrix(client, locations,
                    profile='driving-car',
                    sources='all',
                    destinations='all',
                    metrics=None,
                    resolve_locations=None,
                    units=None,
                    optimized='true',
                    dry_run=None):
    """ Gets travel distance and time for a matrix of origins and destinations.

    :param locations: One or more pairs of lng/lat values.
    :type locations: a single location, or a list of locations, where a
        location is a list or tuple of lng,lat values

    :param profile: Specifies the mode of transport to use when calculating
        directions. One of ["driving-car", "driving-hgv", "foot-walking",
        "foot-hiking", "cycling-regular", "cycling-road",
        "cycling-safe", "cycling-mountain", "cycling-tour", 
        "cycling-electric",]. Default "driving-car".
    :type profile: string

    :param sources: A list of indices that refer to the list of locations
        (starting with 0) or 'all'. Default 'all'.
    :type sources: One or more indices inside a list; or 'all' (string).

    :param destinations: A list of indices that refer to the list of locations
        (starting with 0) or 'all'. Default 'all'.
    :type destinations: One or more indices inside a list; or 'all' (string).

    :param metrics: Specifies a list of returned metrics. One or more of ["distance",
        "duration"]. Default ['duration'].
    :type metrics: list of strings

    :param resolve_locations: Specifies whether given locations are resolved or
        not. If set 'true', every element in destinations and sources will 
        contain the name element that identifies the name of the closest street.
        'true' or 'false'. Default 'false'.
    :type resolve_locations: boolean as string

    :param units: Specifies the unit system to use when displaying results.
        One of ["m", "km", "m"]. Default "m".
    :type units: string

    :param optimized: Specifies whether Dijkstra algorithm ('false') or any 
        available technique to speed up shortest-path routing ('true') is used. 
        For normal Dijkstra the number of visited nodes is limited to 100000.
        Default 'true'.
    :type optimized: boolean as string
    
    :raises ValueError: When profile parameter has wrong value.
    
    :rtype: call to Client.request()
    """

    params = {
        "locations": locations,
        "sources": sources,
        "destinations": destinations
    }

    if profile:
        # NOTE(broady): the mode parameter is not validated by the Maps API
        # server. Check here to prevent silent failures.
        if profile not in ["driving-car",
                           "driving-hgv",
                           "foot-walking",
                           "foot-hiking",
                           "cycling-regular",
                           "cycling-road",
                           "cycling-safe",
                           "cycling-mountain",
                           "cycling-tour", 
                           "cycling-electric",
                           ]:
            raise ValueError("Invalid travel mode.")
        params["profile"] = profile

    if sources:
        if sources == 'all': 
            params["sources"] = sources
        else:
            params["sources"] = convert._comma_list(sources)

    if destinations:
        if destinations == 'all': 
            params["destinations"] = destinations
        else:
            params["destinations"] = convert._comma_list(destinations)

    if metrics:
        params["metrics"] = convert._pipe_list(metrics)

    if resolve_locations:
        params["resolve_locations"] = resolve_locations

    if units:
        params["units"] = units

    if optimized:
        # not checked on backend, check here
        convert._checkBool(optimized)
        params["optimized"] = optimized


    return client.request("/matrix", {}, post_json=params, dry_run=dry_run) # No get() params
