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

from test.test_helper import ENDPOINT_DICT


class ElevationTest(_test.TestCase):
    valid_query = ENDPOINT_DICT['elevation_line']

    @responses.activate
    def test_elevation_line(self):
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/elevation/line',
                      json=self.valid_query,
                      status=200,
                      content_type='application/json')

        resp = self.client.elevation_line(**self.valid_query)

        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(resp, self.valid_query)

    @responses.activate
    def test_elevation_point(self):
        query = ENDPOINT_DICT['elevation_point']
        responses.add(responses.POST,
                      'https://api.openrouteservice.org/elevation/point',
                      json=self.valid_query,
                      status=200,
                      content_type='application/json')

        resp = self.client.elevation_point(**query)

        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(resp, self.valid_query)
