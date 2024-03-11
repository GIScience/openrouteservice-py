# InlineResponse2002Summary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | total cost for all routes | [optional] 
**delivery** | **float** | Total delivery for all routes | [optional] 
**distance** | **float** | total distance for all routes. Only provided when using the &#x60;-g&#x60; flag with &#x60;OSRM&#x60; | [optional] 
**duration** | **float** | total travel time for all routes | [optional] 
**pickup** | **float** | Total pickup for all routes | [optional] 
**priority** | **float** | total priority sum for all assigned tasks | [optional] 
**routes** | **float** | Number of routes in the solution  | [optional] 
**service** | **float** | total service time for all routes | [optional] 
**setup** | **float** | Total setup time for all routes  | [optional] 
**unassigned** | **int** | number of jobs that could not be served | [optional] 
**violations** | [**list[InlineResponse2002Violations]**](InlineResponse2002Violations.md) | array of violation objects for all routes | [optional] 
**waiting_time** | **float** | total waiting time for all routes | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

