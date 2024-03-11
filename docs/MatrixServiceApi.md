# openrouteservice.MatrixServiceApi

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default1**](MatrixServiceApi.md#get_default1) | **POST** /v2/matrix/{profile} | Matrix Service

# **get_default1**
> InlineResponse2006 get_default1(body, profile)

Matrix Service

Returns duration or distance matrix for multiple source and destination points. By default a square duration matrix is returned where every point in locations is paired with each other. The result is null if a value can’t be determined.

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
api_instance = openrouteservice.MatrixServiceApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.MatrixProfileBody() # MatrixProfileBody | 
profile = 'profile_example' # str | Specifies the matrix profile.

try:
    # Matrix Service
    api_response = api_instance.get_default1(body, profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatrixServiceApi->get_default1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatrixProfileBody**](MatrixProfileBody.md)|  | 
 **profile** | **str**| Specifies the matrix profile. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

