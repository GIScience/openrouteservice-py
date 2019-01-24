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
#

"""Tests for the distance matrix module."""
import responses
import test as _test

import openrouteservice


class IsochronesTest(_test.TestCase):

    def setUp(self):
        self.key = 'sample_key'
        self.client = openrouteservice.Client(self.key)
        self.coords_valid = [[9.970093, 48.477473],
                             [9.207916, 49.153868],
                             [37.573242, 55.801281],
                             [115.663757, 38.106467],
                             [8.34234, 48.23424]]

    @responses.activate
    def test_basic_params(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/isochrones',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')

        isochrone = self.client.isochrones(self.coords_valid[0],
                                           intervals=[60])

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/isochrones?api_key={}&'
                            'locations=9.970093%2C48.477473&'
                            'profile=driving-car&range=60&range_type=time'.format(self.key),
                            responses.calls[0].request.url)

    @responses.activate
    def test_all_params(self):
        responses.add(responses.GET,
                      'https://api.openrouteservice.org/isochrones',
                      body='{"status":"OK","routes":[]}',
                      status=200,
                      content_type='application/json')

        isochrone = self.client.isochrones(self.coords_valid,
                                           profile='cycling-regular',
                                           range_type='distance',
                                           intervals=[1000, 2000],
                                           units='m',
                                           location_type='destination',
                                           smoothing=0.5,
                                           attributes=['area', 'reachfactor']
                                           )

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.openrouteservice.org/isochrones?api_key={}&'
                            'locations=9.970093%2C48.477473%7C9.207916'
                            '%2C49.153868%7C37.573242%2C55.801281%7C115.663757'
                            '%2C38.106467%7C8.34234%2C48.23424&profile=cycling-regular&'
                            'range_type=distance&range=1000%2C2000&'
                            'units=m&location_type=destination&'
                            'smoothing=0.5&'
                            'attributes=area|reachfactor'.format(self.key),
                            responses.calls[0].request.url)
