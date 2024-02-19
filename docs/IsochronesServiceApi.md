# openrouteservice.IsochronesServiceApi

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_isochrones**](IsochronesServiceApi.md#get_default_isochrones) | **POST** /v2/isochrones/{profile} | Isochrones Service

# **get_default_isochrones**
> InlineResponse2005 get_default_isochrones(body, profile)

Isochrones Service

The Isochrone Service supports time and distance analyses for one single or multiple locations. You may also specify the isochrone interval or provide multiple exact isochrone range values. This service allows the same range of profile options as the /directions endpoint, which help you to further customize your request to obtain a more detailed reachability area response.

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
api_instance = openrouteservice.IsochronesServiceApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.IsochronesProfileBody() # IsochronesProfileBody | 
profile = 'profile_example' # str | Specifies the route profile.

try:
    # Isochrones Service
    api_response = api_instance.get_default_isochrones(body, profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IsochronesServiceApi->get_default_isochrones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsochronesProfileBody**](IsochronesProfileBody.md)|  | 
 **profile** | **str**| Specifies the route profile. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/geo+json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

