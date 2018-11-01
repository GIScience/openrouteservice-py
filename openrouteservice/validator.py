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

"""Validates the used parameter with Cerberus."""

from cerberus import Validator, TypeDefinition

# Add the tuple type
tuple_type = TypeDefinition("tuple", (tuple), ())
Validator.types_mapping['tuple'] = tuple_type
v = Validator()


def validator(params, module, coords_len):
    if module == "directions":
        return directions_validation(params, coords_len)
    elif module == "isochrones":
        return isochrones_validation(params)
    elif module == "distance_matrix":
        return distance_matrix_validation(params)
    elif module == "search":
        return search_validation(params)
    elif module == "structured":
        return structured_validation(params)
    elif module == "reverse":
        return reverse_validation(params)
    elif module == "pois":
        return pois_validation(params)


def directions_validation(params, coords_len):
    schema = {
        'coordinates': {'anyof': [{'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
                                  {'type': ['list', 'tuple'],
                                   'schema': {'type': ['list', 'tuple'], 'schema': {'type': 'float'}}}],
                        # 'required': True
                        },
        'profile': {'type': 'string',
                    'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                                'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                                'cycling-electric'],  # 'required': True
                    },
        'preference': {'type': 'string', 'allowed': ['fastest', 'shortest', 'recommended'], 'default': 'fastest'},
        'format': {'type': 'string', 'allowed': ['json', 'geojson', 'gpx'], 'default': 'json'},
        'units': {'type': 'string', 'allowed': ['m', 'km', 'mi'], 'default': 'm'},
        'language': {'type': 'string',
                     'allowed': ['en', 'de', 'cn', 'es', 'ru', 'dk', 'fr', 'it', 'nl', 'br', 'se', 'tr', 'gr'],
                     'default': 'en'},
        'geometry': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'true'},
        'geometry_format': {'type': 'string', 'allowed': ['encodedpolyline', 'geojson', 'polyline'],
                            'default': 'encodedpolyline'},
        'geometry_simplify': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'false'},
        'instructions': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'true'},
        'instructions_format': {'type': 'string', 'allowed': ['text', 'html'], 'default': 'text'},
        'roundabout_exits': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'false'},
        'attributes': {'type': ['list', 'tuple'], 'schema': {'type': 'string',
                                                             'allowed': ['avgspeed',
                                                                         'detourfactor', 'percentage']}},
        'maneuvers': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'false'},
        'radiuses': {'type': ['list', 'tuple'],
                     'schema': {'oneof': [{'type': 'float', 'allowed': [-1]}, {'type': 'float', 'min': 0}],
                                'minlength': coords_len, 'maxlength': coords_len
                                }},
        'bearings': {'type': ['list', 'tuple'],
                     'minlength': coords_len - 1, 'maxlength': coords_len,
                     'schema': {'type': 'list',
                                'items': [{'type': 'integer', 'min': 0, 'max': 360, 'required': True},
                                          {'type': 'integer', 'default': 100}], 'minlength': 1, 'maxlength': 2},
                     # 'dependencies': {'optimized': 'false'}
                     },
        'continue_straight': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'false',
                              # 'dependencies': {'optimized': 'false',
                              #                  'profile': ['foot-walking', 'foot-hiking', 'cycling-regular',
                              #                              'cycling-road', 'cycling-safe', 'cycling-mountain',
                              #                              'cycling-tour',
                              #                              'cycling-electric']}
                              },
        'elevation': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'false'},
        'extra_info': {'type': ['list', 'tuple'], 'schema': {'type': 'string',
                                                             'allowed': ['steepness', 'suitability',
                                                                         'surface',
                                                                         'waycategory', 'waytype',
                                                                         'tollways',
                                                                         'traildifficulty']}},
        'optimized': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'true'},
        'options': {'type': 'dict', 'schema': {'maximum_speed': {'type': 'integer'},
                                               'avoid_features': {'type': 'list', 'schema': {'type': 'string',
                                                                                             'allowed': ['highways',
                                                                                                         'tollways',
                                                                                                         'ferries',
                                                                                                         'tunnels',
                                                                                                         'pavedroads',
                                                                                                         'unpavedroads',
                                                                                                         'tracks',
                                                                                                         'fords',
                                                                                                         'steps',
                                                                                                         'hills']}},
                                               'avoid_borders': {'type': 'string',
                                                                 'allowed': ['all', 'controlled'],
                                                                 # 'dependencies': {
                                                                 #     'profile': ['driving-car', 'driving-hgv']}
                                                                 },
                                               'avoid_countries': {'type': 'string'},
                                               'vehicle_type': {'type': 'string',
                                                                'allowed': ['hgv', 'bus', 'agricultural',
                                                                            'delivery',
                                                                            'forestry', 'goods'],
                                                                # 'dependencies': {'profile': 'driving-hgv'}
                                                                },
                                               'profile_params': {'type': 'dict', 'schema': {
                                                   'weightings': {'type': 'dict', 'schema': {
                                                       'steepness_difficulty': {'type': 'dict', 'schema': {
                                                           'level': {'type': 'integer', 'min': 0,
                                                                     'max': 3}},
                                                                                # 'dependencies': {
                                                                                #     'profile': ['cycling-regular',
                                                                                #                 'cycling-road',
                                                                                #                 'cycling-safe',
                                                                                #                 'cycling-mountain',
                                                                                #                 'cycling-tour',
                                                                                #                 'cycling-electric']}
                                                                                },
                                                       'green': {'type': 'dict', 'schema': {
                                                           'factor': {'type': 'float', 'min': 0,
                                                                      'max': 1}},
                                                                 # 'dependencies': {'profile': ['foot-walking',
                                                                 #                              'foot-hiking']}
                                                                 },
                                                       'quiet': {'type': 'dict', 'schema': {
                                                           'factor': {'type': 'float', 'min': 0,
                                                                      'max': 1}},
                                                                 # 'dependencies': {'profile': ['foot-walking',
                                                                 #                              'foot-hiking']}
                                                                 }}
                                                                  },
                                                   # 'restrictions': {'type': 'dict', 'schema': {
                                                   #   'gradient': {'type': 'integer', 'min': 1, 'max': 15,
                                                   # 'dependencies': {
                                                   #     'profile': ['cycling-regular',
                                                   #                 'cycling-road',
                                                   #                 'cycling-safe',
                                                   #                 'cycling-mountain',
                                                   #                 'cycling-tour',
                                                   #                 'cycling-electric']}
                                                   # },

                                                   # }}
                                               }},
                                               # 'avoid_polygons'
                                               }},
        'id': {'type': 'string'}
    }

    v.validate(params, schema)

    return v


