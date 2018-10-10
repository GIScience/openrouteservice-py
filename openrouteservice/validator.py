from cerberus import Validator, TypeDefinition
from cerberus.tests import assert_success, assert_normalized, assert_fail, assert_schema_error
from cerberus import errors  # BasicErrorHandler#, BaseErrorHandler, ValidationError


# class Validator:
# class CustomErrorHandler(errors.BasicErrorHandler):
#     messages = errors.BasicErrorHandler.messages.copy()
#     messages[errors.FORBIDDEN_VALUE.code] = 'VERBOTEN!'

# class SchemaErrorHandler(errors.BasicErrorHandler):
#   messages = errors.BasicErrorHandler.messages.copy()
# def arriseError():

def directions_validate(params):  # , error
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
    assert_success(params, schema)
    # try:
    #     assert_success(params, schema)
    #     #print('OK')
    # except Exception as message:
    #     print(message)


def isochrones_validate(params):
    # """Validates the used parameter with Cerberus."""
    # # Add the tuple type
    # tuple_type = TypeDefinition("tuple", (tuple), ())
    # Validator.types_mapping["tuple"] = tuple_type

    schema = {
        'locations': {'anyof': [{'type': ['list', 'tuple'], 'schema': {'type': 'float'}},
                                {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'float'}}},
                                {'type': 'tuple', 'schema': {'type': 'tuple', 'schema': {'type': 'float'}}}]},
        'profile': {'type': 'string',
                    'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                                'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                                'cycling-electric']},
        'range_type': {'type': 'string', 'allowed': ['time', 'distance']},
        'range': {'type': 'list', 'schema': {'type': 'integer'}},
        'interval': {'type': 'list', 'schema': {'type': 'integer'}},
        'units': {'type': 'string', 'allowed': ['m', 'km', 'mi']},
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

    try:
        assert_success(params, schema)
        print('OK')
    except Exception as message:
        print(message)
