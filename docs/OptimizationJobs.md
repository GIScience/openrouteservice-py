# OptimizationJobs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery** | **list[float]** | an array of integers describing multidimensional quantities for delivery  | [optional] 
**description** | **str** | a string describing this job  | [optional] 
**id** | **int** | an integer used as unique identifier  | [optional] 
**location** | **list[list[float]]** | coordinates array in &#x60;[lon, lat]&#x60;  | [optional] 
**location_index** | **object** | index of relevant row and column in custom matrix  | [optional] 
**pickup** | **list[float]** | an array of integers describing multidimensional quantities for pickup  | [optional] 
**priority** | **float** | an integer in the range [0, 100] describing priority level (defaults to 0)  | [optional] [default to 0]
**service** | **object** | job service duration (defaults to 0), in seconds  | [optional] 
**setup** | **float** | job setup duration (defaults to 0), in seconds  | [optional] 
**skills** | **list[int]** | Array of integers defining mandatory skills for this job  | [optional] 
**time_windows** | **list[list[int]]** | Array of &#x60;time_window&#x60; arrays describing valid slots for job service start and end, in week seconds, i.e. 28800 &#x3D; Mon, 8 AM.  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