def isochrones_validation(params):
    schema = {
        'locations': {'anyof': [{'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
                                {'type': ['list', 'tuple'],
                                 'schema': {'type': ['list', 'tuple'], 'schema': {'type': 'float'}}}],
                      'required': True},
        'profile': {'type': 'string',
                    'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                                'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                                'cycling-electric'], 'required': True},
        'range_type': {'type': 'string', 'allowed': ['time', 'distance'], 'default': 'time'},
        'range': {'type': ['list', 'tuple'], 'schema': {'type': 'integer'}},
        'interval': {'type': ['list', 'tuple'], 'schema': {'type': 'integer'}},
        'units': {'type': 'string', 'allowed': ['m', 'km', 'mi'], 'default': 'm',
                  'dependencies': {'range_type': 'distance'}},
        'location_type': {'type': 'string', 'allowed': ['start', 'destination'], 'default': 'start'},
        'attributes': {'type': ['list', 'tuple'], 'schema': {'type': 'string',
                                                             'allowed': ['area', 'reachfactor', 'total_pop']}},
        'options': {'type': 'dict', 'schema': {'maximum_speed': {'type': 'integer'},
                                               'avoid_features': {'type': 'list', 'schema': {'type': 'string',
                                                                                             'allowed': ['highways',
                                                                                                         'tollways',
                                                                                                         'ferries',
                                                                                                         'tunnels',
                                                                                                         'pavedroads',
                                                                                                         'unpavedroads',
                                                                                                         'tracks',
                                                                                                         'fords',
                                                                                                         'steps',
                                                                                                         'hills']}},
                                               'avoid_borders': {'type': 'string',
                                                                 'allowed': ['all', 'controlled'],
                                                                 'dependencies': {
                                                                     'profile': ['driving-car', 'driving-hgv']}},
                                               'avoid_countries': {'type': 'string'},
                                               'vehicle_type': {'type': 'string',
                                                                'allowed': ['hgv', 'bus', 'agricultural',
                                                                            'delivery',
                                                                            'forestry', 'goods'],
                                                                'dependencies': {'profile': 'driving-hgv'}},
                                               'profile_params': {'type': 'dict', 'schema': {
                                                   'weightings': {'type': 'dict', 'schema': {
                                                       'steepness_difficulty': {'type': 'dict', 'schema': {
                                                           'level': {'type': 'integer', 'min': 0,
                                                                     'max': 3}},
                                                                                'dependencies': {
                                                                                    'profile': ['cycling-regular',
                                                                                                'cycling-road',
                                                                                                'cycling-safe',
                                                                                                'cycling-mountain',
                                                                                                'cycling-tour',
                                                                                                'cycling-electric']}
                                                                                },
                                                       'green': {'type': 'dict', 'schema': {
                                                           'factor': {'type': 'float', 'min': 0,
                                                                      'max': 1}},
                                                                 'dependencies': {'profile': ['foot-walking',
                                                                                              'foot-hiking']}},
                                                       'quiet': {'type': 'dict', 'schema': {
                                                           'factor': {'type': 'float', 'min': 0,
                                                                      'max': 1}},
                                                                 'dependencies': {'profile': ['foot-walking',
                                                                                              'foot-hiking']}}}},
                                                   # 'restrictions': {'type': 'dict', 'schema': {
                                                   #   'gradient': {'type': 'integer', 'min': 1, 'max': 15,
                                                   # 'dependencies': {
                                                   #     'profile': ['cycling-regular',
                                                   #                 'cycling-road',
                                                   #                 'cycling-safe',
                                                   #                 'cycling-mountain',
                                                   #                 'cycling-tour',
                                                   #                 'cycling-electric']}
                                                   # },

                                                   # }}
                                               }},
                                               # 'avoid_polygons'
                                               }},
        'intersections': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'false'},
        'id': {'type': 'string'},
        'smoothing': {"type": "float", 'min': 0, 'max': 1}
    }

    v.validate(params, schema)

    return v


