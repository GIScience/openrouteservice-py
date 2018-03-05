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

"""Performs requests to the ORS geocoding API."""
from openrouteservice import convert


def geocode(client, query,
            lang=None,
            boundary_type=None,
            rect=None,
            circle=None,
            limit=None,
            dry_run=None):
    """
    Geocoding is the process of converting addresses into geographic
    coordinates.

    :param query: Name of location, street address or postal code. For a 
        structured geocoding request, a dict object can be passed. Please refer
        to https://github.com/GIScience/openrouteservice-docs#geocoding-structured-query
        for details. 
    :type query: string or dict of structured geocoding request

    :param lang: Specifies the language of the response. One of ['de', 'en',
        'fr', 'it']. Default 'en'.
    :type lang: string

    :param boundary_type: Specifies the type of spatial search restriction. 
        One of ['rect','circle'].
    :type boundary_type: string

    :param rect: For boundary_type=rect only! Sets the restriction rectangle's
        minimum/maximum longitude/latitude, i.e. [MinLong,MinLat,MaxLong,Maxlat].
    :type rect: list of integers

    :param circle: For boundary_type=circle only! Sets the restriction circle 
        with a center point and a radius in meters, i.e. [Long,Lat,Radius]. 
    :type circle: list of integers

    :param limit: Specifies the maximum number of responses. Default 5.
    :type limit: integer
    dry_run
    :raises ValueError: When parameter has invalid value(s).

    :rtype: call to Client.request()
    """

    params = dict()

    if query:
        # Is not checked on backend
        if isinstance(query, dict):
            allowed_keys = ['address',
                            'neighbourhood',
                            'borough',
                            'locality',
                            'county',
                            'region',
                            'postalcode',
                            'country']
            if not all((key in allowed_keys) for key in query.keys()):
                raise ValueError("Geocoding query contains invalid admin parameter.")
        params["query"] = str(query)

    if lang:
        # Is not checked on backend
        if lang not in ['en', 'fr', 'de', 'it']:
            raise ValueError("Invalid language {} specified)".format(lang))
        params["lang"] = lang

    if boundary_type:
        params["boundary_type"] = boundary_type

    if rect:
        params["rect"] = convert._comma_list(rect)

    if circle:
        params["circle"] = convert._comma_list(circle)

    if limit:
        params["limit"] = str(limit)

    return client.request("/geocoding", params)


def reverse_geocode(client, location,
                    lang=None,
                    boundary_type=None,
                    rect=None,
                    circle=None,
                    limit=None,
                    dry_run=None):
    """
    Reverse geocoding is the process of converting geographic coordinates into a
    human-readable address.

    :param location: Coordinate to be inquired.
    :type location: lng/lat pair as list or tuple

    :param lang: Specifies the language of the response. One of ['de', 'en',
        'fr', 'it']. Default 'en'.
    :type lang: string

    :param boundary_type: Specifies the type of spatial search restriction. 
        One of ['rect','circle'].
    :type boundary_type: string

    :param rect: For boundary_type=rect only! Sets the restriction rectangle's
        minimum/maximum longitude/latitude, i.e. [MinLong,MinLat,MaxLong,Maxlat].
    :type rect: list of integers

    :param circle: For boundary_type=circle only! Sets the restriction circle 
        with a center point and a radius in meters, i.e. [Long,Lat,Radius]. 
    :type circle: list of integers

    :param limit: Specifies the maximum number of responses. Default 5.
    :type limit: integer
    
    :raises ValueError: When parameter has invalid value(s).

    :rtype: dict from JSON response
    """
    
    params = dict()

    # Check if latlng param is a place_id string.
    #  place_id strings do not contain commas; latlng strings do.
    if location:
        params["location"] = convert._comma_list(location)

    if lang:
        # Is not checked on backend
        if lang not in ['en', 'fr', 'de', 'it']:
            raise ValueError("Invalid language {} specified)".format(lang))
        params["lang"] = lang

    if boundary_type:
        params["boundary_type"] = boundary_type

    if rect:
        params["rect"] = convert._comma_list(rect)

    if circle:
        params["circle"] = convert._comma_list(circle)

    if limit:
        params["limit"] = str(limit)

    return client.request("/geocoding", params, dry_run=dry_run)
