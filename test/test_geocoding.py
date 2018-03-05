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

"""Tests for the geocoding module."""

import responses

import test as _test
import unittest
import openrouteservice
from collections import OrderedDict

class GeocodingTest(_test.TestCase):
    
    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key)
        self.query = 'Heidelberg'
        self.location = (8.68353,49.412623)
        self.structured = {"postalcode": "69120",
                            "country":"Germany",
                            "locality": "Heidelberg",
                            }

    @responses.activate
    def test_simple_geocode(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocoding',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.geocode(self.query)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/geocoding?'
                            'api_key={}&query=Heidelberg'.format(self.key),
                            responses.calls[0].request.url)
#
    @responses.activate
    def test_reverse_geocode(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/geocoding',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        results = self.client.reverse_geocode(self.location)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/geocoding?'
                            'api_key={}&location=8.68353%2C49.412623'.format(self.key),
                            responses.calls[0].request.url)

    def test_geocode_structured_query(self):
        with self.assertRaises(ValueError):
            self.structured['Apartment'] = 'Below Bridge No 5'
            self.client.geocode(self.structured)
