# InlineResponse2002Steps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrival** | **float** | estimated time of arrival at this step in seconds | [optional] 
**distance** | **float** | traveled distance upon arrival at this step. Only provided when using the &#x60;-g&#x60; flag with &#x60;OSRM&#x60; | [optional] 
**duration** | **float** | cumulated travel time upon arrival at this step in seconds | [optional] 
**job** | **int** | id of the job performed at this step, only provided if &#x60;type&#x60; value is &#x60;job&#x60; | [optional] 
**location** | **list[float]** | coordinates array for this step (if provided in input) | [optional] 
**service** | **float** | service time at this step, only provided if &#x60;type&#x60; value is &#x60;job&#x60; | [optional] 
**type** | **str** | string that is either &#x60;start&#x60;, &#x60;job&#x60; or &#x60;end&#x60; | [optional] 
**waiting_time** | **float** | waiting time upon arrival at this step, only provided if &#x60;type&#x60; value is &#x60;job&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

