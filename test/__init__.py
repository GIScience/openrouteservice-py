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

import unittest
import codecs

from cerberus import Validator


try: # Python 3
    from urllib.parse import urlparse, parse_qsl
except ImportError: # Python 2
    from urlparse import urlparse, parse_qsl


class TestCase(unittest.TestCase):

    def assertURLEqual(self, first, second, msg=None):
        """Check that two arguments are equivalent URLs. Ignores the order of
        query arguments.
        """
        first_parsed = urlparse(first)
        second_parsed = urlparse(second)
        self.assertEqual(first_parsed[:3], second_parsed[:3], msg)

        first_qsl = sorted(parse_qsl(first_parsed.query))
        second_qsl = sorted(parse_qsl(second_parsed.query))
        self.assertEqual(first_qsl, second_qsl, msg)

    def u(self, string):
        """Create a unicode string, compatible across all versions of Python."""
        # NOTE(cbro): Python 3-3.2 does not have the u'' syntax.
        return codecs.unicode_escape_decode(string)[0]

    def validateFormat(self, params=None):
        """Validates the used parameter with Cerberus."""
        # class ObjectValidator(Validator):
        #   def validate_object(self, obj):
        #      return self.validate(obj.__dict__)

        schema = {
            'address': {'type': 'string'},
            'attributes': {'type': 'list', 'schema': {'type': 'string',
                                                      'allowed': ['area', 'reachfactor', 'total_pop', 'avgspeed',
                                                                  'detourfactor', 'percentage']}},
            # in directions, isochrones # tuple?
            # 'bearings' # tuples are not supported
            'borough': {'type': 'string'},
            # 'buffer'
            'category_group_ids': {'type': 'list', 'schema': {'type': 'integer'}},
            'circle_radius': {'type': 'integer'},
            'continue_straight': {'type': 'string', 'allowed': ['true', 'false']},
            'coordinates': {'type': 'list', 'schema': {'type': 'float'}},
            'country': {'type': 'list', 'schema': {'type': 'string'}},
            # 'country': {'type': 'string'}, -> strucured
            'county': {'type': 'string'},
            'destinations': {
                'oneof': [{'type': 'list', 'schema': {'type': 'integer'}}, {'type': 'string', 'allowed': ['all']}]},
            'dry_run': {'type': 'string', 'allowed': ['true', 'false']},
            'elevation': {'type': 'string', 'allowed': ['true', 'false']},
            'extra_info': {'type': 'string',
                           'allowed': ['steepness', 'suitability', 'surface', 'waycategory', 'waytype', 'tollways',
                                       'traildifficulty']},  # tuples are not supported
            'filter_category_ids': {'type': 'list', 'schema': {'type': 'integer'}},  # -> 'category_ids'?
            'filters_custom': {'type': 'dict', 'schema': {
                'name': {'type': 'list', 'schema': {
                    'type': 'string'
                }},
                'wheelchair': {'type': 'list', 'schema': {
                    'type': 'string', 'allowed': ['yes', 'limited', 'no', 'designated']
                }},
                'smoking': {'type': 'list', 'schema': {
                    'type': 'string', 'allowed': ['dedicated', 'yes', 'separated', 'isolated', 'no', 'outside']
                }},
                'fee': {'type': 'list', 'schema': {
                    'type': 'string', 'allowed': ['yes', 'no', 'str']
                }}}},
            # 'first_request_time': {'type': 'datetime'}, -> datetime.datetime
            'focus_point': {},  # format?
            # 'geojson'
            'geometry': {'type': 'string', 'allowed': ['true', 'false']},
            'geometry_format': {'type': 'string', 'allowed': ['encodedpolyline', 'geojson', 'polyline']},
            'geometry_simplify': {'type': 'string', 'allowed': ['true', 'false']},
            'instructions': {'type': 'string', 'allowed': ['true', 'false']},
            'instructions_format': {'type': 'string', 'allowed': ['text', 'html']},
            # 'intersections': {'type': 'string'}, -> not implemented right now
            'intervals': {'type': 'list', 'schema': {'type': 'integer'}},
            'language': {'type': 'string',
                         'allowed': ['en', 'de', 'cn', 'es', 'ru', 'dk', 'fr', 'it', 'nl', 'br', 'se', 'tr', 'gr']},
            # different values in APIs
            'layers': {'type': 'list', 'schema': {'type': 'string'}},
            'locality': {'type': 'string'},
            'location_type': {'type': 'string', 'allowed': ['start', 'destination']},
            'locations': {'type': 'list', 'schema': {'type': 'float'}},  # tuples are not supported
            'limit': {'type': 'integer'},
            'metrics': {'type': 'list', 'schema': {'type': 'string'}, 'allowed': ['distance', 'duration']},
            'neighbourhood': {'type': 'string'},
            'optimized': {'type': 'string', 'allowed': ['true', 'false']},
            # 'options': {'type': 'dict'}, -> not implemented right now
            # 'params': {} # key/value tuples are not supported
            'point': {'type': 'list', 'schema': {
                'type': 'list', 'schema': {'type': 'float'}}},  # tuples are not supported
            'polyline': {'type': 'string'},
            'post_json': {'type': 'dict'},
            'postalcode': {'type': 'string'},
            'profile': {'type': 'string',
                        'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                                    'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                                    'cycling-electric']},
            'preference': {'type': 'string', 'allowed': ['fastest', 'shortest', 'recommended']},
            'radiuses': {'type': 'list',
                         'schema': {'oneof': [{'type': 'float', 'allowed': [-1]}, {'type': 'float', 'min': 0}]}},
            # tuples are not supported
            'range_type': {'type': 'string', 'allowed': ['time', 'distance']},
            'rect_min_x': {'type': 'float'},
            'rect_min_y': {'type': 'float'},
            'rect_max_x': {'type': 'float'},
            'rect_max_y': {'type': 'float'},
            'region': {'type': 'string'},
            'request': {'type': 'string', 'allowed': ['pois', 'list', 'stats']},
            'requests_kwargs': {'type': 'dict'},
            'resolve_locations': {'type': 'string', 'allowed': ['true', 'false']},
            'retry_counter': {'type': 'integer'},
            'roundabout_exits': {'type': 'string', 'allowed': ['true', 'false']},
            'segments': {'type': 'integer'},
            'size': {'type': 'integer'},
            'smoothing': {'type': 'float', 'min': 0, 'max': 1},
            'sortby': {'type': 'string', 'allowed': ['distance', 'category']},
            # 'sources' -> distanc_matrix: one or more indices inside a list; or 'all' (string)
            'sources': {'type': 'list', 'schema': {'type': 'string'}, 'allowed': ['osm', 'oa', 'wof', 'gn']},
            'text': {'type': 'string'},
            'units': {'type': 'string', 'allowed': ['m', 'km', 'mi']},
            'url': {'type': 'string'},
        }

        # v = ObjectValidator(schema)
        v = Validator()
        validation = v.validate(params, schema)
        self.validateFormat(validation)
