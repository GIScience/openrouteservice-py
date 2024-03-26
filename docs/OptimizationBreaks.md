# OptimizationBreaks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | a string describing this break  | [optional] 
**id** | **int** | Integer used as unique identifier  | [optional] 
**max_load** | **list[float]** | Array of integers describing the maximum vehicle load for which this break can happen. An error is reported if two break objects have the same id for the same vehicle.  | [optional] 
**service** | **float** | break duration in seconds (defaults to 0)  | [optional] [default to 0]
**time_windows** | **list[list[int]]** | Array of time_window objects describing valid slots for break start and end, in week seconds, i.e. 28800 &#x3D; Mon, 8 AM.  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

