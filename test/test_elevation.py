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

"""Tests for the distance matrix module."""
import responses
import test as _test

import openrouteservice
from test.test_helper import ENDPOINT_DICT

class ElevationTest(_test.TestCase):
    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key)
        self.coords = coords = [[13.331302, 38.108433],
                                [13.331273, 38.108493]]
        
    @responses.activate
    def test_line(self):
        query = ENDPOINT_DICT['elevation_line']
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/elevation/line',
                      json=query,
                      status=200,
                      content_type='application/json')

        resp = self.client.elevation_line(**query)

        self.assertEquals(len(responses.calls), 1)
        self.assertURLEqual('https://api.openrouteservice.org/elevation/line?api_key={}'.format(self.key),
                            responses.calls[0].request.url)
        self.assertEquals(responses.calls[0].response.json(), query)
        
    @responses.activate
    def test_point(self):
        query = ENDPOINT_DICT['elevation_point']
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/elevation/point',
                      json= query,
                      status=200,
                      content_type='application/json')
        
        resp = self.client.elevation_point(**query)
        
        self.assertEquals(len(responses.calls), 1)
        self.assertURLEqual('https://api.openrouteservice.org/elevation/point?api_key={}'.format(self.key),
                            responses.calls[0].request.url)        
        self.assertEquals(responses.calls[0].response.json(), query)
    