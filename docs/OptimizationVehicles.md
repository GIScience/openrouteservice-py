# OptimizationVehicles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **list[int]** | Array of integers describing multidimensional quantities.  | [optional] 
**end** | **list[float]** | End coordinates array in &#x60;[lon, lat]&#x60; format. If left blank, the optimization engine will identify the optimal end point.  | [optional] 
**end_index** | **object** | Index of relevant row and column in custom matrix.  | [optional] 
**id** | **int** | Integer used as unique identifier  | [optional] 
**profile** | **str** | The ORS routing profile for the vehicle.  | [optional] 
**skills** | **list[int]** | Array of integers defining skills for this vehicle  | [optional] 
**start** | **list[float]** | Start coordinates array in &#x60;[lon, lat]&#x60; format. If left blank, the optimization engine will identify the optimal start point.  | [optional] 
**start_index** | **object** | Index of relevant row and column in custom matrix.  | [optional] 
**time_window** | **list[int]** | A &#x60;time_window&#x60; array describing working hours for this vehicle, in week seconds, i.e. 28800 &#x3D; Mon, 8 AM.  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

