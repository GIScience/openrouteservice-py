# InlineResponse2002Routes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | cost for this route | [optional] 
**delivery** | **list[int]** | Total delivery for tasks in this route | [optional] 
**description** | **str** | vehicle description, if provided in input  | [optional] 
**distance** | **float** | total route distance. Only provided when using the &#x60;-g&#x60; flag | [optional] 
**duration** | **float** | total travel time for this route | [optional] 
**geometry** | **str** | polyline encoded route geometry. Only provided when using the &#x60;-g&#x60; flag | [optional] 
**pickup** | **list[int]** | total pickup for tasks in this route | [optional] 
**service** | **float** | total service time for this route | [optional] 
**steps** | [**list[InlineResponse2002Steps]**](InlineResponse2002Steps.md) | array of &#x60;step&#x60; objects | [optional] 
**vehicle** | **int** | id of the vehicle assigned to this route | [optional] 
**waiting_time** | **float** | total waiting time for this route | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

