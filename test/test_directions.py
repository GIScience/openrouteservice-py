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

"""Tests for the directions module."""

import responses

import openrouteservice
from openrouteservice.exceptions import ValidationError
import test as _test

class DirectionsTest(_test.TestCase):
            
    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key)
        self.coords_valid = ((8.34234,48.23424),(8.34423,48.26424))

    @responses.activate
    def test_simple_directions(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/directions',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')
        
        routes = self.client.directions(self.coords_valid)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/directions?'
                            'api_key={}&profile=driving-car&'
                            'coordinates=8.34234,48.23424|8.34423,48.26424&'
                            'optimized=true'.format(self.key),
                            responses.calls[0].request.url)        

    @responses.activate
    def test_bearings(self):
        # First: test correct output for bearings 
        # Second: should switch to optimized=false bcs bearings was specified
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/directions',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')
        
        # Simplest directions request. Driving directions by default.
        routes = self.client.directions(self.coords_valid,
                                        bearings=[[100,100],[200,200]])

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/directions?'
                            'api_key={}&coordinates=8.34234%2C48.23424%7C8.34423%2C48.26424&'
                            'profile=driving-car&bearings=100%2C100%7C200%2C200&optimized=false'.format(self.key),
                            responses.calls[0].request.url)

    @responses.activate
    def test_continue_straight(self):
        # Should switch to optimized=false bcs continue_straight is set true
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/directions',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')
        
        # Simplest directions request. Driving directions by default.
        routes = self.client.directions(self.coords_valid,
                                        profile='cycling-regular',
                                        continue_straight='true')

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/directions?'
                            'api_key={}&coordinates=8.34234%2C48.23424%7C8.34423%2C48.26424&'
                            'profile=cycling-regular&continue_straight=true&optimized=false'.format(self.key),
                            responses.calls[0].request.url)        

    @responses.activate
    def test_complex_request(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/directions',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')
        
        params = {
                'coordinates':self.coords_valid,
                'profile':'cycling-regular',
                'preference':'fastest',
                'units':'mi',
                'language':'en',
                'geometry':'true',
                'geometry_format':'geojson',
                'geometry_simplify':'false',
                'instructions':'false',
                'instructions_format':'html',
                'roundabout_exits':'true',
                'attributes':['avgspeed'],
                'radiuses':[10000,10000],
                'bearings':[[100,100], [200,200]],
                'continue_straight':'false',
                'elevation':'true',
                'extra_info':['steepness', 'suitability'],
                'optimized':'false',
                'options':{'maximum_speed':20}
                }

        print(params)
        routes = self.client.directions(**params)
                                        

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/directions?api_key={}&'
                            'coordinates=8.34234%2C48.23424%7C8.34423%2C48.26424&'
                            'profile=cycling-regular&preference=fastest&units=mi&'
                            'language=en&geometry=true&geometry_format=geojson&'
                            'geometry_simplify=false&instructions=false&'
                            'instructions_format=html&roundabout_exits=true'
                            '&attributes=avgspeed'
                            '&radiuses=10000%7C10000&bearings=100%2C100%7C200%2C200&'
                            'continue_straight=false&elevation=true&'
                            'extra_info=steepness%7Csuitability&optimized=false&'
                            'options=%7B%22maximum_speed%22%3A+20%7D'.format(self.key),
                            responses.calls[0].request.url)
