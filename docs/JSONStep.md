# JSONStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** | The distance for the step in metres. | [optional] 
**duration** | **float** | The duration for the step in seconds. | [optional] 
**exit_bearings** | **list[int]** | Contains the bearing of the entrance and all passed exits in a roundabout. | [optional] 
**exit_number** | **int** | Only for roundabouts. Contains the number of the exit to take. | [optional] 
**instruction** | **str** | The routing instruction text for the step. | [optional] 
**maneuver** | [**JSONIndividualRouteResponseManeuver**](JSONIndividualRouteResponseManeuver.md) |  | [optional] 
**name** | **str** | The name of the next street. | [optional] 
**type** | **int** | The [instruction](https://GIScience.github.io/openrouteservice/documentation/Instruction-Types.html) action for symbolisation purposes. | [optional] 
**way_points** | **list[int]** | List containing the indices of the steps start- and endpoint corresponding to the *geometry*. | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

