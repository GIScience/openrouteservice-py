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
from test.test_helper import ENDPOINT_DICT


class GeocodingPeliasTest(_test.TestCase):
    search = ENDPOINT_DICT['pelias_search']
    autocomplete = ENDPOINT_DICT['pelias_autocomplete']
    structured = ENDPOINT_DICT['pelias_structured']
    reverse = ENDPOINT_DICT['pelias_reverse']

    @responses.activate
    def test_pelias_search(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/search',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_search(**self.search)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/search?boundary.circle.lat=48.23424&boundary.circle.lon=8.34234&boundary.circle.radius=50&boundary.country=de&boundary.rect.max_lat=501&boundary.rect.max_lon=501&boundary.rect.min_lat=500&boundary.rect.min_lon=500&focus.point.lat=48.23424&focus.point.lon=8.34234&layers=locality%2Ccounty%2Cregion&size=50&sources=osm%2Cwof%2Cgn&text=Heidelberg',
            responses.calls[0].request.url)

    @responses.activate
    def test_pelias_autocomplete(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/autocomplete',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_autocomplete(**self.autocomplete)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/autocomplete?boundary.country=de&boundary.rect.max_lon%09=500&boundary.rect.min_lat%09=500&boundary.rect.min_lon%09=500&focus.point.lat=48.23424&focus.point.lon=8.34234&layers=locality%2Ccounty%2Cregion&sources=osm%2Cwof%2Cgn&text=Heidelberg',
            responses.calls[0].request.url)

    @responses.activate
    def test_pelias_structured(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/search/structured',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_structured(**self.structured)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/search/structured?address=Berliner+Stra%C3%9Fe+45&borough=Heidelberg&country=de&county=Rhein-Neckar-Kreis&locality=Heidelberg&neighbourhood=Neuenheimer+Feld&postalcode=69120&region=Baden-W%C3%BCrttemberg',
            responses.calls[0].request.url)

    @responses.activate
    def test_pelias_reverse(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocode/reverse',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.pelias_reverse(**self.reverse)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual(
            'https://api.openrouteservice.org/geocode/reverse?boundary.circle.radius=50&boundary.country=de&layers=locality%2Ccounty%2Cregion&point.lat=48.23424&point.lon=8.34234&size=50&sources=osm%2Cwof%2Cgn',
            responses.calls[0].request.url)
