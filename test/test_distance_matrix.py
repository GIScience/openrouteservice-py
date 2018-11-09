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
#

"""Tests for the distance matrix module."""
import responses
import test as _test

import openrouteservice

class DistanceMatrixTest(_test.TestCase):

    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key)
        self.coords_valid = [[9.970093,48.477473],
                            [9.207916,49.153868],
                            [37.573242,55.801281],
                            [115.663757,38.106467]]
            
    @responses.activate
    def test_basic_params(self):
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/matrix',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')

        origins = 'all'
        destinations = 'all'
        
        self.client.distance_matrix(self.coords_valid,
                                     sources=origins,
                                     destinations=destinations)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/matrix?api_key={}&profile=driving-car'.format(self.key),
                            responses.calls[0].request.url)

    @responses.activate
    def test_all_params(self):

        origins = [0,1,2]
        destinations = [1,2,3]
        
        query = {'locations': self.coords_valid,
                 'sources': origins,
                 'destinations': destinations,
                 'profile': 'cycling-regular',
                 'metrics': ['duration', 'distance'],
                 'resolve_locations': 'true',
                 'units': 'mi',
                 'optimized': 'false'
                }
        
        payload = {'locations': [[9.970093, 48.477473], [9.207916, 49.153868], [37.573242, 55.801281], [115.663757, 38.106467]],
                   'sources': [0, 1, 2],
                   'destinations': [1, 2, 3],
                   'profile': 'cycling-regular',
                   'metrics': ['duration', 'distance'], 
                   'resolve_locations': 'true',
                   'units': 'mi',
                   'optimized': 'false'}
        
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/matrix',
                      json=query,
                      status=200,
                      content_type='application/json')
        
        resp = self.client.distance_matrix(**query)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/matrix?api_key={}&profile=cycling-regular'.format(self.key),
                            responses.calls[0].request.url)
        self.assertEqual(resp, payload)
