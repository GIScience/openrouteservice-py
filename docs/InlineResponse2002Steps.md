# InlineResponse2002Steps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrival** | **float** | estimated time of arrival at this step in seconds | [optional] 
**description** | **str** | step description, if provided in input  | [optional] 
**distance** | **float** | traveled distance upon arrival at this step. Only provided when using the &#x60;-g&#x60; flag | [optional] 
**duration** | **float** | cumulated travel time upon arrival at this step in seconds | [optional] 
**id** | **int** | id of the task performed at this step, only provided if type value is &#x60;job&#x60;, &#x60;pickup&#x60;, &#x60;delivery&#x60; or &#x60;break&#x60;  | [optional] 
**load** | **int** | vehicle load after step completion (with capacity constraints)  | [optional] 
**location** | **list[float]** | coordinates array for this step (if provided in input) | [optional] 
**service** | **float** | service time at this step  | [optional] 
**setup** | **float** | setup time at this step  | [optional] 
**type** | **str** | string that is either &#x60;start&#x60;, &#x60;job&#x60; or &#x60;end&#x60; | [optional] 
**violations** | [**list[InlineResponse2002Violations]**](InlineResponse2002Violations.md) | array of violation objects for this step | [optional] 
**waiting_time** | **float** | waiting time upon arrival at this step, only provided if &#x60;type&#x60; value is &#x60;job&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

