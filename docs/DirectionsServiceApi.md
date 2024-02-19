# openrouteservice.DirectionsServiceApi

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_geo_json_route**](DirectionsServiceApi.md#get_geo_json_route) | **POST** /v2/directions/{profile}/geojson | Directions Service GeoJSON
[**get_json_route**](DirectionsServiceApi.md#get_json_route) | **POST** /v2/directions/{profile}/json | Directions Service JSON

# **get_geo_json_route**
> InlineResponse2003 get_geo_json_route(body, profile)

Directions Service GeoJSON

Returns a route between two or more locations for a selected profile and its settings as GeoJSON

### Example
```python
from __future__ import print_function
import time
import openrouteservice
from openrouteservice.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = openrouteservice.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openrouteservice.DirectionsServiceApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.DirectionsService() # DirectionsService | 
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
 **body** | [**DirectionsService**](DirectionsService.md)|  | 
 **profile** | **str**| Specifies the route profile. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/geo+json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **get_json_route**
> InlineResponse2004 get_json_route(body, profile)

Directions Service JSON

Returns a route between two or more locations for a selected profile and its settings as JSON

### Example
```python
from __future__ import print_function
import time
import openrouteservice
from openrouteservice.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = openrouteservice.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openrouteservice.DirectionsServiceApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.DirectionsService1() # DirectionsService1 | 
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
 **body** | [**DirectionsService1**](DirectionsService1.md)|  | 
 **profile** | **str**| Specifies the route profile. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

