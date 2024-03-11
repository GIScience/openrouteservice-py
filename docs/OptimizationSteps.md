# OptimizationSteps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | id of the task to be performed at this step if &#x60;type&#x60; value is not &#x60;start&#x60; or &#x60;end&#x60;  | [optional] 
**service_after** | **float** | hard constraint on service time lower bound (as absolute or relative timestamp)  | [optional] 
**service_at** | **float** | hard constraint on service time (as absolute or relative timestamp)  | [optional] 
**service_before** | **float** | hard constraint on service time upper bound (as absolute or relative timestamp)  | [optional] 
**type** | **str** | step type (either start, job, pickup, delivery, break or end)]  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

