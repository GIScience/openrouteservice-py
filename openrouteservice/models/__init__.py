# coding: utf-8

# flake8: noqa
"""
    Openrouteservice

    This is the openrouteservice API documentation for ORS Core-Version 7.1.1. Documentations for [older Core-Versions](https://github.com/GIScience/openrouteservice-docs/releases) can be rendered with the [Swagger-Editor](https://editor-next.swagger.io/).  # noqa: E501

    OpenAPI spec version: 7.1.1
    Contact: support@smartmobility.heigit.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from openrouteservice.models.alternative_routes import AlternativeRoutes
from openrouteservice.models.directions_service import DirectionsService
from openrouteservice.models.directions_service1 import DirectionsService1
from openrouteservice.models.elevation_line_body import ElevationLineBody
from openrouteservice.models.elevation_point_body import ElevationPointBody
from openrouteservice.models.geo_json_features_object import GeoJSONFeaturesObject
from openrouteservice.models.geo_json_geometry_object import GeoJSONGeometryObject
from openrouteservice.models.geo_json_properties_object import GeoJSONPropertiesObject
from openrouteservice.models.geo_json_properties_object_category_ids import GeoJSONPropertiesObjectCategoryIds
from openrouteservice.models.geo_json_properties_object_category_ids_category_id import GeoJSONPropertiesObjectCategoryIdsCategoryId
from openrouteservice.models.geo_json_properties_object_osm_tags import GeoJSONPropertiesObjectOsmTags
from openrouteservice.models.geocode_response import GeocodeResponse
from openrouteservice.models.inline_response200 import InlineResponse200
from openrouteservice.models.inline_response2001 import InlineResponse2001
from openrouteservice.models.inline_response2001_geometry import InlineResponse2001Geometry
from openrouteservice.models.inline_response2002 import InlineResponse2002
from openrouteservice.models.inline_response2002_routes import InlineResponse2002Routes
from openrouteservice.models.inline_response2002_steps import InlineResponse2002Steps
from openrouteservice.models.inline_response2002_summary import InlineResponse2002Summary
from openrouteservice.models.inline_response2002_unassigned import InlineResponse2002Unassigned
from openrouteservice.models.inline_response2002_violations import InlineResponse2002Violations
from openrouteservice.models.inline_response2003 import InlineResponse2003
from openrouteservice.models.inline_response2003_metadata import InlineResponse2003Metadata
from openrouteservice.models.inline_response2004 import InlineResponse2004
from openrouteservice.models.inline_response2004_extras import InlineResponse2004Extras
from openrouteservice.models.inline_response2004_instructions import InlineResponse2004Instructions
from openrouteservice.models.inline_response2004_legs import InlineResponse2004Legs
from openrouteservice.models.inline_response2004_maneuver import InlineResponse2004Maneuver
from openrouteservice.models.inline_response2004_routes import InlineResponse2004Routes
from openrouteservice.models.inline_response2004_segments import InlineResponse2004Segments
from openrouteservice.models.inline_response2004_stops import InlineResponse2004Stops
from openrouteservice.models.inline_response2004_summary import InlineResponse2004Summary
from openrouteservice.models.inline_response2004_summary1 import InlineResponse2004Summary1
from openrouteservice.models.inline_response2004_warnings import InlineResponse2004Warnings
from openrouteservice.models.inline_response2005 import InlineResponse2005
from openrouteservice.models.inline_response2005_features import InlineResponse2005Features
from openrouteservice.models.inline_response2005_geometry import InlineResponse2005Geometry
from openrouteservice.models.inline_response2005_metadata import InlineResponse2005Metadata
from openrouteservice.models.inline_response2005_metadata_engine import InlineResponse2005MetadataEngine
from openrouteservice.models.inline_response2006 import InlineResponse2006
from openrouteservice.models.inline_response2006_destinations import InlineResponse2006Destinations
from openrouteservice.models.inline_response2006_metadata import InlineResponse2006Metadata
from openrouteservice.models.inline_response2006_sources import InlineResponse2006Sources
from openrouteservice.models.inline_response2007 import InlineResponse2007
from openrouteservice.models.inline_response2007_locations import InlineResponse2007Locations
from openrouteservice.models.inline_response2007_metadata import InlineResponse2007Metadata
from openrouteservice.models.inline_response2008 import InlineResponse2008
from openrouteservice.models.inline_response2008_features import InlineResponse2008Features
from openrouteservice.models.inline_response2008_geometry import InlineResponse2008Geometry
from openrouteservice.models.inline_response2008_properties import InlineResponse2008Properties
from openrouteservice.models.inline_response200_geometry import InlineResponse200Geometry
from openrouteservice.models.isochrones_profile_body import IsochronesProfileBody
from openrouteservice.models.matrix_profile_body import MatrixProfileBody
from openrouteservice.models.openpoiservice_poi_request import OpenpoiservicePoiRequest
from openrouteservice.models.openpoiservice_poi_response import OpenpoiservicePoiResponse
from openrouteservice.models.optimization_body import OptimizationBody
from openrouteservice.models.optimization_breaks import OptimizationBreaks
from openrouteservice.models.optimization_costs import OptimizationCosts
from openrouteservice.models.optimization_jobs import OptimizationJobs
from openrouteservice.models.optimization_matrices import OptimizationMatrices
from openrouteservice.models.optimization_matrices_cyclingelectric import OptimizationMatricesCyclingelectric
from openrouteservice.models.optimization_options import OptimizationOptions
from openrouteservice.models.optimization_steps import OptimizationSteps
from openrouteservice.models.optimization_vehicles import OptimizationVehicles
from openrouteservice.models.pois_filters import PoisFilters
from openrouteservice.models.pois_geometry import PoisGeometry
from openrouteservice.models.profile_geojson_body import ProfileGeojsonBody
from openrouteservice.models.profile_json_body import ProfileJsonBody
from openrouteservice.models.profile_parameters import ProfileParameters
from openrouteservice.models.profile_parameters_restrictions import ProfileParametersRestrictions
from openrouteservice.models.profile_weightings import ProfileWeightings
from openrouteservice.models.round_trip_route_options import RoundTripRouteOptions
from openrouteservice.models.route_options import RouteOptions
from openrouteservice.models.route_options_avoid_polygons import RouteOptionsAvoidPolygons
from openrouteservice.models.snap_profile_body import SnapProfileBody
