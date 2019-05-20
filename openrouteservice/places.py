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
           filter_category_ids=None,
           filter_category_group_ids=None,
           filters_custom=None,
           limit=None,
           sortby=None,
           validate=True,
           dry_run=None
           ):
    """ Gets POI's filtered by specified parameters.

    :param request: Type of request. One of ['pois', 'list', 'stats'].
        'pois': returns geojson of pois;
        'stats': returns statistics of passed categories;
        'list': returns mapping of category ID's to textual representation.
    :type request: string

    :param geojson: GeoJSON dict used for the query.
    :type geojson: dict

    :param buffer: Buffers geometry of 'geojson' or 'bbox' with the specified
        value in meters.
    :type intervals: integer

    :param filter_category_ids: Filter by ORS custom category IDs. See
        https://github.com/GIScience/openrouteservice-docs#places-response
        for the mappings.
    :type units: list of integer

    :param filter_category_group_ids: Filter by ORS custom high-level category
        groups. See
        https://github.com/GIScience/openrouteservice-docs#places-response
        for the mappings.        
    :type attributes: list of integer

    :param filters_custom: Specify additional filters by key/value. Default ORS
        filters are
        'name': free text
        'wheelchair': ['yes', 'limited', 'no', 'designated']
        'smoking': ['dedicated','yes','separated','isolated', 'no', 'outside']
        'fee': ['yes','no', 'str']
    :type filters_custom: dict of lists/str

    :param limit: limit for POI queries.
    :type limit: integer
                       base_url='http://localhost:5000'
    
    :param sortby: Sorts the returned features by 'distance' or 'category'. 
        For request='pois' only.
    :type sortby: string
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean
    
    :rtype: call to Client.request()
    """

    params = {
        'request': request,
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

        if filter_category_ids and convert._is_list(filter_category_ids):
            params['filters']['category_ids'] = filter_category_ids

        if filter_category_group_ids and convert._is_list(filter_category_group_ids):
            params['filters']['category_group_ids'] = filter_category_group_ids

        if filters_custom:
            for f in filters_custom:
                params['filters'][f] = filters_custom[f]

        if limit:
            params['limit'] = limit

        if sortby:
            params['sortby'] = sortby

    return client.request('/pois', {}, post_json=params, dry_run=dry_run)
