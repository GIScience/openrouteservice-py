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
from test.test_helper import PARAM_POINT, ENDPOINT_DICT


class IsochronesTest(_test.TestCase):

    @responses.activate
    def test_isochrones(self):
        query = ENDPOINT_DICT['isochrones']

        responses.add(responses.POST,
                      'https://api.openrouteservice.org/v2/isochrones/{}/geojson'.format(query['profile']),
                      json=query,
                      status=200,
                      content_type='application/json')

        resp = self.client.isochrones(**query)

        self.assertEqual(1, len(responses.calls))
        self.assertEqual(resp, query)
