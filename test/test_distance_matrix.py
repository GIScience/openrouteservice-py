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

from test.test_helper import ENDPOINT_DICT, PARAM_LINE


class DistanceMatrixTest(_test.TestCase):
    valid_query = ENDPOINT_DICT['distance_matrix']

    @responses.activate
    def test_matrix(self):
        query = self.valid_query.copy()
        query['locations'] = tuple([tuple(x) for x in PARAM_LINE])

        responses.add(responses.POST,
                      'https://api.openrouteservice.org/v2/matrix/{}/json'.format(query['profile']),
                      json=query,
                      status=200,
                      content_type='application/json')

        resp = self.client.distance_matrix(**query)
        self.assertEqual(resp, self.valid_query)