def distance_matrix_validation(params):
    schema = {
        'locations': {'type': ['list', 'tuple'], 'schema': {'type': ['list', 'tuple'], 'schema': {'type': 'float'}}},
        'sources': {'oneof': [{'type': 'list',
                               'schema': {'type': 'integer', 'min': 0}},
                              {'type': 'string', 'allowed': ['all']}]},
        'destinations': {
            'oneof': [{'type': 'list', 'schema': {'type': 'integer'}}, {'type': 'string', 'allowed': ['all']}]},
        'profile': {'type': 'string',
                    'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                                'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                                'cycling-electric'],  # 'required': True,
                    },
        'metrics': {'type': 'list', 'schema': {'type': 'string'}, 'allowed': ['distance', 'duration']},
        'resolve_locations': {'type': 'string', 'allowed': ['true', 'false']},
        'units': {'type': 'string', 'allowed': ['m', 'km', 'mi'], 'default': 'm'},
        'optimized': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'true'},
    }

    v.validate(params, schema)

    return v


def search_validation(params):
    schema = {
        'text': {'type': 'string'},
        'focus_point': {'type': 'list', 'schema': {'type': 'float'}},
        'rect_min_x': {'type': 'float'},
        'rect_min_y': {'type': 'float'},
        'rect_max_x': {'type': 'float'},
        'rect_max_y': {'type': 'float'},
        'circle_point': {'type': 'list', 'schema': {'type': 'float'}},
        'circle_radius': {'type': 'integer', 'default': 50},
        'sources': {'type': 'list', 'schema': {'type': 'string'}, 'allowed': ['osm', 'oa', 'wof', 'gn'],
                    'default': ['osm', 'oa', 'wof', 'gn']},
        'layers': {'type': 'list', 'schema': {'type': 'string'},
                   'allowed': ['venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                               'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'],
                   'default': ['venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                               'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse']},
        'country': {'type': 'string'},
        'size': {'type': 'integer', 'default': 10},
        'dry_run': {'type': 'string', 'allowed': ['true', 'false']}
    }

    v.validate(params, schema)

    return v


def structured_validation(params):
    schema = {
        'address': {'type': 'string'},
        'neighbourhood': {'type': 'string'},
        'borough': {'type': 'string'},
        'locality': {'type': 'string'},
        'county': {'type': 'string'},
        'region': {'type': 'string'},
        'postalcode': {'type': 'string'},
        'country': {'type': 'string'},
        # 'size': {'type': 'integer', 'default': 10},
    }

    v.validate(params, schema)

    return v


def reverse_validation(params):
    schema = {
        'point': {'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
        'circle_radius': {'type': 'integer'},
        'sources': {'type': ['list', 'tuple'], 'schema': {'type': 'string'}, 'allowed': ['osm', 'oa', 'wof', 'gn'],
                    'default': ['osm', 'oa', 'wof', 'gn']},
        'layers': {'type': ['list', 'tuple'], 'schema': {'type': 'string'},
                   'allowed': ['venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                               'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'],
                   'default': ['venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                               'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse']},
        'country': {'type': 'string'},
        'size': {'type': 'integer', 'default': 10},
    }

    v.validate(params, schema)

    return v


# def geocode_validation(params):

def pois_validation(params):
    schema = {
        'request': {'type': 'string', 'allowed': ['pois', 'list', 'stats']},
        # 'geometry': {'type': 'dict', 'schema': {
        'bbox': {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'float', 'maxlength': 2}}},
        'geojson': {'type': 'dict', 'schema': {
            'type': {'type': 'string', 'allowed': ['Point', 'Polygon', 'LineString']},
            'coordinates': {'type': 'list', 'schema': {'type': 'float', 'maxlength': 2}},  # listed list für polygone?
        }},  # }},
        'buffer': {'type': 'integer'},
        # 'filters': {'type': 'dict', 'schema': {
        'filter_category_group_ids': {'type': 'list', 'schema': {'type': 'integer'}},
        'filter_category_ids': {'type': 'list', 'schema': {'type': 'integer'}},
        'name': {'type': 'list', 'schema': {'type': 'string'}},
        'wheelchair': {'type': 'list',
                       'schema': {'type': 'string', 'allowed': ['yes', 'no', 'limited', 'designated']}},
        'smoking': {'type': 'list', 'schema': {'type': 'string',
                                               'allowed': ['dedicated', 'yes', 'no', 'separated', 'isolated',
                                                           'outside']}},
        'fee': {'type': 'list', 'schema': {'type': 'string', 'allowed': ['yes', 'no']}},  # }},
        'limit': {'type': 'integer', 'max': 1000},
        'sortby': {'type': 'string', 'allowed': ['category', 'distance']}
    }

    v.validate(params, schema)

    return v
