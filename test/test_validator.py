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

from openrouteservice import validator, exceptions
import test as _test

params = {'profile': 'foot-walking',
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

params_isochrones = {'profile': 'cycling-regular',
                     'range_type': 'distance',
                     'intervals': [1000, 2000],
                     'units': 'm',
                     'location_type': 'destination',
                     'attributes': ['area', 'reachfactor'],
                     'segments': 30}

params_matrix = {'sources': [0, 1, 2],
                 'destinations': [1, 2, 3],
                 'profile': 'cycling-regular',
                 'metrics': ['duration', 'distance'],
                 'resolve_locations': 'true',
                 'units': 'mi',
                 'optimized': 'false'}

params_search = {'text': 'Heidelberg',
                 'rect_min_x': 8.573179,
                 'rect_min_y': 49.351764,
                 'rect_max_x': 8.79405,
                 'rect_max_y': 49.459693,
                 'circle_point': (8.675786, 49.418431),
                 'circle_radius': 50,
                 'sources': ['osm', 'wof', 'gn'],
                 'layers': ['locality', 'county', 'region'],
                 'country': 'de',
                 'size': 5}

params_structured = {'address': 'Berliner Straße 45',
                     'neighbourhood': 'Neuenheimer Feld',
                     'borough': 'Heidelberg',
                     'locality': 'Heidelberg',
                     'county': 'Rhein-Neckar-Kreis',
                     'region': 'Baden-Württemberg',
                     'postalcode': '69120',
                     'country': 'de'}

params_reverse = {'circle_radius': 50,
                  'sources': ['osm', 'wof', 'gn'],
                  'layers': ['locality', 'county', 'region'],
                  'country': 'de',
                  'size': 5}

params_pois = {'request': 'pois',
               'bbox': [[8.8034, 53.0756], [8.7834, 53.0456]],
               'geojson': {'type': 'Point'},
               'buffer': 100,
               'limit': 900,
               'filter_category_ids': [180, 245],
               'filters_custom': {'wheelchair': ['yes'], 'smoking': ['dedicated'], 'fee': ['yes']},
               'sortby': 'distance'}


class ValidatorTest(_test.TestCase):

    def setUp(self):
        self.coords_point = (8.34234, 48.23424)
        self.coords_linestring = ((8.34234, 48.23424), (8.34423, 48.26424))
        self.coords_matrix = [[9.970093, 48.477473], [9.207916, 49.153868], [37.573242, 55.801281],
                              [115.663757, 38.106467]]

    def test_directions_correct_schema(self):
        params['coordinates'] = self.coords_linestring
        validator.validator(params, 'directions')

    def test_directions_wrong_schema(self):
        params['coordinates'] = self.coords_linestring
        params['preference'] = 'best'
        params['attributeds'] = ['avgspeed']
        params['optimized'] = 'true'
        params['radiuses'] = [10000, 10000, 10000, 10000]
        params['bearings'] = [[100, 100], [200, 200]]
        params['options'] = {'maximum_speed': '20'}

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(params, 'directions')
        em = e.exception
        print(em)

        self.assertIn('unallowed value best', str(em))
        self.assertIn('unknown field', str(em))
        self.assertIn('max length is 2', str(em))
        self.assertIn('must be of integer type', str(em))

    def test_isochrones_correct_schema(self):
        params_isochrones['locations'] = self.coords_linestring
        validator.validator(params_isochrones, 'isochrones')

    def test_isochrones_wrong_schema(self):
        params_isochrones['intervals'] = ['30']

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(params_isochrones, 'isochrones')
        em = e.exception
        print(em)

        self.assertIn('required field', str(em))
        self.assertIn('must be of integer type', str(em))

    def test_distance_matrix_correct_schema(self):
        params_matrix['locations'] = self.coords_matrix
        validator.validator(params_matrix, 'distance_matrix')

    def test_distance_matrix_wrong_schema(self):
        params_matrix['locations'] = self.coords_matrix
        params_matrix['sources'] = [0, 1, 2, 3, 4, 5]
        params_matrix['optimizedd'] = 'false'

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(params_matrix, 'distance_matrix')
        em = e.exception
        print(em)

        self.assertIn('no definitions validate', str(em))
        self.assertIn('unknown field', str(em))

    def test_search_correct_schema(self):
        params_search['focus_point'] = self.coords_point
        validator.validator(params_search, 'pelias_search')

    def test_search_wrong_schema(self):
        params_search['circle_radius'] = {50}
        params_search['layers'] = ['locality', 'name']

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(params_search, 'pelias_search')
        em = e.exception
        print(em)

        self.assertIn("unallowed values ['name']", str(em))
        self.assertIn('must be of integer type', str(em))

    def test_structured_correct_schema(self):
        validator.validator(params_structured, 'pelias_structured')

    def test_structured_wrong_schema(self):
        params_structured['address'] = {'Berliner Straße 45'}

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(params_structured, 'pelias_structured')
        em = e.exception
        print(em)

        self.assertIn('must be of string type', str(em))

    def test_reverse_correct_schema(self):
        params_reverse['point'] = self.coords_point
        validator.validator(params_reverse, 'pelias_reverse')

    def test_reverse_wrong_schema(self):
        params_reverse['country'] = 50
        params_reverse['sources'] = ['osm', 'wof', 'gm']

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(params_reverse, 'pelias_reverse')
        em = e.exception
        print(em)

        self.assertIn('must be of string type', str(em))
        self.assertIn("unallowed values ['gm']", str(em))

    def test_pois_correct_schema(self):
        params_pois['geojson']['coordinates'] = self.coords_point
        validator.validator(params_pois, 'pois')

    def test_pois_wrong_schema(self):
        params_pois['filters_custom']['wheelchair'] = ['maybe']
        params_pois['limit'] = 1200

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(params_pois, 'pois')
        em = e.exception
        print(em)

        self.assertIn("field 'coordinates' is required", str(em))
        self.assertIn('max value is 1000', str(em))
        self.assertIn('unallowed value maybe', str(em))
