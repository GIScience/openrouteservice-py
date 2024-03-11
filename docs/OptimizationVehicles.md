# OptimizationVehicles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breaks** | [**list[OptimizationBreaks]**](OptimizationBreaks.md) | An array of &#x60;break&#x60; objects  | [optional] 
**capacity** | **list[int]** | Array of integers describing multidimensional quantities.  | [optional] 
**costs** | [**OptimizationCosts**](OptimizationCosts.md) |  | [optional] 
**description** | **str** | a string describing this vehicle  | [optional] 
**end** | **list[float]** | End coordinates array in &#x60;[lon, lat]&#x60; format. If left blank, the optimization engine will identify the optimal end point.  | [optional] 
**end_index** | **object** | Index of relevant row and column in custom matrix.  | [optional] 
**id** | **int** | Integer used as unique identifier  | [optional] 
**max_distance** | **float** | an integer defining the maximum distance for this vehicle  | [optional] 
**max_tasks** | **float** | an integer defining the maximum number of tasks in a route for this vehicle  | [optional] 
**max_travel_time** | **float** | an integer defining the maximum travel time for this vehicle  | [optional] 
**profile** | **str** | The ORS routing profile for the vehicle.  | [optional] 
**skills** | **list[int]** | Array of integers defining skills for this vehicle  | [optional] 
**speed_factor** | **float** | A double value in the range (0, 5] used to scale all vehicle travel times (defaults to 1.). The respected precision is limited to two digits after the decimal point.  | [optional] 
**start** | **list[float]** | Start coordinates array in &#x60;[lon, lat]&#x60; format. If left blank, the optimization engine will identify the optimal start point.  | [optional] 
**start_index** | **object** | Index of relevant row and column in custom matrix.  | [optional] 
**steps** | [**list[OptimizationSteps]**](OptimizationSteps.md) |  | [optional] 
**time_window** | **list[int]** | A &#x60;time_window&#x60; array describing working hours for this vehicle, in week seconds, i.e. 28800 &#x3D; Mon, 8 AM.  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

