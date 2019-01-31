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
from test.test_helper import *

class DistanceMatrixTest(_test.TestCase):

    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key, base_url="http://129.206.5.136:8080/ors", requests_kwargs={'verify': False})
        self.valid_query = ENDPOINT_DICT['distance_matrix']

    @responses.activate
    def test_all_params(self):
        query = self.valid_query
        
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/v2/matrix/{}/json'.format(query['profile']),
                      json=query,
                      status=200,
                      content_type='application/json')

        #TODO: how does the API call work here?! Can I get the header from resp?
        resp = self.client.distance_matrix(**query)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/v2/matrix/{}/json'.format(query['profile']),
                            responses.calls[0].request.url)
        self.assertEqual(resp, self.valid_query)

    @responses.activate
    def test_tuple_parameter(self):
        query = self.valid_query
        query['locations'] = tuple([tuple(x) for x in PARAM_LINE])

        responses.add(responses.POST,
                      'https://api.openrouteservice.org/matrix',
                      json=query,
                      status=200,
                      content_type='application/json')

        resp = self.client.distance_matrix(**query)

        print(resp)
        print(responses.calls[0])

        self.assertEqual(resp, self.valid_query)
