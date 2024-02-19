# JSONIndividualRouteResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrival** | **datetime** | Arrival date and time | [optional] 
**bbox** | **list[float]** | A bounding box which contains the entire route | [optional] 
**departure** | **datetime** | Departure date and time | [optional] 
**extras** | [**dict(str, JSONIndividualRouteResponseExtras)**](JSONIndividualRouteResponseExtras.md) | List of extra info objects representing the extra info items that were requested for the route. | [optional] 
**geometry** | **str** | The geometry of the route. For JSON route responses this is an encoded polyline. | [optional] 
**legs** | [**list[JSONIndividualRouteResponseLegs]**](JSONIndividualRouteResponseLegs.md) | List containing the legs the route consists of. | [optional] 
**segments** | [**list[JSONIndividualRouteResponseSegments]**](JSONIndividualRouteResponseSegments.md) | List containing the segments and its corresponding steps which make up the route. | [optional] 
**summary** | [**JSONIndividualRouteResponseSummary**](JSONIndividualRouteResponseSummary.md) |  | [optional] 
**warnings** | [**list[JSONIndividualRouteResponseWarnings]**](JSONIndividualRouteResponseWarnings.md) | List of warnings that have been generated for the route | [optional] 
**way_points** | **list[int]** | List containing the indices of way points corresponding to the *geometry*. | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

