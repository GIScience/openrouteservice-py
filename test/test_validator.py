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

"""Tests for the validator module."""

from openrouteservice import validator, exceptions
import test as _test
from test.test_helper import *

class ValidatorTest(_test.TestCase):
    
    def test_directions_correct_schema(self):
        validator.validator(ENDPOINT_DICT['directions'], 'directions')

    def test_directions_wrong_schema(self):
        ENDPOINT_DICT['directions']['preference'] = 'best'
        ENDPOINT_DICT['directions']['attributeds'] = ['avgspeed']
        ENDPOINT_DICT['directions']['radiuses'] = 2 * PARAM_LIST_ONE
        ENDPOINT_DICT['directions']['options'] = {'maximum_speed': '20'}

        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['directions'], 'directions')
        em = e.exception
        print(em)
        
        self.assertIn('unallowed value best', str(em))
        self.assertIn('unknown field', str(em))
        self.assertIn('max length is 2', str(em))
        self.assertIn('must be of integer type', str(em))
        
    def test_isochrones_correct_schema(self):
        validator.validator(ENDPOINT_DICT['isochrones'], 'isochrones')

    def test_isochrones_wrong_schema(self):
        del ENDPOINT_DICT['isochrones']['locations']
        ENDPOINT_DICT['isochrones'].update(
                { 'attributes': ['areas', 'reachfactor'],
                  'intervals': ['30']
                  })
        
        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['isochrones'], 'isochrones')
        em = e.exception        
        print(em)
        
        self.assertIn('required field', str(em))
        self.assertIn('unallowed value', str(em))
        self.assertIn('must be of integer type', str(em))

    def test_distance_matrix_correct_schema(self):
        validator.validator(ENDPOINT_DICT['distance_matrix'], 'distance_matrix')

    def test_distance_matrix_wrong_schema(self):
        ENDPOINT_DICT['distance_matrix'].update(
                { 'sources': [0, 1, 2],
                  'metrics': ['duration', 'distance'],
                  'resolve_locations': 'true',
                  'units': 'm',
                  'optimizedd': 'false'}
                )
        
        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['distance_matrix'], 'distance_matrix')
        em = e.exception        
        print(em)
        
        self.assertIn('no definitions validate', str(em))
        self.assertIn('unknown field', str(em))

    def test_search_correct_schema(self):
        validator.validator(ENDPOINT_DICT['pelias_search'], 'pelias_search')

    def test_search_wrong_schema(self):
        ENDPOINT_DICT['pelias_search'].update({
                  'layers': ['locality', 'name'],
                  'circle_radius': {50},
                })
        
        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['pelias_search'], 'pelias_search')
        em = e.exception        
        print(em)
        
        self.assertIn("unallowed values ['name']", str(em))
        self.assertIn('must be of integer type', str(em))

    def test_autocomplete_correct_schema(self):
        validator.validator(ENDPOINT_DICT['pelias_autocomplete'], 'pelias_autocomplete')

    def test_autocomplete_wrong_schema(self):
        ENDPOINT_DICT['pelias_autocomplete'].update({
                  'layers': ['locality', 'name'],
                })
        
        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['pelias_autocomplete'], 'pelias_autocomplete')
        em = e.exception        
        print(em)
        
        self.assertIn("unallowed values ['name']", str(em))
        
    def test_structured_correct_schema(self):
        validator.validator(ENDPOINT_DICT['pelias_structured'], 'pelias_structured')
        
    def test_structured_wrong_schema(self):
        ENDPOINT_DICT['pelias_structured'].update({
                'address': {'Berliner Straße 45'},
                'postalcode': '69120',                
                })
        params = {'address': {'Berliner Straße 45'},
                  'neighbourhood': 'Neuenheimer Feld',
                  'borough': 'Heidelberg',
                  'locality': 'Heidelberg',
                  'county': 'Rhein-Neckar-Kreis',
                  'region': 'Baden-Württemberg',
                  'postalcode': '69120',
                  'country': 'de',
                  }
        
        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['pelias_structured'], 'pelias_structured')
        em = e.exception        
        print(em)
        
        self.assertIn('must be of integer type', str(em))
        self.assertIn('must be of string type', str(em))

    def test_reverse_correct_schema(self):
        validator.validator(ENDPOINT_DICT['pelias_reverse'], 'pelias_reverse')
        
    def test_reverse_wrong_schema(self):
        ENDPOINT_DICT['pelias_reverse'].update({
                  'country': 35,
                  'sources': ['osm', 'wof', 'gm'],                
                })
        
        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['pelias_reverse'], 'pelias_reverse')
        em = e.exception        
        print(em)
        
        self.assertIn('must be of string type', str(em))
        self.assertIn("unallowed values ['gm']", str(em))
        
    def test_pois_correct_schema(self):
        validator.validator(ENDPOINT_DICT['pois'], 'pois')
        
        ENDPOINT_DICT['pois']['geojson'] = PARAM_GEOJSON_LINE
        validator.validator(ENDPOINT_DICT['pois'], 'pois')
        
        ENDPOINT_DICT['pois']['geojson'] = PARAM_GEOJSON_POLY
        validator.validator(ENDPOINT_DICT['pois'], 'pois')
        
        ENDPOINT_DICT['pois']['request'] = 'stats'
        validator.validator(ENDPOINT_DICT['pois'], 'pois')
    
        ENDPOINT_DICT['pois'] = {'request': 'list'}
        validator.validator(ENDPOINT_DICT['pois'], 'pois')        
        
    def test_pois_wrong_schema(self):
        ENDPOINT_DICT['pois'].update({
                  'geojson': {'type': 'Point'},
                  'filters_custom': {'wheelchair': ['maybe']},
                  'limit': 1200,
                })
        
        with self.assertRaises(exceptions.ValidationError) as e:
            validator.validator(ENDPOINT_DICT['pois'], 'pois')
        em = e.exception        
        print(em)
        
        self.assertIn("field 'coordinates' is required", str(em))
        self.assertIn('max value is 1000', str(em))
        self.assertIn('unallowed value maybe', str(em))
