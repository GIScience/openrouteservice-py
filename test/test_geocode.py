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


"""Tests for the Pelias geocoding module."""

import responses

import test as _test
import unittest
import openrouteservice
from collections import OrderedDict


class GeocodingPeliasTest(_test.TestCase):
    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key)
        self.search = {'text': 'Heidelberg',
                       'focus_point': (8.675786, 49.418431),
                       'rect_min_x': 8.573179,
                       'rect_min_y': 49.351764,
                       'rect_max_x': 8.79405,
                       'rect_max_y': 49.459693,
                       'circle_point': (8.675786, 49.418431),
                       'circle_radius': 50,
                       'sources': ['osm', 'wof', 'gn'],
                       'layers': ['locality', 'county', 'region'],
                       'country': 'de',
                       'size': 5,
                       }
        self.autocomplete = {'text': 'Heidelberg',
                             'focus_point': (8.675786, 49.418431),
                             'rect_min_x': 8.573179,
                             'rect_min_y': 49.351764,
                             'rect_max_x': 8.79405,
                             'rect_max_y': 49.459693,
                             'sources': ['osm', 'wof', 'gn'],
                             'layers': ['locality', 'county', 'region'],
                             'country': 'de',
                             }
        self.structured = {'address': 'Berliner Straße 45',
                           'neighbourhood': 'Neuenheimer Feld',
                           'borough': 'Heidelberg',
                           'locality': 'Heidelberg',
                           'county': 'Rhein-Neckar-Kreis',
                           'region': 'Baden-Württemberg',
                           'postalcode': 69120,
                           'country': 'de',
                           }
        self.reverse = {'point': (8.675786, 49.418431),
                        'circle_radius': 50,
                        'sources': ['osm', 'wof', 'gn'],
                        'layers': ['locality', 'county', 'region'],
                        'country': 'de',
                        'size': 5,
                        }

    @responses.activate
    def test_full_search(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/search',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_search(**self.search)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/search?boundary.circle.lat=49.418431&boundary.circle.lon=8.675786&boundary.circle.radius=50&boundary.rect.max_lon=8.79405&boundary.rect.max_lat=49.459693&boundary.rect.min_lat=49.351764&boundary.rect.min_lon=8.573179&boundary.country=de&focus.point.lat=49.418431&focus.point.lon=8.675786&layers=locality%2Ccounty%2Cregion&size=5&sources=osm%2Cwof%2Cgn&text=Heidelberg&api_key=sample_key'.format(
                self.key),
            responses.calls[0].request.url)

    @responses.activate
    def test_full_autocomplete(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/autocomplete',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_autocomplete(**self.autocomplete)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/autocomplete?boundary.rect.max_lon%09=49.459693&boundary.rect.min_lat%09=49.351764&boundary.rect.min_lon%09=8.573179&boundary.country=de&focus.point.lat=49.418431&focus.point.lon=8.675786&layers=locality%2Ccounty%2Cregion&sources=osm%2Cwof%2Cgn&text=Heidelberg&api_key=sample_key'.format(
                self.key),
            responses.calls[0].request.url)

    @responses.activate
    def test_full_structured(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/search/structured',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_structured(**self.structured)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/search/structured?address=Berliner%20Straße%2045&neighbourhood=Neuenheimer%20Feld&borough=Heidelberg&locality=Heidelberg&county=Rhein-Neckar-Kreis&region=Baden-Württemberg&postalcode=69120&country=de&api_key=sample_key'.format(
                self.key),
            responses.calls[0].request.url)

    @responses.activate
    def test_full_reverse(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/reverse',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_reverse(**self.reverse)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/reverse?boundary.circle.radius=50&boundary.country=de&layers=locality%2Ccounty%2Cregion&point.lat=49.418431&point.lon=8.675786&size=5&sources=osm%2Cwof%2Cgn&api_key=sample_key'.format(
                self.key),
            responses.calls[0].request.url)
