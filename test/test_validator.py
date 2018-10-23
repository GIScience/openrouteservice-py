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

"""Tests for the validator module."""

import responses

import openrouteservice
from openrouteservice import validator
import test as _test


class ValidatorTest(_test.TestCase):

    @responses.activate
    def test_directions_validation(self):
        params = {
            'coordinates': ((8.34234, 48.23424), (8.34423, 48.26424)),
            'profile': 'driving-hgv',
            'preference': 'best',
            'units': 'mi',
            'language': 'en',
            'geometry': 'true',
            'geometry_format': 'geojson',
            'geometry_simplify': 'false',
            'instructions': 'false',
            'instructions_format': 'html',
            'roundabout_exits': 'true',
            'attributeds': ['avgspeed'],
            'radiuses': [10000, 10000],
            'bearings': [[100, 100], [200, 200]],
            'elevation': 'true',
            'extra_info': ['steepness', 'suitability'],
            'optimized': 'true',
            'options': {'maximum_speed': '20'}
        }
        v = validator.validator(params, 'directions')
        self.assertEqual('unallowed value best', v.errors['preference'][0])
        self.assertEqual('unknown field', v.errors['attributeds'][0])
        self.assertEqual('must be of integer type', v.errors['options'][0]['maximum_speed'][0])
        self.assertEqual("depends on these values: {'optimized': 'false'}", v.errors['bearings'][0])

    @responses.activate
    def test_direction_correct_validation(self):
        params = {
            'coordinates': ((8.34234, 48.23424), (8.34423, 48.26424)),
            'profile': 'driving-hgv',
            'preference': 'fastest',
            'units': 'mi',
            'language': 'en',
            'geometry': 'true',
            'geometry_format': 'geojson',
            'geometry_simplify': 'false',
            'instructions': 'false',
            'instructions_format': 'html',
            'roundabout_exits': 'true',
            'attributes': ['avgspeed'],
            'radiuses': [10000, 10000],
            'bearings': [[100, 100], [200, 200]],
            'continue_straight': 'false',
            'elevation': 'true',
            'extra_info': ['steepness', 'suitability'],
            'optimized': 'false',
            'options': {'maximum_speed': 20}
        }
        v = validator.validator(params, 'directions')

    @responses.activate
    def test_isochrones_validation(self):
        params = {'locations': [[9.970093, 48.477473], [9.207916, 49.153868]],
                  'profile': 'cycling-reguläar',
                  'range_type': 'distance',
                  'range': [1000, 2000],
                  'units': 'm',
                  'location_type': 'destination',
                  'attributes': ['area', 'reachfactor'],
                  'interval': [30]
                  }
        v = validator.validator(params, "isochrones")

    @responses.activate
    def test_distance_matrix_validation(self):
        params = {'locations': [[9.970093, 48.477473], [9.207916, 49.153868], [37.573242, 55.801281],
                                [115.663757, 38.106467]],
                  'sources': [0, 1, 2],
                  'destinations': [1, 2, 3],
                  'profile': 'cycling-regular',
                  'metrics': ['duration', 'distance'],
                  'resolve_locations': 'tlrue',
                  'units': 'mi',
                  'optimized': 'false'}
        v = validator.validator(params, 'distance_matrix')
        # self.assertEqual()
        print(v.errors)

    @responses.activate
    def test_search_validation(self):
        params = {'text': 'Heidelberg',
                  'focus_point': (8.675786, 49.418431),
                  'rect_min_x': 8.573179,
                  'rect_min_y': 49.351764,
                  'rect_max_x': 8.79405,
                  'rect_max_y': 49.459693,
                  'circle_point': (8.675786, 49.418431),
                  'circle_radius': 50,
                  'sources': ['osm', 'wof', 'gn'],
                  'layers': ['locality', 'county', 'region'],
                  'country': 'de',
                  'size': 5,
                  }
        validator.search_validation(params)

    @responses.activate
    def test_structured_validation(self):
        params = {'address': 'Berliner Straße 45',
                  'neighbourhood': 'Neuenheimer Feld',
                  'borough': 'Heidelberg',
                  'locality': 'Heidelberg',
                  'county': 'Rhein-Neckar-Kreis',
                  'region': 'Baden-Württemberg',
                  'postalcode': '69120',
                  'country': 'de',
                  }
        validator.structured_validation(params)

    def test_reverse_validation(self):
        params = {'point': (8.675786, 49.418431),
                  'circle_radius': 50,
                  'sources': ['osm', 'wof', 'gn'],
                  'layers': ['locality', 'county', 'region'],
                  'country': 'de',
                  'size': 5,
                  }
        validator.reverse_validation(params)
