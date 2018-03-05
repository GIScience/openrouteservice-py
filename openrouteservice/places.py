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

"""Performs requests to the ORS Places API."""

from openrouteservice import convert

def places(client, request,
                geojson=None,
                bbox=None,
                buffer=None,
                filter_name=None,
                filter_wheelchair=None,
                filter_smoking=None,
                filter_category_ids=None,
                filter_category_group_ids=None,
                limit=None,
                sortby=None,
                    ):
    """ Gets POI's filtered by specified parameters.

    :param request: Type of request. One or more of ['pois', 'category_list', 'category_stats'].
        pois: returns geojson of pois;
        category_stats: returns statistics of passed categories;
        category_list: returns mapping of category ID's to textual representation.
    :type request: list of strings

    :param profile: Specifies the mode of transport to use when calculating
        directions. One of ["driving-car", "driving-hgv", "foot-walking",
        "foot-hiking", "cycling-regular", "cycling-road",
        "cycling-safe", "cycling-mountain", "cycling-tour", 
        "cycling-electric",]. Default "driving-car".
    :type profile: string

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

    :param attributes: 'area' returns the area of each polygon in its feature
        properties. 'reachfactor' returns a reachability score between 0 and 1.
        One or more of ['area', 'reachfactor']. Default 'area'.
    :type attributes: list of string(s)

    :param options: not implemented right now.
    :type options: dict
    
    :param intersections: not implented right now.
    :type intersections: boolean as string
    
    :raises ValueError: When parameter has invalid value(s).
    
    :rtype: dict from JSON response
    """
    
    params = {'request': request,
              'filters': dict(),
              'geometry': dict(),
              }
    
    if request != 'category_list':
        if geojson:
            params['geometry']['geojson'] = geojson
            
        if bbox:
            params['geometry']['bbox'] = bbox
            
        if buffer:
            params['geometry']['buffer'] = buffer
                    
        if filter_name:
            params['filters']['name'] = filter_name
                    
        if filter_wheelchair:
            params['filters']['wheelchair'] = filter_wheelchair
                    
        if filter_smoking:
            params['filters']['smoking'] = filter_smoking
                    
        if filter_category_ids and convert._is_list(filter_category_ids):
            params['filters']['category_ids'] = filter_category_ids
                    
        if filter_category_group_ids:
            params['filters']['categroy_group_ids'] = filter_category_group_ids
                    
        if limit:
            params['limit'] = limit
                    
        if sortby:
            params['sortby'] = sortby
            
    return client.request('/places', {}, post_json=params)