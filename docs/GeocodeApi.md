# openrouteservice.GeocodeApi

All URIs are relative to *https://api.openrouteservice.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geocode_autocomplete_get**](GeocodeApi.md#geocode_autocomplete_get) | **GET** /geocode/autocomplete | Geocode Autocomplete Service
[**geocode_reverse_get**](GeocodeApi.md#geocode_reverse_get) | **GET** /geocode/reverse | Reverse Geocode Service
[**geocode_search_get**](GeocodeApi.md#geocode_search_get) | **GET** /geocode/search | Forward Geocode Service
[**geocode_search_structured_get**](GeocodeApi.md#geocode_search_structured_get) | **GET** /geocode/search/structured | Structured Forward Geocode Service (beta)

# **geocode_autocomplete_get**
> GeocodeResponse geocode_autocomplete_get(text, focus_point_lon=focus_point_lon, focus_point_lat=focus_point_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_country=boundary_country, sources=sources, layers=layers)

Geocode Autocomplete Service

**Requests should be throttled when using this endpoint!** *Be aware that Responses are asynchronous.* Returns a JSON formatted list of objects corresponding to the search input. `boundary.*`-parameters can be combined if they are overlapping. **The interactivity for this enpoint is experimental!** [Please refer to this external Documentation](https://github.com/pelias/documentation/blob/master/autocomplete.md) 

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
api_instance = openrouteservice.GeocodeApi(openrouteservice.ApiClient(configuration))
text = 'text_example' # str | Name of location, street address or postal code. 
focus_point_lon = 3.4 # float | Longitude of the `focus.point`. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance.  Use with `focus.point.lat`.  (optional)
focus_point_lat = 3.4 # float | Latitude of the `focus.point`. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance. Use with `focus.point.lon`.  (optional)
boundary_rect_min_lon = 3.4 # float | Left border of rectangular boundary to narrow results.  (optional)
boundary_rect_min_lat = 3.4 # float | Bottom border of rectangular boundary to narrow results.  (optional)
boundary_rect_max_lon = 3.4 # float | Right border of rectangular boundary to narrow results.  (optional)
boundary_rect_max_lat = 3.4 # float | Top border of rectangular boundary to narrow results.  (optional)
boundary_country = 'boundary_country_example' # str | Restrict results to single country. Possible values are [alpha-2 and alpha-3 country codes](https://en.wikipedia.org/wiki/ISO_3166-1). Example: `DEU` or `DE` for Germany.  (optional)
sources = ['[\"osm\",\"oa\",\"gn\",\"wof\"]'] # list[str] | Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [`openstreetmap(osm)`](http://www.openstreetmap.org/), [`openaddresses(oa)`](http://openaddresses.io/), [`whosonfirst(wof)`](https://whosonfirst.org/), [`geonames(gn)`](http://www.geonames.org/).  (optional) (default to ["osm","oa","gn","wof"])
layers = ['layers_example'] # list[str] | Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   `venue`|points of interest, businesses, things with walls|   `address`|places with a street address|   `street`|streets,roads,highways|   `neighbourhood`|social communities, neighbourhoods|   `borough`|a local administrative boundary, currently only used for New York City|   `localadmin`|local administrative boundaries|   `locality`|towns, hamlets, cities|   `county`|official governmental area; usually bigger than a locality, almost always smaller than a region|   `macrocounty`|a related group of counties. Mostly in Europe.|   `region`|states and provinces|   `macroregion`|a related group of regions. Mostly in Europe|   `country`|places that issue passports, nations, nation-states|   `coarse`|alias for simultaneously using all administrative layers (everything except `venue` and `address`)|  (optional)

try:
    # Geocode Autocomplete Service
    api_response = api_instance.geocode_autocomplete_get(text, focus_point_lon=focus_point_lon, focus_point_lat=focus_point_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_country=boundary_country, sources=sources, layers=layers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeocodeApi->geocode_autocomplete_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Name of location, street address or postal code.  | 
 **focus_point_lon** | **float**| Longitude of the &#x60;focus.point&#x60;. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance.  Use with &#x60;focus.point.lat&#x60;.  | [optional] 
 **focus_point_lat** | **float**| Latitude of the &#x60;focus.point&#x60;. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance. Use with &#x60;focus.point.lon&#x60;.  | [optional] 
 **boundary_rect_min_lon** | **float**| Left border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_min_lat** | **float**| Bottom border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_max_lon** | **float**| Right border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_max_lat** | **float**| Top border of rectangular boundary to narrow results.  | [optional] 
 **boundary_country** | **str**| Restrict results to single country. Possible values are [alpha-2 and alpha-3 country codes](https://en.wikipedia.org/wiki/ISO_3166-1). Example: &#x60;DEU&#x60; or &#x60;DE&#x60; for Germany.  | [optional] 
 **sources** | [**list[str]**](str.md)| Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [&#x60;openstreetmap(osm)&#x60;](http://www.openstreetmap.org/), [&#x60;openaddresses(oa)&#x60;](http://openaddresses.io/), [&#x60;whosonfirst(wof)&#x60;](https://whosonfirst.org/), [&#x60;geonames(gn)&#x60;](http://www.geonames.org/).  | [optional] [default to [&quot;osm&quot;,&quot;oa&quot;,&quot;gn&quot;,&quot;wof&quot;]]
 **layers** | [**list[str]**](str.md)| Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   &#x60;venue&#x60;|points of interest, businesses, things with walls|   &#x60;address&#x60;|places with a street address|   &#x60;street&#x60;|streets,roads,highways|   &#x60;neighbourhood&#x60;|social communities, neighbourhoods|   &#x60;borough&#x60;|a local administrative boundary, currently only used for New York City|   &#x60;localadmin&#x60;|local administrative boundaries|   &#x60;locality&#x60;|towns, hamlets, cities|   &#x60;county&#x60;|official governmental area; usually bigger than a locality, almost always smaller than a region|   &#x60;macrocounty&#x60;|a related group of counties. Mostly in Europe.|   &#x60;region&#x60;|states and provinces|   &#x60;macroregion&#x60;|a related group of regions. Mostly in Europe|   &#x60;country&#x60;|places that issue passports, nations, nation-states|   &#x60;coarse&#x60;|alias for simultaneously using all administrative layers (everything except &#x60;venue&#x60; and &#x60;address&#x60;)|  | [optional] 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **geocode_reverse_get**
> GeocodeResponse geocode_reverse_get(point_lon, point_lat, boundary_circle_radius=boundary_circle_radius, size=size, layers=layers, sources=sources, boundary_country=boundary_country)

Reverse Geocode Service

Returns the next enclosing object with an address tag which surrounds the given coordinate. **The interactivity for this enpoint is experimental!** [Please refer to this external Documentation](https://github.com/pelias/documentation/blob/master/reverse.md#reverse-geocoding) 

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
api_instance = openrouteservice.GeocodeApi(openrouteservice.ApiClient(configuration))
point_lon = 3.4 # float | Longitude of the coordinate to query. 
point_lat = 48.858268 # float | Latitude of the coordinate to query.  (default to 48.858268)
boundary_circle_radius = 1 # float | Restrict search to circular region around `point.lat/point.lon`. Value in kilometers.  (optional) (default to 1)
size = 10 # int | Set the number of returned results.  (optional) (default to 10)
layers = ['layers_example'] # list[str] | Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   `venue`|points of interest, businesses, things with walls|   `address`|places with a street address|   `street`|streets,roads,highways|   `neighbourhood`|social communities, neighbourhoods|   `locality`|towns, hamlets, cities|   `borough`|a local administrative boundary, currently only used for New York City|   `localadmin`|local administrative boundaries|   `county`|official governmental area; usually bigger than a locality, almost always smaller than a region|   `macrocounty`|a related group of counties. Mostly in Europe.|   `region`|states and provinces|   `macroregion`|a related group of regions. Mostly in Europe|   `country`|places that issue passports, nations, nation-states|   `coarse`|alias for simultaneously using all administrative layers (everything except `venue` and `address`)|  (optional)
sources = ['[\"osm\",\"oa\",\"gn\",\"wof\"]'] # list[str] | Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [`openstreetmap(osm)`](http://www.openstreetmap.org/), [`openaddresses(oa)`](http://openaddresses.io/), [`whosonfirst(wof)`](https://whosonfirst.org/), [`geonames(gn)`](http://www.geonames.org/).  (optional) (default to ["osm","oa","gn","wof"])
boundary_country = 'boundary_country_example' # str | Restrict search to country by [alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or [alpha 3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) codes.  (optional)

try:
    # Reverse Geocode Service
    api_response = api_instance.geocode_reverse_get(point_lon, point_lat, boundary_circle_radius=boundary_circle_radius, size=size, layers=layers, sources=sources, boundary_country=boundary_country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeocodeApi->geocode_reverse_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_lon** | **float**| Longitude of the coordinate to query.  | 
 **point_lat** | **float**| Latitude of the coordinate to query.  | [default to 48.858268]
 **boundary_circle_radius** | **float**| Restrict search to circular region around &#x60;point.lat/point.lon&#x60;. Value in kilometers.  | [optional] [default to 1]
 **size** | **int**| Set the number of returned results.  | [optional] [default to 10]
 **layers** | [**list[str]**](str.md)| Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   &#x60;venue&#x60;|points of interest, businesses, things with walls|   &#x60;address&#x60;|places with a street address|   &#x60;street&#x60;|streets,roads,highways|   &#x60;neighbourhood&#x60;|social communities, neighbourhoods|   &#x60;locality&#x60;|towns, hamlets, cities|   &#x60;borough&#x60;|a local administrative boundary, currently only used for New York City|   &#x60;localadmin&#x60;|local administrative boundaries|   &#x60;county&#x60;|official governmental area; usually bigger than a locality, almost always smaller than a region|   &#x60;macrocounty&#x60;|a related group of counties. Mostly in Europe.|   &#x60;region&#x60;|states and provinces|   &#x60;macroregion&#x60;|a related group of regions. Mostly in Europe|   &#x60;country&#x60;|places that issue passports, nations, nation-states|   &#x60;coarse&#x60;|alias for simultaneously using all administrative layers (everything except &#x60;venue&#x60; and &#x60;address&#x60;)|  | [optional] 
 **sources** | [**list[str]**](str.md)| Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [&#x60;openstreetmap(osm)&#x60;](http://www.openstreetmap.org/), [&#x60;openaddresses(oa)&#x60;](http://openaddresses.io/), [&#x60;whosonfirst(wof)&#x60;](https://whosonfirst.org/), [&#x60;geonames(gn)&#x60;](http://www.geonames.org/).  | [optional] [default to [&quot;osm&quot;,&quot;oa&quot;,&quot;gn&quot;,&quot;wof&quot;]]
 **boundary_country** | **str**| Restrict search to country by [alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or [alpha 3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) codes.  | [optional] 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **geocode_search_get**
> GeocodeResponse geocode_search_get(text, focus_point_lon=focus_point_lon, focus_point_lat=focus_point_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_radius=boundary_circle_radius, boundary_gid=boundary_gid, boundary_country=boundary_country, sources=sources, layers=layers, size=size)

Forward Geocode Service

Returns a JSON formatted list of objects corresponding to the search input. `boundary.*`-parameters can be combined if they are overlapping. **The interactivity for this enpoint is experimental!** [Please refer to this external Documentation](https://github.com/pelias/documentation/blob/master/search.md#search-the-world) 

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
api_instance = openrouteservice.GeocodeApi(openrouteservice.ApiClient(configuration))
text = 'text_example' # str | Name of location, street address or postal code. 
focus_point_lon = 3.4 # float | Longitude of the `focus.point`. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance.  Use with `focus.point.lat`.  (optional)
focus_point_lat = 3.4 # float | Latitude of the `focus.point`. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance. Use with `focus.point.lon`.  (optional)
boundary_rect_min_lon = 3.4 # float | Left border of rectangular boundary to narrow results.  (optional)
boundary_rect_min_lat = 3.4 # float | Bottom border of rectangular boundary to narrow results.  (optional)
boundary_rect_max_lon = 3.4 # float | Right border of rectangular boundary to narrow results.  (optional)
boundary_rect_max_lat = 3.4 # float | Top border of rectangular boundary to narrow results.  (optional)
boundary_circle_lon = 3.4 # float | Center Longitude of circular boundary to narrow results. Use with `boundary.circle.lat` & `boundary.circle.radius`.  (optional)
boundary_circle_lat = 3.4 # float | Center Latitude of circular boundary to narrow results. Use with `boundary.circle.lon` & `boundary.circle.radius`.  (optional)
boundary_circle_radius = 50 # float | Radius of circular boundary around the center coordinate in kilometers. Use with `boundary.circle.lon` & `boundary.circle.lat`.  (optional) (default to 50)
boundary_gid = 'boundary_gid_example' # str | Restrict results to administrative boundary using a Pelias global id [`gid`](https://github.com/pelias/documentation/blob/f1f475aa4f8c18426fb80baea636990502c08ed3/search.md#search-within-a-parent-administrative-area). `gid`s for records can be found using either the [Who's on First Spelunker](http://spelunker.whosonfirst.org/), a tool for searching Who's on First data, or from the responses of other Pelias queries. In this case a [search for Oklahoma](http://pelias.github.io/compare/#/v1/search%3Ftext=oklahoma) will return the proper `gid`.  (optional)
boundary_country = 'boundary_country_example' # str | Restrict results to single country. Possible values are [alpha-2 and alpha-3 country codes](https://en.wikipedia.org/wiki/ISO_3166-1). Example: `DEU` or `DE` for Germany.  (optional)
sources = ['[\"osm\",\"oa\",\"gn\",\"wof\"]'] # list[str] | Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [`openstreetmap(osm)`](http://www.openstreetmap.org/), [`openaddresses(oa)`](http://openaddresses.io/), [`whosonfirst(wof)`](https://whosonfirst.org/), [`geonames(gn)`](http://www.geonames.org/).  (optional) (default to ["osm","oa","gn","wof"])
layers = ['layers_example'] # list[str] | Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   `venue`|points of interest, businesses, things with walls|   `address`|places with a street address|   `street`|streets,roads,highways|   `neighbourhood`|social communities, neighbourhoods|   `borough`|a local administrative boundary, currently only used for New York City|   `localadmin`|local administrative boundaries|   `locality`|towns, hamlets, cities|   `county`|official governmental area; usually bigger than a locality, almost always smaller than a region|   `macrocounty`|a related group of counties. Mostly in Europe.|   `region`|states and provinces|   `macroregion`|a related group of regions. Mostly in Europe|   `country`|places that issue passports, nations, nation-states|   `coarse`|alias for simultaneously using all administrative layers (everything except `venue` and `address`)|  (optional)
size = 10 # int | Set the number of returned results.  (optional) (default to 10)

try:
    # Forward Geocode Service
    api_response = api_instance.geocode_search_get(text, focus_point_lon=focus_point_lon, focus_point_lat=focus_point_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_radius=boundary_circle_radius, boundary_gid=boundary_gid, boundary_country=boundary_country, sources=sources, layers=layers, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeocodeApi->geocode_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Name of location, street address or postal code.  | 
 **focus_point_lon** | **float**| Longitude of the &#x60;focus.point&#x60;. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance.  Use with &#x60;focus.point.lat&#x60;.  | [optional] 
 **focus_point_lat** | **float**| Latitude of the &#x60;focus.point&#x60;. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance. Use with &#x60;focus.point.lon&#x60;.  | [optional] 
 **boundary_rect_min_lon** | **float**| Left border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_min_lat** | **float**| Bottom border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_max_lon** | **float**| Right border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_max_lat** | **float**| Top border of rectangular boundary to narrow results.  | [optional] 
 **boundary_circle_lon** | **float**| Center Longitude of circular boundary to narrow results. Use with &#x60;boundary.circle.lat&#x60; &amp; &#x60;boundary.circle.radius&#x60;.  | [optional] 
 **boundary_circle_lat** | **float**| Center Latitude of circular boundary to narrow results. Use with &#x60;boundary.circle.lon&#x60; &amp; &#x60;boundary.circle.radius&#x60;.  | [optional] 
 **boundary_circle_radius** | **float**| Radius of circular boundary around the center coordinate in kilometers. Use with &#x60;boundary.circle.lon&#x60; &amp; &#x60;boundary.circle.lat&#x60;.  | [optional] [default to 50]
 **boundary_gid** | **str**| Restrict results to administrative boundary using a Pelias global id [&#x60;gid&#x60;](https://github.com/pelias/documentation/blob/f1f475aa4f8c18426fb80baea636990502c08ed3/search.md#search-within-a-parent-administrative-area). &#x60;gid&#x60;s for records can be found using either the [Who&#x27;s on First Spelunker](http://spelunker.whosonfirst.org/), a tool for searching Who&#x27;s on First data, or from the responses of other Pelias queries. In this case a [search for Oklahoma](http://pelias.github.io/compare/#/v1/search%3Ftext&#x3D;oklahoma) will return the proper &#x60;gid&#x60;.  | [optional] 
 **boundary_country** | **str**| Restrict results to single country. Possible values are [alpha-2 and alpha-3 country codes](https://en.wikipedia.org/wiki/ISO_3166-1). Example: &#x60;DEU&#x60; or &#x60;DE&#x60; for Germany.  | [optional] 
 **sources** | [**list[str]**](str.md)| Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [&#x60;openstreetmap(osm)&#x60;](http://www.openstreetmap.org/), [&#x60;openaddresses(oa)&#x60;](http://openaddresses.io/), [&#x60;whosonfirst(wof)&#x60;](https://whosonfirst.org/), [&#x60;geonames(gn)&#x60;](http://www.geonames.org/).  | [optional] [default to [&quot;osm&quot;,&quot;oa&quot;,&quot;gn&quot;,&quot;wof&quot;]]
 **layers** | [**list[str]**](str.md)| Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   &#x60;venue&#x60;|points of interest, businesses, things with walls|   &#x60;address&#x60;|places with a street address|   &#x60;street&#x60;|streets,roads,highways|   &#x60;neighbourhood&#x60;|social communities, neighbourhoods|   &#x60;borough&#x60;|a local administrative boundary, currently only used for New York City|   &#x60;localadmin&#x60;|local administrative boundaries|   &#x60;locality&#x60;|towns, hamlets, cities|   &#x60;county&#x60;|official governmental area; usually bigger than a locality, almost always smaller than a region|   &#x60;macrocounty&#x60;|a related group of counties. Mostly in Europe.|   &#x60;region&#x60;|states and provinces|   &#x60;macroregion&#x60;|a related group of regions. Mostly in Europe|   &#x60;country&#x60;|places that issue passports, nations, nation-states|   &#x60;coarse&#x60;|alias for simultaneously using all administrative layers (everything except &#x60;venue&#x60; and &#x60;address&#x60;)|  | [optional] 
 **size** | **int**| Set the number of returned results.  | [optional] [default to 10]

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

# **geocode_search_structured_get**
> GeocodeResponse geocode_search_structured_get(address=address, neighbourhood=neighbourhood, country=country, postalcode=postalcode, region=region, county=county, locality=locality, borough=borough, focus_point_lon=focus_point_lon, focus_point_lat=focus_point_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, layers=layers, sources=sources, size=size)

Structured Forward Geocode Service (beta)

Returns a JSON formatted list of objects corresponding to the search input. **The interactivity for this enpoint is experimental!** [Please refer to this external Documentation](https://github.com/pelias/documentation/blob/master/structured-geocoding.md#structured-geocoding) 

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
api_instance = openrouteservice.GeocodeApi(openrouteservice.ApiClient(configuration))
address = 'address_example' # str | Search for full address with house number or only a street name.  (optional)
neighbourhood = 'neighbourhood_example' # str | Search for neighbourhoods. Neighbourhoods are vernacular geographic entities that may not necessarily be official administrative divisions but are important nonetheless. Example: `Notting Hill`.  (optional)
country = 'country_example' # str | Search for full country name, [alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or [alpha 3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) codes.  (optional)
postalcode = 'postalcode_example' # str | Search for postal codes. Postal codes are unique within a country so they are useful in geocoding as a shorthand for a fairly granular geographical location.  (optional)
region = 'region_example' # str | Search for regions. Regions are normally the first-level administrative divisions within countries. For US-regions [common abbreviations](https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations) can be used.  (optional)
county = 'county_example' # str | Search for counties. Counties are administrative divisions between localities and regions. Can be useful when attempting to disambiguate between localities.  (optional)
locality = 'Tokyo' # str | Search for localities. Localities are equivalent to what are commonly referred to as *cities*.  (optional) (default to Tokyo)
borough = 'borough_example' # str | Search for boroughs. Boroughs are mostly known in the context of New York City, even though they may exist in other cities, such as Mexico City. Example: `Manhatten`.  (optional)
focus_point_lon = 3.4 # float | Longitude of the `focus.point`. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance.  Use with `focus.point.lat`.  (optional)
focus_point_lat = 3.4 # float | Latitude of the `focus.point`. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance. Use with `focus.point.lon`.  (optional)
boundary_rect_min_lon = 3.4 # float | Left border of rectangular boundary to narrow results.  (optional)
boundary_rect_min_lat = 3.4 # float | Bottom border of rectangular boundary to narrow results.  (optional)
boundary_rect_max_lon = 3.4 # float | Right border of rectangular boundary to narrow results.  (optional)
boundary_rect_max_lat = 3.4 # float | Top border of rectangular boundary to narrow results.  (optional)
boundary_circle_lon = 3.4 # float | Center Longitude of circular boundary to narrow results. Use with `boundary.circle.lat` & `boundary.circle.radius`.  (optional)
boundary_circle_lat = 3.4 # float | Center Latitude of circular boundary to narrow results. Use with `boundary.circle.lon` & `boundary.circle.radius`.  (optional)
boundary_circle_radius = 50 # float | Radius of circular boundary around the center coordinate in kilometers. Use with `boundary.circle.lon` & `boundary.circle.lat`.  (optional) (default to 50)
boundary_country = 'boundary_country_example' # str | Restrict results to single country. Possible values are [alpha-2 and alpha-3 country codes](https://en.wikipedia.org/wiki/ISO_3166-1). Example: `DEU` or `DE` for Germany.  (optional)
layers = ['layers_example'] # list[str] | Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   `venue`|points of interest, businesses, things with walls|   `address`|places with a street address|   `street`|streets,roads,highways|   `neighbourhood`|social communities, neighbourhoods|   `borough`|a local administrative boundary, currently only used for New York City|   `localadmin`|local administrative boundaries|   `locality`|towns, hamlets, cities|   `county`|official governmental area; usually bigger than a locality, almost always smaller than a region|   `macrocounty`|a related group of counties. Mostly in Europe.|   `region`|states and provinces|   `macroregion`|a related group of regions. Mostly in Europe|   `country`|places that issue passports, nations, nation-states|   `coarse`|alias for simultaneously using all administrative layers (everything except `venue` and `address`)|  (optional)
sources = ['[\"osm\",\"oa\",\"gn\",\"wof\"]'] # list[str] | Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [`openstreetmap(osm)`](http://www.openstreetmap.org/), [`openaddresses(oa)`](http://openaddresses.io/), [`whosonfirst(wof)`](https://whosonfirst.org/), [`geonames(gn)`](http://www.geonames.org/).  (optional) (default to ["osm","oa","gn","wof"])
size = 10 # int | Set the number of returned results.  (optional) (default to 10)

try:
    # Structured Forward Geocode Service (beta)
    api_response = api_instance.geocode_search_structured_get(address=address, neighbourhood=neighbourhood, country=country, postalcode=postalcode, region=region, county=county, locality=locality, borough=borough, focus_point_lon=focus_point_lon, focus_point_lat=focus_point_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, layers=layers, sources=sources, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeocodeApi->geocode_search_structured_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Search for full address with house number or only a street name.  | [optional] 
 **neighbourhood** | **str**| Search for neighbourhoods. Neighbourhoods are vernacular geographic entities that may not necessarily be official administrative divisions but are important nonetheless. Example: &#x60;Notting Hill&#x60;.  | [optional] 
 **country** | **str**| Search for full country name, [alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or [alpha 3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) codes.  | [optional] 
 **postalcode** | **str**| Search for postal codes. Postal codes are unique within a country so they are useful in geocoding as a shorthand for a fairly granular geographical location.  | [optional] 
 **region** | **str**| Search for regions. Regions are normally the first-level administrative divisions within countries. For US-regions [common abbreviations](https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations) can be used.  | [optional] 
 **county** | **str**| Search for counties. Counties are administrative divisions between localities and regions. Can be useful when attempting to disambiguate between localities.  | [optional] 
 **locality** | **str**| Search for localities. Localities are equivalent to what are commonly referred to as *cities*.  | [optional] [default to Tokyo]
 **borough** | **str**| Search for boroughs. Boroughs are mostly known in the context of New York City, even though they may exist in other cities, such as Mexico City. Example: &#x60;Manhatten&#x60;.  | [optional] 
 **focus_point_lon** | **float**| Longitude of the &#x60;focus.point&#x60;. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance.  Use with &#x60;focus.point.lat&#x60;.  | [optional] 
 **focus_point_lat** | **float**| Latitude of the &#x60;focus.point&#x60;. Specify the focus point to order results by linear distance to this point. Works for up to 100 kilometers distance. Use with &#x60;focus.point.lon&#x60;.  | [optional] 
 **boundary_rect_min_lon** | **float**| Left border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_min_lat** | **float**| Bottom border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_max_lon** | **float**| Right border of rectangular boundary to narrow results.  | [optional] 
 **boundary_rect_max_lat** | **float**| Top border of rectangular boundary to narrow results.  | [optional] 
 **boundary_circle_lon** | **float**| Center Longitude of circular boundary to narrow results. Use with &#x60;boundary.circle.lat&#x60; &amp; &#x60;boundary.circle.radius&#x60;.  | [optional] 
 **boundary_circle_lat** | **float**| Center Latitude of circular boundary to narrow results. Use with &#x60;boundary.circle.lon&#x60; &amp; &#x60;boundary.circle.radius&#x60;.  | [optional] 
 **boundary_circle_radius** | **float**| Radius of circular boundary around the center coordinate in kilometers. Use with &#x60;boundary.circle.lon&#x60; &amp; &#x60;boundary.circle.lat&#x60;.  | [optional] [default to 50]
 **boundary_country** | **str**| Restrict results to single country. Possible values are [alpha-2 and alpha-3 country codes](https://en.wikipedia.org/wiki/ISO_3166-1). Example: &#x60;DEU&#x60; or &#x60;DE&#x60; for Germany.  | [optional] 
 **layers** | [**list[str]**](str.md)| Restrict search to layers (place type). By default all layers are searched.   layer|description|   ----|----|   &#x60;venue&#x60;|points of interest, businesses, things with walls|   &#x60;address&#x60;|places with a street address|   &#x60;street&#x60;|streets,roads,highways|   &#x60;neighbourhood&#x60;|social communities, neighbourhoods|   &#x60;borough&#x60;|a local administrative boundary, currently only used for New York City|   &#x60;localadmin&#x60;|local administrative boundaries|   &#x60;locality&#x60;|towns, hamlets, cities|   &#x60;county&#x60;|official governmental area; usually bigger than a locality, almost always smaller than a region|   &#x60;macrocounty&#x60;|a related group of counties. Mostly in Europe.|   &#x60;region&#x60;|states and provinces|   &#x60;macroregion&#x60;|a related group of regions. Mostly in Europe|   &#x60;country&#x60;|places that issue passports, nations, nation-states|   &#x60;coarse&#x60;|alias for simultaneously using all administrative layers (everything except &#x60;venue&#x60; and &#x60;address&#x60;)|  | [optional] 
 **sources** | [**list[str]**](str.md)| Restrict your search to specific sources. Searches all sources by default. You can either use the normal or short name. Sources are [&#x60;openstreetmap(osm)&#x60;](http://www.openstreetmap.org/), [&#x60;openaddresses(oa)&#x60;](http://openaddresses.io/), [&#x60;whosonfirst(wof)&#x60;](https://whosonfirst.org/), [&#x60;geonames(gn)&#x60;](http://www.geonames.org/).  | [optional] [default to [&quot;osm&quot;,&quot;oa&quot;,&quot;gn&quot;,&quot;wof&quot;]]
 **size** | **int**| Set the number of returned results.  | [optional] [default to 10]

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to Model list]](../README.md#documentation_for_models) [[Back to README]](../README.md)

