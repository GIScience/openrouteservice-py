# openrouteservice.SnappingServiceApi

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default**](SnappingServiceApi.md#get_default) | **POST** /v2/snap/{profile} | Snapping Service
[**get_geo_json_snapping**](SnappingServiceApi.md#get_geo_json_snapping) | **POST** /v2/snap/{profile}/geojson | Snapping Service GeoJSON
[**get_json_snapping**](SnappingServiceApi.md#get_json_snapping) | **POST** /v2/snap/{profile}/json | Snapping Service JSON

# **get_default**
> InlineResponse2007 get_default(body, profile)

Snapping Service

Returns a list of points snapped to the nearest edge in the graph. In case an appropriate snapping point cannot be found within the specified search radius, \"null\" is returned. 

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
api_instance = openrouteservice.SnappingServiceApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.SnapProfileBody() # SnapProfileBody | 
profile = 'profile_example' # str | Specifies the route profile.

try:
    # Snapping Service
    api_response = api_instance.get_default(body, profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnappingServiceApi->get_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapProfileBody**](SnapProfileBody.md)|  | 
 **profile** | **str**| Specifies the route profile. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **get_geo_json_snapping**
> InlineResponse2008 get_geo_json_snapping(body, profile)

Snapping Service GeoJSON

Returns a GeoJSON FeatureCollection of points snapped to the nearest edge in the graph. In case an appropriate snapping point cannot be found within the specified search radius, it is omitted from the features array. The features provide the 'source_id' property, to match the results with the input location array (IDs start at 0). 

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
api_instance = openrouteservice.SnappingServiceApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.ProfileGeojsonBody() # ProfileGeojsonBody | 
profile = 'profile_example' # str | Specifies the profile.

try:
    # Snapping Service GeoJSON
    api_response = api_instance.get_geo_json_snapping(body, profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnappingServiceApi->get_geo_json_snapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProfileGeojsonBody**](ProfileGeojsonBody.md)|  | 
 **profile** | **str**| Specifies the profile. | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **get_json_snapping**
> InlineResponse2007 get_json_snapping(body, profile)

Snapping Service JSON

Returns a list of points snapped to the nearest edge in the graph. In case an appropriate snapping point cannot be found within the specified search radius, \"null\" is returned. 

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
api_instance = openrouteservice.SnappingServiceApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.ProfileJsonBody() # ProfileJsonBody | 
profile = 'profile_example' # str | Specifies the profile.

try:
    # Snapping Service JSON
    api_response = api_instance.get_json_snapping(body, profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnappingServiceApi->get_json_snapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProfileJsonBody**](ProfileJsonBody.md)|  | 
 **profile** | **str**| Specifies the profile. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

