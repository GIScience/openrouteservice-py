from cerberus import Validator, TypeDefinition
from cerberus.tests import assert_success, assert_normalized, assert_fail, assert_schema_error
from cerberus import errors  # BasicErrorHandler#, BaseErrorHandler, ValidationError


def directions_validation(params):  # , error
    """Validates the used parameter with Cerberus."""
    # Add the tuple type
    tuple_type = TypeDefinition("tuple", (tuple), ())
    Validator.types_mapping["tuple"] = tuple_type

    schema = {
        'coordinates': {'anyof': [{'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
                                  {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'float'}}},
                                  {'type': 'tuple', 'schema': {'type': 'tuple', 'schema': {'type': 'float'}}}],
                        # 'required': True
                        },
        'profile': {'type': 'string',
                    'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                                'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                                'cycling-electric'],  # 'required': True,
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
                                'minlength': len('coordinates'), 'maxlength': len('coordinates')}},
        'bearings': {'type': ['list', 'tuple'],
                     # 'minlength': len('coordinates') - 1,
                     'maxlength': len('coordinates'),
                     'schema': {'type': 'list',
                                'items': [{'type': 'integer', 'min': 0, 'max': 360, 'required': True},
                                          {'type': 'integer', 'default': 100}],
                                'minlength': 1, 'maxlength': 2
                                },
                     # 'dependencies': {'optimized': 'false'}
                     },
        'continue_straight': {'type': 'string', 'allowed': ['true', 'false'], 'default': 'false',
                              # 'dependencies': {'optimized': 'false'},
                              # 'forbidden': [{'profile': 'driving-^'}]
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
                                                                 # 'dependencies': {'profile': ['driving-car', 'driving-hgv']}
                                                                 },
                                               'avoid_countries': {'type': 'string'},
                                               'vehicle_type': {'type': 'string',
                                                                'allowed': ['hgv', 'bus', 'agricultural',
                                                                            'delivery',
                                                                            'forestry', 'goods']
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
                                                                 # 'dependencies': {'profile': 'foot-walking',
                                                                 #                  'foot-hiking'}
                                                                 },
                                                       'quiet': {'type': 'dict', 'schema': {
                                                           'factor': {'type': 'float', 'min': 0,
                                                                      'max': 1}},
                                                                 # 'dependencies': {'profile': 'foot-walking',
                                                                 #                  'foot-hiking'}
                                                                 }}},
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
    # assert_success(params, schema)
    try:
        assert_success(params, schema)
        # print('OK')
    except Exception as message:
        print(message)


def isochrones_validation(params):
    """Validates the used parameter with Cerberus."""
    # Add the tuple type
    tuple_type = TypeDefinition("tuple", (tuple), ())
    Validator.types_mapping["tuple"] = tuple_type

    schema = {
        'locations': {'anyof': [{'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
                                {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'float'}}},
                                {'type': 'tuple', 'schema': {'type': 'tuple', 'schema': {'type': 'float'}}}]},
        'profile': {'type': 'string',
                    'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                                'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                                'cycling-electric']},
        'range_type': {'type': 'string', 'allowed': ['time', 'distance']},
        'range': {'type': ['list', 'tuple'], 'schema': {'type': 'integer'}},
        'interval': {'type': ['list', 'tuple'], 'schema': {'type': 'integer'}},
        'units': {'type': 'string', 'allowed': ['m', 'km', 'mi'], 'default': 'm'},
        'location_type': {'type': 'string', 'allowed': ['start', 'destination']},
        'attributes': {'type': ['list', 'tuple'], 'schema': {'type': 'string',
                                                             'allowed': ['area', 'reachfactor', 'total_pop']}},
        'options': {'type': 'dict', 'schema': {'maximum_speed': {'type': 'integer'},
                                               'avoid_features': {'type': 'string',
                                                                  'allowed': ['highways', 'tollways', 'ferries',
                                                                              'tunnels',
                                                                              'pavedroads', 'unpavedroads',
                                                                              'tracks',
                                                                              'fords', 'steps', 'hills']},
                                               'avoid_borders': {'type': 'string',
                                                                 'allowed': ['all', 'controlled']},
                                               'avoid_countries': {'type': 'string'},
                                               'vehicle_type': {'type': 'string',
                                                                'allowed': ['hgv', 'bus', 'agricultural',
                                                                            'delivery',
                                                                            'forestry', 'goods']},
                                               'profile_params': {'type': 'dict', 'schema': {
                                                   'weightings': {'type': 'dict', 'schema': {
                                                       'steepness_difficulty': {'type': 'dict', 'schema': {
                                                           'level': {'type': 'integer', 'min': 0, 'max': 3}}},
                                                       'green': {'type': 'dict', 'schema': {
                                                           'factor': {'type': 'float', 'min': 0, 'max': 1}}},
                                                       'quiet': {'type': 'dict', 'schema': {
                                                           'factor': {'type': 'float', 'min': 0, 'max': 1}}}}},
                                                   # 'restrictions':
                                               }},
                                               # 'avoid_polygons'
                                               }},
        'intersections': {'type': 'string', 'allowed': ['true', 'false']},
        'id': {'type': 'string'}
    }

    assert_success(params, schema)


