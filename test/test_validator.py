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

params = {
    # 'coordinates': ((8.34234, 48.23424), (8.34423, 48.26424)),
    'profile': 'foot-walking',
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
    'continue_straight': 'true',
    'elevation': 'true',
    'extra_info': ['steepness', 'suitability'],
    'optimized': 'false',
    'options': {'maximum_speed': 20}}


class ValidatorTest(_test.TestCase):

    def setUp(self):
        self.coords_point = (8.34234, 48.23424)
        self.coords_linestring = ((8.34234, 48.23424), (8.34423, 48.26424))

    def test_directions_correct_schema(self):
        params['coordinates'] = self.coords_linestring
        v = validator.validator(params, 'directions', 2)
        self.assertEqual(0, len(v.errors))

    def test_directions_wrong_schema(self):
        params['coordinates'] = self.coords_linestring
        params['preference'] = 'best'
        params['attributeds'] = ['avgspeed']
        params['optimized'] = 'true'
        params['radiuses'] = [10000, 10000, 10000, 10000]
        params['bearings'] = [[100, 100], [200, 200]]
        params['options'] = {'maximum_speed': '20'}

        v = validator.validator(params, 'directions', 2)
        self.assertEqual('unallowed value best', v.errors['preference'][0])
        self.assertEqual('unknown field', v.errors['attributeds'][0])
        self.assertEqual('max length is 2', v.errors['radiuses'][0])
        self.assertEqual("depends on these values: {'optimized': 'false'}", v.errors['bearings'][0])
        self.assertEqual('must be of integer type', v.errors['options'][0]['maximum_speed'][0])

    def test_isochrones_wrong_schema(self):
        params = {'locations': self.coords_linestring,
                  'profile': 'cycling-reguläar',
                  'range_type': 'distance',
                  'range': [1000, 2000],
                  'units': 'm',
                  'location_type': 'destination',
                  'attributes': ['area', 'reachfactor'],
                  'interval': [30]
                  }
        v = validator.validator(params, "isochrones")
        print(v.errors)

    def test_distance_matrix_wrong_schema(self):
        params = {'locations': self.coords_linestring,
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

    def test_search_wrong_schema(self):
        params = {'text': 'Heidelberg',
                  'focus_point': self.coords_point,
                  'rect_min_x': 8.573179,
                  'rect_min_y': 49.351764,
                  'rect_max_x': 8.79405,
                  'rect_max_y': 49.459693,
                  'circle_point': self.coords_point,
                  'circle_radius': 50,
                  'sources': ['osm', 'wof', 'gn'],
                  'layers': ['locality', 'coddunty', 'region'],
                  'country': 'de',
                  'size': 5,
                  }
        # validator.search_validation(params)
        v = validator.validator(params, 'search')
        # self.assertEqual()
        print(v.errors)

    def test_structured_wrong_schema(self):
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

    def test_reverse_wrong_schema(self):
        params = {'point': self.coords_point,
                  'circle_radius': 50,
                  'sources': ['osm', 'wof', 'gn'],
                  'layers': ['locality', 'county', 'region'],
                  'country': 'de',
                  'size': 5,
                  }
        validator.reverse_validation(params)
