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
from openrouteservice import exceptions

# Add the tuple type
tuple_type = TypeDefinition("tuple", (tuple), ())
Validator.types_mapping['tuple'] = tuple_type
v = Validator()


def validator(args, function):
    """
    Validates arguments against function specific schemas
    
    :param args: Arguments to validate
    :type args: dict
    
    :param function: calling function
    :type function: string
    
    :raises: ValidationError    
    """

    # Sanitize locals() variables
    args = {arg: args[arg] for arg in args if arg != 'client' and args[arg] is not None}

    if function == 'directions':
        coords_len = len(args['coordinates'])
        val = _directions_validation(args, coords_len)
    elif function == "isochrones":
        val = _isochrones_validation(args)
    elif function == "distance_matrix":
        coords_len = len(args['locations'])
        val = _distance_matrix_validation(args, coords_len)
    elif function == "pelias_search":
        val = _search_validation(args)
    elif function == "pelias_autocomplete":
        val = _autocomplete_validation(args)
    elif function == "pelias_structured":
        val = _structured_validation(args)
    elif function == "pelias_reverse":
        val = _reverse_validation(args)
    elif function == "pois":
        val = _pois_validation(args)
    elif function in ["elevation_point", "elevation_line"]:
        val = _elevation_validation(args)

    if val.errors:
        raise exceptions.ValidationError(val.errors)


