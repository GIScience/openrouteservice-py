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
import test as _test

class ClientTest(_test.TestCase):
    
    def setUp(self):
        self.key = 'sample_key'
        self.query = 'Heidelberg'
        self.coords_valid = ((8.34234,48.23424),(8.34423,48.26424))

    def test_no_api_key(self):
        with self.assertRaises(Exception):
            client = openrouteservice.Client()
            client.directions(self.coords_valid)

    def test_invalid_api_key(self):
        with self.assertRaises(Exception):
            client = openrouteservice.Client(key="Invalid key.")
            client.directions(self.coords_valid)

    def test_urlencode(self):
        encoded_params = openrouteservice.client._urlencode_params([("address", "=Sydney ~")])
        self.assertEqual("address=%3DSydney+~", encoded_params)
        
    @responses.activate
    def test_queries_per_minute_sleep_function(self):
        # This test assumes that the time to run a mocked query is
        # relatively small, eg a few milliseconds. We define a rate of
        # 3 queries per second, and run double that, which should take at
        # least 1 minute but no more than 2.
        queries_per_minute = 2
        query_range = range(queries_per_minute * 2)
        
        for _ in query_range:
            responses.add(responses.GET,
                          'https://api.openrouteservice.org/directions',
                          body='{"status":"OK","results":[]}',
                          status=200,
                          content_type='application/json')
            
        client = openrouteservice.Client(key=self.key,
                                   queries_per_minute=queries_per_minute)
        start = time.time()
        for idx, _ in enumerate(query_range):
            client.directions(self.coords_valid)
        end = time.time()
        self.assertTrue(start + 60 < end < start + 120)
        
    # def test_overquerylimit_error(self):
    #     # Assume more queries_per_minute than allowed by API policy and
    #     # don't allow retries if API throws 'rate exceeded' error, which
    #     # should be caught.
    #     queries_per_minute = 110
    #     query_range = range(queries_per_minute * 2)
    #
    #     client = openrouteservice.Client(key='5b3ce3597851110001cf624870cf2f2a58d44c718542b3088221b684',
    #                                queries_per_minute=queries_per_minute,
    #                                retry_over_query_limit=False)
    #
    #     with self.assertRaises(openrouteservice.exceptions._OverQueryLimit):
    #         for _ in query_range:
    #             client.directions(self.coords_valid)

    @responses.activate
    def test_raise_timeout_retriable_requests(self):
        # Mock query gives 503 as HTTP status, code should try a few times to 
        # request the same and then fail on Timout() error.
        retry_timeout = 3
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/directions',
                      body='{"status":"OK","results":[]}',
                      status=503,
                      content_type='application/json')
            
        client = openrouteservice.Client(key=self.key, 
                                         retry_timeout=retry_timeout)
        
        start = time.time()
        with self.assertRaises(openrouteservice.exceptions.Timeout):
            client.directions(self.coords_valid)
        end = time.time()
        self.assertTrue(retry_timeout < end-start < 2 * retry_timeout)

    @responses.activate
    def test_host_override_with_parameters(self):
        # Test if it's possible to override host for individual hosting.
        responses.add(responses.GET,
                      "https://foo.com/bar",
                      body='{"status":"OK","results":[]}',
                      status=200,
                      content_type="application/json")

        client = openrouteservice.Client(base_url="https://foo.com")
        client.request("/bar", {'bunny':'pretty', 'fox':'prettier'})
        
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
        
        client = openrouteservice.Client(key=self.key)
        req = client.request(params={'format_out': 'geojson'},
                             url='directions/',
                             dry_run='true')
        
        self.assertEqual(0, len(responses.calls))