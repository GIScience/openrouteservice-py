# OptimizationJobs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **list[int]** | Array describing multidimensional quantities  | [optional] 
**id** | **int** | an integer used as unique identifier  | [optional] 
**location** | **list[list[float]]** | coordinates array in &#x60;[lon, lat]&#x60;  | [optional] 
**location_index** | **object** | index of relevant row and column in custom matrix  | [optional] 
**service** | **object** | job service duration (defaults to 0), in seconds  | [optional] 
**skills** | **list[int]** | Array of integers defining mandatory skills for this job  | [optional] 
**time_windows** | **list[list[int]]** | Array of &#x60;time_window&#x60; arrays describing valid slots for job service start and end, in week seconds, i.e. 28800 &#x3D; Mon, 8 AM.  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

