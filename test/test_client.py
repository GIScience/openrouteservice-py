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


"""Tests for client module."""

import responses
import time

import openrouteservice
from test.test_helper import *
import test as _test


class ClientTest(_test.TestCase):

    def test_no_api_key(self):
        with self.assertRaises(ValueError):
            client = openrouteservice.Client()
            client.directions(PARAM_LINE)

    def test_invalid_api_key(self):
        with self.assertRaises(openrouteservice.exceptions.ApiError):
            client = openrouteservice.Client(key="Invalid key.")
            client.directions(PARAM_LINE)

    def test_urlencode(self):
        encoded_params = openrouteservice.client._urlencode_params([("address", "=Sydney ~")])
        self.assertEqual("address=%3DSydney+~", encoded_params)

    @responses.activate
    def test_raise_over_query_limit(self):
        valid_query = ENDPOINT_DICT['directions']
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/v2/directions/{}/geojson'.format(valid_query['profile']),
                      json=valid_query,
                      status=429,
                      content_type='application/json')

        with self.assertRaises(openrouteservice.exceptions._OverQueryLimit):
            client = openrouteservice.Client(key=self.key, retry_over_query_limit=False)
            client.directions(**valid_query)

        with self.assertRaises(openrouteservice.exceptions.Timeout):
            client = openrouteservice.Client(key=self.key, retry_over_query_limit=True, retry_timeout=3)
            client.directions(**valid_query)

    @responses.activate
    def test_raise_timeout_retriable_requests(self):
        # Mock query gives 503 as HTTP status, code should try a few times to 
        # request the same and then fail on Timout() error.
        retry_timeout = 3
        valid_query = ENDPOINT_DICT['directions']
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/v2/directions/{}/geojson'.format(valid_query['profile']),
                      json=valid_query,
                      status=503,
                      content_type='application/json')

        client = openrouteservice.Client(key=self.key,
                                         retry_timeout=retry_timeout)

        start = time.time()
        with self.assertRaises(openrouteservice.exceptions.Timeout):
            client.directions(**valid_query)
        end = time.time()
        self.assertTrue(retry_timeout < end - start < 2 * retry_timeout)

    @responses.activate
    def test_host_override_with_parameters(self):
        # Test if it's possible to override host for individual hosting.
        responses.add(responses.GET,
                      "https://foo.com/bar",
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type="application/json")

        client = openrouteservice.Client(base_url="https://foo.com")
        client.request("/bar", {'bunny': 'pretty', 'fox': 'prettier'})

        self.assertURLEqual("https://foo.com/bar?bunny=pretty&fox=prettier",
                            responses.calls[0].request.url)
        self.assertEqual(1, len(responses.calls))

    @responses.activate
    def test_dry_run(self):
        # Test that nothing is requested when dry_run is 'true'

        responses.add(responses.GET,
                      'https://api.openrouteservice.org/directions',
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type='application/json')

        req = self.client.request(get_params={'format_out': 'geojson'},
                                  url='directions/',
                                  dry_run='true')

        self.assertEqual(0, len(responses.calls))

    @responses.activate
    def test_key_in_header(self):
        # Test that API key is being put in the Authorization header
        query = ENDPOINT_DICT['directions']

        responses.add(responses.POST,
                      'https://api.openrouteservice.org/v2/directions/{}/geojson'.format(query['profile']),
                      json=ENDPOINT_DICT['directions'],
                      status=200,
                      content_type='application/json')

        resp = self.client.directions(**query)

        self.assertDictContainsSubset({'Authorization': self.key}, responses.calls[0].request.headers)
