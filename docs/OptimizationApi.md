# openrouteservice.OptimizationApi

> [!NOTE]  
> This documentation is automatically generated. Code examples might not work out of the box as not all required parameters are passed.

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**optimization_post**](OptimizationApi.md#optimization_post) | **POST** /optimization | Optimization Service

# **optimization_post**
> JSONResponse optimization_post(body)

Optimization Service

The optimization endpoint solves [Vehicle Routing Problems](https://en.wikipedia.org/wiki/Vehicle_routing_problem) and can be used to schedule multiple vehicles and jobs, respecting time windows, capacities and required skills.  This service is based on the excellent [Vroom project](https://github.com/VROOM-Project/vroom). Please also consult its [API documentation](https://github.com/VROOM-Project/vroom/blob/master/docs/API.md).  General Info: - The expected order for all coordinates arrays is `[lon, lat]` - All timings are in seconds - All distances are in meters - A `time_window` object is a pair of timestamps in the form `[start, end]` 

### Example
```python
from __future__ import print_function
import time
import openrouteservice
from openrouteservice.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openrouteservice.OptimizationApi(openrouteservice.apiClient(apiKey='YOUR_API_KEY'))
body = openrouteservice.OptimizationBody() # OptimizationBody | The request body of the optimization request.

try:
    # Optimization Service
    api_response = api_instance.optimization_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->optimization_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OptimizationBody**](OptimizationBody.md)| The request body of the optimization request. | 

### Return type

[**JSONResponse**](JSONResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