def _directions_validation(params, coords_len):
    schema = {
        'coordinates': {
            'type': [
                'list',
                'tuple'
            ],
            'schema': {
                'type': [
                    'list',
                    'tuple'
                ],
                'schema': {
                    'type': 'float'
                }
            },
            'required': True
        },
        'profile': {
            'type': 'string',
            'allowed': [
                'driving-car',
                'driving-hgv',
                'foot-walking',
                'foot-hiking',
                'cycling-regular',
                'cycling-road',
                'cycling-safe',
                'cycling-mountain',
                'cycling-tour',
                'cycling-electric'
            ],
            'required': True
        },
        'preference': {
            'type': 'string',
            'allowed': [
                'fastest',
                'shortest',
                'recommended'
            ],
            'default': 'fastest'
        },
        'format_out': {
            'type': 'string',
            'allowed': [
                'json',
                'geojson',
                'gpx'
            ],
            'default': 'json'
        },
        'format': {
            'type': 'string',
            'allowed': [
                'json',
                'geojson',
                'gpx'
            ],
            'default': 'json'
        },
        'units': {
            'type': 'string',
            'allowed': [
                'm',
                'km',
                'mi'
            ],
            'default': 'm'
        },
        'language': {
            'type': 'string',
            'allowed': [
                'en',
                'de',
                'cn',
                'es',
                'ru',
                'dk',
                'fr',
                'it',
                'nl',
                'br',
                'se',
                'tr',
                'gr'
            ],
            'default': 'en'
        },
        'geometry': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'geometry_format': {
            'type': 'string',
            'allowed': [
                'encodedpolyline',
                'geojson',
                'polyline'
            ],
            'default': 'encodedpolyline'
        },
        'geometry_simplify': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'instructions': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'instructions_format': {
            'type': 'string',
            'allowed': [
                'text',
                'html'
            ],
            'default': 'text'
        },
        'roundabout_exits': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'attributes': {
            'type': [
                'list',
                'tuple'
            ],
            'schema': {
                'type': 'string',
                'allowed': [
                    'avgspeed',
                    'detourfactor',
                    'percentage'
                ]
            }
        },
        'maneuvers': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'radiuses': {
            'type': [
                'list',
                'tuple'
            ],
            'schema': {
                'type': 'integer',
                'min': -1
            },
            'minlength': coords_len,
            'maxlength': coords_len
        },
        'bearings': {
            'type': [
                'list',
                'tuple'
            ],
            'minlength': coords_len - 1,
            'maxlength': coords_len,
            'schema': {
                'type': 'list',
                'items': [
                    {
                        'type': 'integer',
                        'min': 0,
                        'max': 360,
                        'required': True
                    },
                    {
                        'type': 'integer',
                        'default': 100
                    }
                ],
                'minlength': 1,
                'maxlength': 2
            },

        },
        'continue_straight': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ],
            'dependencies': {
                '^profile': [
                    'foot-walking',
                    'foot-hiking',
                    'cycling-regular',
                    'cycling-road',
                    'cycling-safe',
                    'cycling-mountain',
                    'cycling-tour',
                    'cycling-electric'
                ]
            }
        },
        'elevation': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'extra_info': {
            'type': [
                'list',
                'tuple'
            ],
            'schema': {
                'type': 'string',
                'allowed': [
                    'steepness',
                    'suitability',
                    'surface',
                    'waycategory',
                    'waytype',
                    'tollways',
                    'traildifficulty',
                    'roadaccessrestrictions'
                ]
            }
        },
        'optimized': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'false',
                        'true'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'options': {
            'type': 'dict',
            'schema': {
                'avoid_features': {
                    'type': 'list',
                    'schema': {
                        'type': 'string',
                        'allowed': [
                            'highways',
                            'tollways',
                            'ferries',
                            'fords',
                            'steps'
                        ]
                    }
                },
                'avoid_borders': {
                    'type': 'string',
                    'allowed': [
                        'all',
                        'controlled'
                    ],
                    'dependencies': {
                        '^profile': [
                            'driving-car',
                            'driving-hgv'
                        ]
                    }
                },
                'avoid_countries': {
                    'schema': {
                        'type': 'integer'
                    },
                    'dependencies': {
                        '^profile': [
                            'driving-car',
                            'driving-hgv'
                        ]
                    }
                },
                'vehicle_type': {
                    'type': 'string',
                    'allowed': [
                        'hgv',
                        'bus',
                        'agricultural',
                        'delivery',
                        'forestry',
                        'goods'
                    ],
                    'dependencies': {
                        '^profile': 'driving-hgv'
                    }
                },
                'profile_params': {
                    'type': 'dict',
                    'schema': {
                        'weightings': {
                            'type': 'dict',
                            'schema': {
                                'steepness_difficulty': {
                                    'type': 'dict',
                                    'schema': {
                                        'level': {
                                            'type': 'integer',
                                            'allowed': [
                                                0,
                                                1,
                                                2,
                                                3
                                            ]
                                        }
                                    },
                                    'dependencies': {
                                        '^profile': [
                                            'cycling-regular',
                                            'cycling-road',
                                            'cycling-safe',
                                            'cycling-mountain',
                                            'cycling-tour',
                                            'cycling-electric'
                                        ]
                                    }
                                },
                                'green': {
                                    'type': 'float',
                                    'min': 0,
                                    'max': 1,
                                    'dependencies': {
                                        '^profile': [
                                            'foot-walking',
                                            'foot-hiking'
                                        ]
                                    }
                                },
                                'quiet': {
                                    'type': 'float',
                                    'min': 0,
                                    'max': 1,
                                    'dependencies': {
                                        '^profile': [
                                            'foot-walking',
                                            'foot-hiking'
                                        ]
                                    }
                                }
                            }
                        },
                        'restrictions': {
                            'type': 'dict',
                            'schema': {
                                'length': {
                                    'type': [
                                        'integer'
                                    ],
                                    'dependencies': {
                                        '^profile': 'driving-hgv'
                                    }
                                },
                                'width': {
                                    'type': [
                                        'integer'
                                    ],
                                    'dependencies': {
                                        '^profile': 'driving-hgv'
                                    }
                                },
                                'height': {
                                    'type': [
                                        'integer'
                                    ],
                                    'dependencies': {
                                        '^profile': 'driving-hgv'
                                    }
                                },
                                'axleload': {
                                    'type': [
                                        'integer'
                                    ],
                                    'dependencies': {
                                        '^profile': 'driving-hgv'
                                    }
                                },
                                'weight': {
                                    'type': [
                                        'integer'
                                    ],
                                    'dependencies': {
                                        '^profile': 'driving-hgv'
                                    }
                                },
                                'hazmat': {
                                    'anyof': [{
                                        'type': 'string',
                                        'allowed': [
                                            'true',
                                            'false'
                                        ]
                                    },
                                        {'type': 'boolean'}
                                    ],
                                    'dependencies': {
                                        '^profile': 'driving-hgv'
                                    }
                                },
                                'surface_type': {
                                    'type': 'string',
                                    'dependencies': {
                                        '^profile': 'wheelchair'
                                    }
                                },
                                'track_type': {
                                    'type': 'string',
                                    'allowed': [
                                        'grade1',
                                        'grade2',
                                        'grade3',
                                        'grade4',
                                        'grade5'
                                    ],
                                    'dependencies': {
                                        '^profile': 'wheelchair'
                                    }
                                },
                                'smoothness_type': {
                                    'type': 'string',
                                    'default': 'good',
                                    'dependencies': {
                                        '^profile': 'wheelchair'
                                    }
                                },
                                'maximum_sloped_curb': {
                                    'anyof': [
                                        {
                                            'type': 'float',
                                            'allowed': [
                                                0.03,
                                                0.06,
                                                0.1
                                            ]
                                        },
                                        {
                                            'type': 'string',
                                            'allowed': [
                                                'all'
                                            ]
                                        }
                                    ],
                                    'dependencies': {
                                        '^profile': 'wheelchair'
                                    }
                                },
                                'maximum_incline': {
                                    'anyof': [
                                        {
                                            'type': 'integer',
                                            'allowed': [
                                                3,
                                                6,
                                                10,
                                                15
                                            ]
                                        },
                                        {
                                            'type': 'string',
                                            'allowed': [
                                                'all'
                                            ]
                                        }
                                    ],
                                    'dependencies': {
                                        '^profile': 'wheelchair'
                                    }
                                }
                            }
                        }
                    }
                },
                'avoid_polygons': {
                    'type': 'dict',
                    'schema': {
                        'coordinates': {
                            'type': 'list',
                            'schema': {
                                'type': 'list',
                                'schema': {
                                    'type': 'list',
                                    'schema': {
                                        'anyof': [
                                            {
                                                'type': 'list',
                                                'schema': {
                                                    'type': 'float',
                                                },
                                                'minlength': 2,
                                                'maxlength': 2
                                            },
                                            {
                                                'type': 'float',
                                            }
                                        ]
                                    }
                                }
                            },
                        },
                        'type': {
                            'type': 'string',
                            'allowed': [
                                'Polygon',
                                'MultiPolygon'
                            ]
                        }
                    }
                }
            }
        },
        'suppress_warnings': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        },
        'id': {
            'type': 'string'
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [
                {
                    'type': 'string',
                    'allowed': [
                        'true',
                        'false'
                    ]
                },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _isochrones_validation(params):
    schema = {
        'locations': {
            'anyof': [{
                'type': ['list', 'tuple'],
                'schema': {
                    'type': 'float'
                }
            },
                {
                    'type': ['list', 'tuple'],
                    'schema': {
                        'type': ['list', 'tuple'],
                        'schema': {
                            'type': 'float'
                        }
                    }
                }
            ],
            'required': True
        },
        'profile': {
            'type': 'string',
            'allowed': ['driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                        'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                        'cycling-electric'
                        ],
            'default': 'driving-car',
            'required': True
        },
        'range_type': {
            'type': 'string',
            'allowed': ['time', 'distance'],
            'default': 'time'
        },
        'intervals': {
            'type': ['list', 'tuple'],
            'schema': {
                'type': 'integer'
            }
        },
        'range': {
            'type': ['list', 'tuple'],
            'schema': {
                'type': 'integer'
            }
        },
        'segments': {
            'anyof': [{
                'type': ['list', 'tuple'],
                'schema': {
                    'type': 'integer'
                }
            },
                {
                    'type': 'integer'
                }
            ]
        },
        'interval': {
            'anyof': [{
                'type': ['list', 'tuple'],
                'schema': {
                    'type': 'integer'
                }
            },
                {
                    'type': 'integer'
                }
            ]
        },
        'units': {
            'type': 'string',
            'allowed': ['m', 'km', 'mi'],
            'default': 'm'
        },
        'location_type': {
            'type': 'string',
            'allowed': ['start', 'destination'],
            'default': 'start'
        },
        'attributes': {
            'type': ['list', 'tuple'],
            'schema': {
                'type': 'string',
                'allowed': ['area', 'reachfactor', 'total_pop']
            }
        },
        'intersections': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        },
        'id': {
            'type': 'string'
        },
        'smoothing': {
            "type": "float",
            'min': 0,
            'max': 1
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _distance_matrix_validation(params, coords_len):
    schema = {
        'locations': {
            'anyof': [{
                'type': ['list', 'tuple'],
                'schema': {
                    'type': 'float'
                }
            },
                {
                    'type': ['list', 'tuple'],
                    'schema': {
                        'type': ['list', 'tuple'],
                        'schema': {
                            'type': 'float'
                        }
                    }
                }
            ],
            'required': True
        },
        'profile': {
            'type': 'string',
            'allowed': [
                'driving-car', 'driving-hgv', 'foot-walking', 'foot-hiking', 'cycling-regular',
                'cycling-road', 'cycling-safe', 'cycling-mountain', 'cycling-tour',
                'cycling-electric'
            ],
            'default': 'driving-car',
            'required': True
        },
        'sources': {
            'type': 'list',
            'schema': {
                'type': 'integer',
                'min': 0,
                'max': coords_len - 1
            }
        },
        'destinations': {
            'type': 'list',
            'schema': {
                'type': 'integer',
                'min': 0,
                'max': coords_len - 1
            }
        },
        'metrics': {
            'type': 'list',
            'schema': {
                'type': 'string'
            },
            'allowed': ['distance', 'duration']
        },
        'resolve_locations': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        },
        'units': {
            'type': 'string',
            'allowed': ['m', 'km', 'mi'],
            'default': 'm'
        },
        'optimized': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        },
        'id': {
            'type': 'string'
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _search_validation(params):
    schema = {
        'text': {
            'type': 'string',
            'required': True
        },
        'focus_point': {
            'type': 'list',
            'schema': {
                'type': 'float'
            }
        },
        'rect_min_x': {
            'type': 'float'
        },
        'rect_min_y': {
            'type': 'float'
        },
        'rect_max_x': {
            'type': 'float'
        },
        'rect_max_y': {
            'type': 'float'
        },
        'circle_point': {
            'type': 'list',
            'schema': {
                'type': 'float'
            }
        },
        'circle_radius': {
            'type': 'integer',
            'default': 50
        },
        'sources': {
            'type': 'list',
            'schema': {
                'type': 'string'
            },
            'allowed': ['osm', 'oa', 'wof', 'gn'],
            'default': ['osm', 'oa', 'wof', 'gn']
        },
        'layers': {
            'type': 'list',
            'schema': {
                'type': 'string'
            },
            'allowed': [
                'venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'
            ],
            'default': [
                'venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'
            ]
        },
        'country': {
            'type': 'string'
        },
        'size': {
            'type': 'integer',
            'default': 10
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _autocomplete_validation(params):
    schema = {
        'text': {
            'type': 'string',
            'required': True
        },
        'focus_point': {
            'type': 'list',
            'schema': {
                'type': 'float'
            }
        },
        'rect_min_x': {
            'type': 'float'
        },
        'rect_min_y': {
            'type': 'float'
        },
        'rect_max_x': {
            'type': 'float'
        },
        'rect_max_y': {
            'type': 'float'
        },
        'sources': {
            'type': 'list',
            'schema': {
                'type': 'string'
            },
            'allowed': ['osm', 'oa', 'wof', 'gn'],
            'default': ['osm', 'oa', 'wof', 'gn']
        },
        'layers': {
            'type': 'list',
            'schema': {
                'type': 'string'
            },
            'allowed': [
                'venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'
            ],
            'default': [
                'venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'
            ]
        },
        'country': {
            'type': 'string'
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _structured_validation(params):
    schema = {
        'address': {
            'type': 'string'
        },
        'neighbourhood': {
            'type': 'string'
        },
        'borough': {
            'type': 'string'
        },
        'locality': {
            'type': 'string'
        },
        'county': {
            'type': 'string'
        },
        'region': {
            'type': 'string'
        },
        'postalcode': {
            'type': 'integer'
        },
        'country': {
            'type': 'string'
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _reverse_validation(params):
    schema = {
        'point': {
            'type': ['list', 'tuple'],
            'schema': {
                'type': 'float'
            },
            'required': True
        },
        'circle_radius': {
            'type': 'integer'
        },
        'sources': {
            'type': ['list', 'tuple'],
            'schema': {
                'type': 'string'
            },
            'allowed': ['osm', 'oa', 'wof', 'gn'],
            'default': ['osm', 'oa', 'wof', 'gn']
        },
        'layers': {
            'type': ['list', 'tuple'],
            'schema': {
                'type': 'string'
            },
            'allowed': [
                'venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'
            ],
            'default': [
                'venue', 'address', 'street', 'neighbourhood', 'borough', 'localadmin', 'locality',
                'county', 'macrocounty', 'region', 'macroregion', 'country', 'coarse'
            ]
        },
        'country': {
            'type': 'string'
        },
        'size': {
            'type': 'integer',
            'default': 10
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _pois_validation(params):
    schema = {
        'request': {
            'type': 'string',
            'allowed': ['pois', 'list', 'stats'],
            'default': 'pois',
            'required': True
        },
        'bbox': {
            'type': 'list',
            'schema': {
                'type': 'list',
                'schema': {
                    'type': 'float',
                    'maxlength': 2
                }
            }
        },
        'geojson': {
            'type': 'dict',
            'schema': {
                'type': {
                    'type': 'string',
                    'allowed': ['Point', 'Polygon', 'LineString'],
                    'required': True,
                    'dependencies': 'coordinates'
                },
                'coordinates': {
                    'anyof': [{
                        'type': 'list',
                        'schema': {
                            'type': 'float',
                            'maxlength': 2
                        },
                        'dependencies': {
                            'type': 'Point'
                        }
                    },
                        {
                            'type': 'list',
                            'schema': {
                                'type': 'list',
                                'schema': {
                                    'type': 'float',
                                    'maxlength': 2
                                }
                            },
                            'dependencies': {
                                'type': ['LineString']
                            }
                        },
                        {
                            'type': 'list',
                            'schema': {
                                'type': 'list',
                                'schema': {
                                    'type': 'list',
                                    'schema': {
                                        'type': 'float',
                                        'maxlength': 2
                                    }
                                }
                            },
                            'dependencies': {
                                'type': ['Polygon']
                            }
                        }
                    ]
                },
            }
        },
        'buffer': {
            'type': 'integer',
            'default': 500
        },
        'filter_category_group_ids': {
            'type': 'list',
            'schema': {
                'type': 'integer'
            }
        },
        'filter_category_ids': {
            'type': 'list',
            'schema': {
                'type': 'integer'
            }
        },
        'filters_custom': {
            'type': 'dict',
            'schema': {
                'wheelchair': {
                    'type': 'list',
                    'schema': {
                        'type': 'string',
                        'allowed': ['yes', 'no', 'limited', 'designated']
                    }
                },
                'smoking': {
                    'type': 'list',
                    'schema': {
                        'type': 'string',
                        'allowed': ['dedicated', 'yes', 'no', 'separated', 'isolated',
                                    'outside'
                                    ]
                    }
                },
                'fee': {
                    'type': 'list',
                    'schema': {
                        'type': 'string',
                        'allowed': ['yes', 'no']
                    }
                },
                'name': {
                    'type': 'string'
                },
            }
        },
        'limit': {
            'type': 'integer',
            'max': 1000
        },
        'sortby': {
            'type': 'string',
            'allowed': ['category', 'distance']
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v


def _elevation_validation(params):
    schema = {
        'format_in': {
            'type': 'string',
            'allowed': ['geojson', 'point', 'polyline', 'encodedpolyline'],
            'required': True
        },
        'format_out': {
            'type': 'string',
            'allowed': ['geojson', 'point', 'polyline', 'encodedpolyline'],
            'default': 'geojson'
        },
        'dataset': {
            'type': 'string',
            'allowed': ['srtm'],
            'default': 'srtm'
        },
        'geometry': {
            'anyof': [{
                'type': 'dict',
                'schema': {
                    'type': {
                        'type': 'string',
                        'allowed': ['Point', 'LineString'],
                        'required': True
                    },
                    'coordinates': {
                        'anyof': [{
                            'type': 'list',
                            'schema': {
                                'type': 'float',
                                'minlength': 2,
                                'maxlength': 2
                            }
                        },
                            {
                                'type': 'list',
                                'schema': {
                                    'type': 'list',
                                    'schema': {
                                        'type': 'float',
                                        'minlength': 2,
                                        'maxlength': 2
                                    }
                                }
                            }
                        ],
                        'required': True
                    }
                },
                'dependencies': {
                    '^format_in': 'geojson'
                },
            },
                {
                    'type': 'list',
                    'schema': {
                        'type': 'float',
                        'minlength': 2,
                        'maxlength': 2
                    },
                    'dependencies': {
                        '^format_in': 'point'
                    }
                },
                {
                    'type': ['list', 'tuple'],
                    'schema': {
                        'type': ['list', 'tuple'],
                        'schema': {
                            'type': 'float',
                            'minlength': 2,
                            'maxlength': 2
                        }
                    },
                    'dependencies': {
                        '^format_in': 'polyline'
                    }
                },
                {
                    'type': 'string',
                    'dependencies': {
                        '^format_in': 'encodedpolyline'
                    }
                }
            ],
            'required': True
        },
        'validate': {
            'type': 'boolean'
        },
        'dry_run': {
            'anyof': [{
                'type': 'string',
                'allowed': ['true', 'false']
            },
                {
                    'type': 'boolean'
                }
            ]
        }
    }

    v.validate(params, schema)

    return v
