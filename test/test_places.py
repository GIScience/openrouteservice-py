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

""" Tests for the places module."""

import responses

import openrouteservice
from openrouteservice.exceptions import ValidationError
import test as _test


class PlacesTest(_test.TestCase):

    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key)
        self.coord_valid = [8.8034, 53.0756]
        self.bbox_valid = [[8.8034, 53.0756], [8.7834, 53.0456]]
        self.coords_invalid = ((1, 2), (3, 4))

    @responses.activate
    def test_basic_params(self):
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/pois',
                      body='{"status":"OK","geometry":[]}',
                      status=200,
                      content_type='application/json')

        self.client.places(request='pois',
                           geojson=dict(type='Point', coordinates=self.coord_valid),
                           buffer=100)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/pois?api_key={}'.format(self.key),
                            responses.calls[0].request.url)

    @responses.activate
    def test_all_params(self):
        params = {'request': 'pois',
                  'bbox': self.bbox_valid,
                  'geojson': {'type': 'Point', 'coordinates': self.coord_valid},
                  'buffer': 100,
                  'limit': 900,
                  'filter_category_ids': [180, 245],
                  'filters_custom': {'wheelchair': ['yes'], 'smoking': ['dedicated'], 'fee': ['yes']},
                  'sortby': 'distance'}

        payload = {'request': 'pois',
                   'bbox': [[8.8034, 53.0756], [8.7834, 53.0456]],
                   'geojson': {'type': 'Point', 'coordinates': [8.8034, 53.0756]},
                   'buffer': 100,
                   'limit': 900,
                   'filter_category_ids': [180, 245],
                   'filters_custom': {'wheelchair': ['yes'], 'smoking': ['dedicated'], 'fee': ['yes']},
                   'sortby': 'distance'}

        responses.add(responses.POST,
                      'https://api.openrouteservice.org/pois',
                      json=params,
                      status=200,
                      content_type='application/json')

        resp = self.client.places(**params)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/pois?api_key={}'.format(self.key),
                            responses.calls[0].request.url)
        self.assertEqual(resp, payload)
