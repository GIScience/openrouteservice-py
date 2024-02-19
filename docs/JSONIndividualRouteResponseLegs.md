# JSONIndividualRouteResponseLegs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrival** | **datetime** | Arrival date and time | [optional] 
**departure** | **datetime** | Departure date and time | [optional] 
**departure_location** | **str** | The departure location of the leg. | [optional] 
**distance** | **float** | The distance for the leg in metres. | [optional] 
**duration** | **float** | The duration for the leg in seconds. | [optional] 
**feed_id** | **str** | The feed ID this public transport leg based its information from. | [optional] 
**geometry** | **str** | The geometry of the leg. This is an encoded polyline. | [optional] 
**instructions** | [**list[JSONIndividualRouteResponseInstructions]**](JSONIndividualRouteResponseInstructions.md) | List containing the specific steps the segment consists of. | [optional] 
**is_in_same_vehicle_as_previous** | **bool** | Whether the legs continues in the same vehicle as the previous one. | [optional] 
**route_desc** | **str** | The route description of the leg (if provided in the GTFS data set). | [optional] 
**route_id** | **str** | The route ID of this public transport leg. | [optional] 
**route_long_name** | **str** | The public transport route name of the leg. | [optional] 
**route_short_name** | **str** | The public transport route name (short version) of the leg. | [optional] 
**route_type** | **int** | The route type of the leg (if provided in the GTFS data set). | [optional] 
**stops** | [**list[JSONIndividualRouteResponseStops]**](JSONIndividualRouteResponseStops.md) | List containing the stops the along the leg. | [optional] 
**trip_headsign** | **str** | The headsign of the public transport vehicle of the leg. | [optional] 
**trip_id** | **str** | The trip ID of this public transport leg. | [optional] 
**type** | **str** | The type of the leg, possible values are currently &#x27;walk&#x27; and &#x27;pt&#x27;. | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

