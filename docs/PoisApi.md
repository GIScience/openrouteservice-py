# openrouteservice.PoisApi

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pois_post**](PoisApi.md#pois_post) | **POST** /pois | Pois Service

# **pois_post**
> OpenpoiservicePoiResponse pois_post(body)

Pois Service

Returns points of interest in the area surrounding a geometry which can either be a bounding box, polygon or buffered linestring or point. Find more examples on [github](https://github.com/GIScience/openpoiservice). 

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
api_instance = openrouteservice.PoisApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.OpenpoiservicePoiRequest() # OpenpoiservicePoiRequest | body for a post request

try:
    # Pois Service
    api_response = api_instance.pois_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoisApi->pois_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenpoiservicePoiRequest**](OpenpoiservicePoiRequest.md)| body for a post request | 

### Return type

[**OpenpoiservicePoiResponse**](OpenpoiservicePoiResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

