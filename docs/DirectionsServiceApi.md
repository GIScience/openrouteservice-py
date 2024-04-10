# openrouteservice.DirectionsServiceApi

> [!NOTE]  
> This documentation is automatically generated. Code examples might not work out of the box as not all required parameters are passed.

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_geo_json_route**](DirectionsServiceApi.md#get_geo_json_route) | **POST** /v2/directions/{profile}/geojson | Directions Service GeoJSON
[**get_json_route**](DirectionsServiceApi.md#get_json_route) | **POST** /v2/directions/{profile}/json | Directions Service JSON

# **get_geo_json_route**
> JSONResponse get_geo_json_route(body, profile)

Directions Service GeoJSON

Returns a route between two or more locations for a selected profile and its settings as GeoJSON

### Example
```python
from __future__ import print_function
import time
import openrouteservice
from openrouteservice.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openrouteservice.DirectionsServiceApi(openrouteservice.apiClient(apiKey='YOUR_API_KEY'))
body = openrouteservice.DirectionsServiceBody() # DirectionsServiceBody | 
profile = 'profile_example' # str | Specifies the route profile.

try:
    # Directions Service GeoJSON
    api_response = api_instance.get_geo_json_route(body, profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsServiceApi->get_geo_json_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectionsServiceBody**](DirectionsServiceBody.md)|  | 
 **profile** | **str**| Specifies the route profile. | 

### Return type

[**JSONResponse**](JSONResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/geo+json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **get_json_route**
> JSONResponse get_json_route(body, profile)

Directions Service JSON

Returns a route between two or more locations for a selected profile and its settings as JSON

### Example
```python
from __future__ import print_function
import time
import openrouteservice
from openrouteservice.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openrouteservice.DirectionsServiceApi(openrouteservice.apiClient(apiKey='YOUR_API_KEY'))
body = openrouteservice.DirectionsServiceBody() # DirectionsServiceBody | 
profile = 'profile_example' # str | Specifies the route profile.

try:
    # Directions Service JSON
    api_response = api_instance.get_json_route(body, profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectionsServiceApi->get_json_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectionsServiceBody**](DirectionsServiceBody.md)|  | 
 **profile** | **str**| Specifies the route profile. | 

### Return type

[**JSONResponse**](JSONResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

