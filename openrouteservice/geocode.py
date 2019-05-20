# -*- coding: utf-8 -*-
# Copyright (C) 2018 HeiGIT, University of Heidelberg.
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

"""Performs requests to the ORS geocode API (direct Pelias clone)."""
from openrouteservice import convert


def pelias_search(client, text,
                  focus_point=None,
                  rect_min_x=None,
                  rect_min_y=None,
                  rect_max_x=None,
                  rect_max_y=None,
                  circle_point=None,
                  circle_radius=None,
                  sources=None,
                  layers=None,
                  country=None,
                  size=None,
                  validate=True,
                  dry_run=None):
    """
    Geocoding is the process of converting addresses into geographic
    coordinates.

    This endpoint queries directly against a Pelias instance.

    :param text: Full-text query against search endpoint. Required.
    :type text: string

    :param focus_point: Focusses the search to be around this point and gives
        results within a 100 km radius higher scores.
    :type query: list or tuple of (Long, Lat)

    :param rect_min_x: Min longitude by which to constrain request geographically.
    :type rect_min_x: float

    :param rect_min_y: Min latitude by which to constrain request geographically.
    :type rect_min_y: float

    :param rect_max_x: Max longitude by which to constrain request geographically.
    :type rect_max_x: float

    :param rect_max_y: Max latitude by which to constrain request geographically.
    :type rect_max_y: float

    :param circle_point: Geographical constraint in form a circle.
    :type circle_point: list or tuple of (Long, Lat)

    :param circle_radius: Radius of circle constraint in km. Default 50.
    :type circle_radius: integer

    :param sources: The originating source of the data. One or more of
        ['osm', 'oa', 'wof', 'gn']. Currently only 'osm', 'wof' and 'gn' are
        supported.
    :type sources: list of strings

    :param layers: The administrative hierarchy level for the query. Refer to
        https://github.com/pelias/documentation/blob/master/search.md#filter-by-data-type
        for details.
    :type layers: list of strings

    :param country: Constrain query by country. Accepts a alpha-2 or alpha-3
        digit ISO-3166 country code.
    :type country: str

    :param size: The amount of results returned. Default 10.
    :type size: integer
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean

    :raises ValueError: When parameter has invalid value(s).
    :raises TypeError: When parameter is of the wrong type.

    :rtype: call to Client.request()
    """

    params = {'text': text}

    if focus_point:
        params['focus.point.lon'] = convert._format_float(focus_point[0])
        params['focus.point.lat'] = convert._format_float(focus_point[1])

    if rect_min_x:
        params['boundary.rect.min_lon'] = convert._format_float(rect_min_x)  #

    if rect_min_y:
        params['boundary.rect.min_lat'] = convert._format_float(rect_min_y)  #

    if rect_max_x:
        params['boundary.rect.max_lon'] = convert._format_float(rect_max_x)  #

    if rect_max_y:
        params['boundary.rect.max_lat'] = convert._format_float(rect_max_y)  #

    if circle_point:
        params['boundary.circle.lon'] = convert._format_float(circle_point[0])  #
        params['boundary.circle.lat'] = convert._format_float(circle_point[1])  #

    if circle_radius:
        params['boundary.circle.radius'] = circle_radius

    if sources:
        params['sources'] = convert._comma_list(sources)

    if layers:
        params['layers'] = convert._comma_list(layers)

    if country:
        params['boundary.country'] = country

    if size:
        params['size'] = size

    return client.request("/geocode/search", params, dry_run=dry_run)


def pelias_autocomplete(client, text,
                        focus_point=None,
                        rect_min_x=None,
                        rect_min_y=None,
                        rect_max_x=None,
                        rect_max_y=None,
                        country=None,
                        sources=None,
                        layers=None,
                        validate=True,
                        dry_run=None):
    """
    Autocomplete geocoding can be used alongside /search to enable real-time feedback.
    It represents a type-ahead functionality, which helps to find the desired location,
    without to require a fully specified search term.

    This endpoint queries directly against a Pelias instance.
    For fully documentation, please see https://github.com/pelias/documentation/blob/master/autocomplete.md

    :param text: Full-text query against search endpoint. Required.
    :type text: string

    :param focus_point: Focusses the search to be around this point and gives
        results within a 100 km radius higher scores.
    :type query: list or tuple of (Long, Lat)

    :param rect_min_x: Min longitude by which to constrain request geographically.
    :type rect_min_x: float

    :param rect_min_y: Min latitude by which to constrain request geographically.
    :type rect_min_y: float

    :param rect_max_x: Max longitude by which to constrain request geographically.
    :type rect_max_x: float

    :param rect_max_y: Max latitude by which to constrain request geographically.
    :type rect_max_y: float

    :param country: Constrain query by country. Accepts a alpha-2 or alpha-3
        digit ISO-3166 country codes.
    :type country: str

    :param sources: The originating source of the data. One or more of
        ['osm', 'oa', 'wof', 'gn']. Currently only 'osm', 'wof' and 'gn' are
        supported.
    :type sources: list of strings

    :param layers: The administrative hierarchy level for the query. Refer to
        https://github.com/pelias/documentation/blob/master/search.md#filter-by-data-type
        for details.
    :type layers: list of strings
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean

    :raises ValueError: When parameter has invalid value(s).
    :raises TypeError: When parameter is of the wrong type.

    :rtype: dict from JSON response
    """

    params = {'text': text}

    if focus_point:
        params['focus.point.lon'] = convert._format_float(focus_point[0])
        params['focus.point.lat'] = convert._format_float(focus_point[1])

    if rect_min_x:
        params['boundary.rect.min_lon	'] = convert._format_float(rect_min_x)

    if rect_min_y:
        params['boundary.rect.min_lat	'] = convert._format_float(rect_min_y)

    if rect_max_x:
        params['boundary.rect.max_lon	'] = convert._format_float(rect_max_x)

    if rect_max_y:
        params['boundary.rect.max_lon	'] = convert._format_float(rect_max_y)

    if country:
        params['boundary.country'] = country

    if sources:
        params['sources'] = convert._comma_list(sources)

    if layers:
        params['layers'] = convert._comma_list(layers)

    return client.request("/geocode/autocomplete", params, dry_run=dry_run)