def distance_matrix_validation(params):
    """Validates the used parameter with Cerberus."""
    # Add the tuple type
    tuple_type = TypeDefinition("tuple", (tuple), ())
    Validator.types_mapping["tuple"] = tuple_type

    schema = {
        'locations': {'anyof': [{'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
                                {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'float'}}},
                                {'type': 'tuple', 'schema': {'type': 'tuple', 'schema': {'type': 'float'}}}]},
        'sources': {'oneof': [{'type': 'list', 'schema': {'type': 'integer', 'min': 0}},
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

    assert_success(params, schema)


def search_validation(params):
    """Validates the used parameter with Cerberus."""
    # Add the tuple type
    tuple_type = TypeDefinition("tuple", (tuple), ())
    Validator.types_mapping["tuple"] = tuple_type

    schema = {
        'text': {'type': 'string'},
        'focus_point': {'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
        'rect_min_x': {'type': 'float'},
        'rect_min_y': {'type': 'float'},
        'rect_max_x': {'type': 'float'},
        'rect_max_y': {'type': 'float'},
        'circle_point': {'type': ['tuple', 'float']},
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
    }

    assert_success(params, schema)


def structured_validation(params):
    """Validates the used parameter with Cerberus."""
    # Add the tuple type
    tuple_type = TypeDefinition("tuple", (tuple), ())
    Validator.types_mapping["tuple"] = tuple_type

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

    assert_success(params, schema)


def reverse_validation(params):
    """Validates the used parameter with Cerberus."""
    # Add the tuple type
    tuple_type = TypeDefinition("tuple", (tuple), ())
    Validator.types_mapping["tuple"] = tuple_type

    schema = {
        'point': {'anyof': [{'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
                            {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'float'}}},
                            {'type': 'tuple', 'schema': {'type': 'tuple', 'schema': {'type': 'float'}}}]},
        'circle_radius': {'type': 'integer'},
        'sources': {'type': 'list', 'schema': {'type': 'string'}, 'allowed': ['osm', 'oa', 'wof', 'gn'],
                    'default': ['osm', 'oa', 'wof', 'gn']},
        'layers': {'type': 'list', 'schema': {'type': 'string'},
                   'allowed': ['venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                               'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'],
                   'default': ['venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                               'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse']},
        'country': {'type': 'string'},
        'size': {'type': 'integer', 'default': 10},
    }

    assert_success(params, schema)

# def geocode_validation(params):

# def places_validation(params):
#     """Validates the used parameter with Cerberus."""
#     # Add the tuple type
#     tuple_type = TypeDefinition("tuple", (tuple), ())
#     Validator.types_mapping["tuple"] = tuple_type
#
#     schema = {
#         'request': {'type': 'string', 'allowed': ['pois', 'list', 'stats']},
#
#     }
