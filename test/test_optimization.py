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
from copy import deepcopy
import json

from test.test_helper import *
from openrouteservice.optimization import Job, Vehicle


class OptimizationTest(_test.TestCase):

    def _get_params(self):
        jobs, vehicles = list(), list()

        for idx, coord in enumerate(PARAM_LINE):
            jobs.append(Job(idx, location=coord,
                             service=PARAM_INT_BIG,
                             location_index=idx,
                             amount=[PARAM_INT_SMALL],
                             skills=PARAM_LIST_ONE,
                             time_windows=[PARAM_LIST_ONE]
                             ))

            vehicles.append(Vehicle(idx, profile='driving-car',
                                     start=coord,
                                     start_index=idx,
                                     end=coord,
                                     end_index=idx,
                                     capacity=[PARAM_INT_SMALL],
                                     skills=PARAM_LIST_ONE,
                                     time_window=PARAM_LIST_ONE))
        return jobs, vehicles

    def test_jobs_vehicles_classes(self):

        jobs, vehicles = self._get_params()

        self.assertEqual(ENDPOINT_DICT['optimization']['jobs'], [j.__dict__ for j in jobs])
        self.assertEqual(ENDPOINT_DICT['optimization']['vehicles'], [v.__dict__ for v in vehicles])

    @responses.activate
    def test_full_optimization(self):
        query = deepcopy(ENDPOINT_DICT['optimization'])

        jobs, vehicles = self._get_params()

        responses.add(responses.POST,
                      'https://api.openrouteservice.org/optimization',
                      json={},
                      status=200,
                      content_type='application/json')

        self.client.optimization(jobs, vehicles, geometry=False, matrix=PARAM_LIST_TWO)

        self.assertEqual(query, json.loads(responses.calls[0].request.body.decode('utf-8')))