def pelias_structured(client,
                      address=None,
                      neighbourhood=None,
                      borough=None,
                      locality=None,
                      county=None,
                      region=None,
                      postalcode=None,
                      country=None,
                      validate=True,
                      dry_run=None,
                      # size=None
                      ):
    """
    With structured geocoding, you can search for the individual parts of a location.
    Structured geocoding is an option on the search endpoint,
    which allows you to define a query that maintains the individual fields.

    This endpoint queries directly against a Pelias instance.
    For full documentation, please see https://github.com/pelias/documentation/blob/master/structured-geocoding.md

    :param address: Can contain a full address with house number or only a street name.
    :type address: string

    :param neighbourhood: Neighbourhoods are vernacular geographic entities that
        may not necessarily be official administrative divisions but are important nonetheless.
    :type neighbourhood: string

    # Check all passed arguments
    convert._is_valid_args(locals())

    :param borough: Mostly known in the context of New York City, even though they may exist in other cities.
    :type borough: string

    :param locality: Localities are equivalent to what are commonly referred to as cities.
    :type locality: string

    :param county: Administrative divisions between localities and regions.
        Not as commonly used in geocoding as localities, but useful when attempting to
        disambiguate between localities.
    :type county: string

    :param region: Normally the first-level administrative divisions within countries, analogous to states
        and provinces in the United States and Canada. Can be a full name or abbreviation.
    :type region: string

    :param postalcode: Dictated by an administrative division, which is almost always countries.
        Postal codes are unique within a country.
    :type postalcode: integer

    :param country: Highest-level divisions supported in a search. Can be a full name or abbreviation.
    :type country: string
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean

    :raises TypeError: When parameter is of the wrong type.

    :rtype: dict from JSON response
    """

    params = dict()

    if address:
        params['address'] = address

    if neighbourhood:
        params['neighbourhood'] = neighbourhood

    if borough:
        params['borough'] = borough

    if locality:
        params['locality'] = locality

    if county:
        params['county'] = county

    if region:
        params['region'] = region

    if postalcode:
        params['postalcode'] = postalcode

    if country:
        params['country'] = country

    return client.request("/geocode/search/structured", params, dry_run=dry_run)


def pelias_reverse(client, point,
                   circle_radius=None,
                   sources=None,
                   layers=None,
                   country=None,
                   size=None,
                   validate=True,
                   dry_run=None):
    """
    Reverse geocoding is the process of converting geographic coordinates into a
    human-readable address.

    This endpoint queries directly against a Pelias instance.

    :param point: Coordinate tuple. Required.
    :type point: list or tuple of [Lon, Lat]

    :param circle_radius: Radius around point to limit query in km. Default 1.
    :type circle_radius: integer

    :param sources: The originating source of the data. One or more of
        ['osm', 'oa', 'wof', 'gn']. Currently only 'osm', 'wof' and 'gn' are
        supported.
    :type sources: list of strings

    :param layers: The administrative hierarchy level for the query. Refer to
        https://github.com/pelias/documentation/blob/master/search.md#filter-by-data-type
        for details.
    :type layers: list of strings

    :param country: Constrain query by country. Accepts a alpha-2 or alpha-3
        digit ISO-3166 country codes.
    :type country: str

    :param size: The amount of results returned. Default 10.
    :type size: integer
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean

    :raises ValueError: When parameter has invalid value(s).

    :rtype: dict from JSON response
    """

    params = dict()

    params['point.lon'] = convert._format_float(point[0])
    params['point.lat'] = convert._format_float(point[1])

    if circle_radius:
        params['boundary.circle.radius'] = str(circle_radius)

    if sources:
        params['sources'] = convert._comma_list(sources)

    if layers:
        params['layers'] = convert._comma_list(layers)

    if country:
        params['boundary.country'] = country

    if size:
        params['size'] = size

    return client.request("/geocode/reverse", params, dry_run=dry_run)
