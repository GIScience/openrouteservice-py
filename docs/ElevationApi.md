# openrouteservice.ElevationApi

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevation_line_post**](ElevationApi.md#elevation_line_post) | **POST** /elevation/line | Elevation Line Service
[**elevation_point_get**](ElevationApi.md#elevation_point_get) | **GET** /elevation/point | Elevation Point Service
[**elevation_point_post**](ElevationApi.md#elevation_point_post) | **POST** /elevation/point | Elevation Point Service

# **elevation_line_post**
> InlineResponse200 elevation_line_post(body)

Elevation Line Service

This endpoint can take planar 2D line objects and enrich them with elevation from a variety of datasets.  The input and output formats are:   * GeoJSON   * Polyline   * <a href="https://developers.google.com/maps/documentation/utilities/polylinealgorithm">Google's Encoded polyline</a> with coordinate precision 5 or 6  Example: ```   # POST LineString as polyline   curl -XPOST https://api.openrouteservice.org/elevation/line     -H 'Content-Type: application/json' \\     -H 'Authorization: INSERT_YOUR_KEY     -d '{       \"format_in\": \"polyline\",       \"format_out\": \"encodedpolyline5\",       \"geometry\": [[13.349762, 38.112952],                    [12.638397, 37.645772]]         }' ``` 

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
api_instance = openrouteservice.ElevationApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.ElevationLineBody() # ElevationLineBody | Query the elevation of a line in various formats.

try:
    # Elevation Line Service
    api_response = api_instance.elevation_line_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevationApi->elevation_line_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElevationLineBody**](ElevationLineBody.md)| Query the elevation of a line in various formats. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **elevation_point_get**
> InlineResponse2001 elevation_point_get(geometry, format_out=format_out, dataset=dataset)

Elevation Point Service

This endpoint can take a 2D point and enrich it with elevation from a variety of datasets.  The output formats are:   * GeoJSON   * Point  Example: ```   # GET point   curl -XGET https://localhost:5000/elevation/point?geometry=13.349762,38.11295 ``` 

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
api_instance = openrouteservice.ElevationApi(openrouteservice.ApiClient(configuration))
geometry = [3.4] # list[float] | The point to be queried, in comma-separated lon,lat values, e.g. [13.349762, 38.11295]
format_out = 'geojson' # str | The output format to be returned. (optional) (default to geojson)
dataset = 'srtm' # str | The elevation dataset to be used. (optional) (default to srtm)

try:
    # Elevation Point Service
    api_response = api_instance.elevation_point_get(geometry, format_out=format_out, dataset=dataset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevationApi->elevation_point_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geometry** | [**list[float]**](float.md)| The point to be queried, in comma-separated lon,lat values, e.g. [13.349762, 38.11295] | 
 **format_out** | **str**| The output format to be returned. | [optional] [default to geojson]
 **dataset** | **str**| The elevation dataset to be used. | [optional] [default to srtm]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **elevation_point_post**
> InlineResponse2001 elevation_point_post(body)

Elevation Point Service

This endpoint can take a 2D point and enrich it with elevation from a variety of datasets.  The input and output formats are:   * GeoJSON   * Point  Example: ```   # POST point as GeoJSON   # https://api.openrouteservice.org/elevation/point?api_key=YOUR-KEY   {     \"format_in\": \"geojson\",     \"format_out\": \"geojson\",     \"geometry\": {       \"coordinates\": [13.349762, 38.11295],       \"type\": \"Point\"     }   } ``` 

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
api_instance = openrouteservice.ElevationApi(openrouteservice.ApiClient(configuration))
body = openrouteservice.ElevationPointBody() # ElevationPointBody | Query the elevation of a point in various formats.

try:
    # Elevation Point Service
    api_response = api_instance.elevation_point_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElevationApi->elevation_point_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElevationPointBody**](ElevationPointBody.md)| Query the elevation of a point in various formats. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

