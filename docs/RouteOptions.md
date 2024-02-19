# RouteOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avoid_borders** | **str** | Specify which type of border crossing to avoid | [optional] 
**avoid_countries** | **list[str]** | List of countries to exclude from matrix with &#x60;driving-*&#x60; profiles. Can be used together with &#x60;&#x27;avoid_borders&#x27;: &#x27;controlled&#x27;&#x60;. &#x60;[ 11, 193 ]&#x60; would exclude Austria and Switzerland. List of countries and application examples can be found [here](https://GIScience.github.io/openrouteservice/documentation/routing-options/Country-List.html). Also, ISO standard country codes cna be used in place of the numerical ids, for example, DE or DEU for Germany.  | [optional] 
**avoid_features** | **list[str]** | List of features to avoid.  | [optional] 
**avoid_polygons** | [**RouteOptionsAvoidPolygons**](RouteOptionsAvoidPolygons.md) |  | [optional] 
**profile_params** | [**ProfileParameters**](ProfileParameters.md) |  | [optional] 
**round_trip** | [**RoundTripRouteOptions**](RoundTripRouteOptions.md) |  | [optional] 
**vehicle_type** | **str** | Definition of the vehicle type. | [optional] [default to 'hgv']

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

