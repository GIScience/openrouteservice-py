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

"""Performs requests to the ORS elevation API."""


def elevation_point(client, format_in, geometry,
                    format_out='geojson',
                    dataset='srtm',
                    validate=True,
                    dry_run=None):
    """
    POSTs 2D point to be enriched with elevation.
    
    :param format_in: Format of input geometry. One of ['geojson',
        'point']
    :type format_in: string
    
    :param geometry: Point geometry 
    :type geometry: depending on format_in, either list of coordinates or Point geojson
    
    :param format_out: Format of output geometry, one of ['geojson', 'point']
    :type format_out: string
    
    :param dataset: Elevation dataset to be used. Currently only SRTM v4.1 available.
    :type dataset: string
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean
    
    :returns: correctly formatted parameters
    :rtype: Client.request()
    """

    params = {
        'format_in': format_in,
        'geometry': geometry,
        'format_out': format_out,
        'dataset': dataset
    }

    return client.request('/elevation/point', {}, post_json=params, dry_run=dry_run)


def elevation_line(client, format_in, geometry,
                   format_out='geojson',
                   dataset='srtm',
                   validate=True,
                   dry_run=None):
    """
    POSTs 2D point to be enriched with elevation.
    
    :param format_in: Format of input geometry. One of ['geojson',
        'polyline', 'encodedpolyline']
    :type format_in: string
    
    :param geometry: Point geometry 
    :type geometry: depending on format_in, either list of coordinates, LineString
        geojson or string
    
    :param format_out: Format of output geometry, one of ['geojson',
        'polyline', 'encodedpolyline']
    :type format_out: string
    
    :param dataset: Elevation dataset to be used. Currently only SRTM v4.1 available.
    :type dataset: string
    
    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean
    
    :returns: correctly formatted parameters
    :rtype: Client.request()
    """

    params = {
        'format_in': format_in,
        'geometry': geometry,
        'format_out': format_out,
        'dataset': dataset
    }

    return client.request('/elevation/line', {}, post_json=params, dry_run=dry_run)
