# MatrixRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | **list[str]** | A list of indices that refers to the list of locations (starting with &#x60;0&#x60;). &#x60;{index_1},{index_2}[,{index_N} ...]&#x60; or &#x60;all&#x60; (default). &#x60;[0,3]&#x60; for the first and fourth locations  | [optional] 
**id** | **str** | Arbitrary identification string of the request reflected in the meta information. | [optional] 
**locations** | **list[list[float]]** | List of comma separated lists of &#x60;longitude,latitude&#x60; coordinates in WGS 84 (EPSG:4326) | 
**metrics** | **list[str]** | Specifies a list of returned metrics. \&quot;* &#x60;distance&#x60; - Returns distance matrix for specified points in defined &#x60;units&#x60;. * &#x60;duration&#x60; - Returns duration matrix for specified points in **seconds**.  | [optional] 
**resolve_locations** | **bool** | Specifies whether given locations are resolved or not. If the parameter value set to &#x60;true&#x60;, every element in &#x60;destinations&#x60; and &#x60;sources&#x60; will contain a &#x60;name&#x60; element that identifies the name of the closest street. Default is &#x60;false&#x60;.  | [optional] [default to False]
**sources** | **list[str]** | A list of indices that refers to the list of locations (starting with &#x60;0&#x60;). &#x60;{index_1},{index_2}[,{index_N} ...]&#x60; or &#x60;all&#x60; (default). example &#x60;[0,3]&#x60; for the first and fourth locations  | [optional] 
**units** | **str** | Specifies the distance unit. Default: m. | [optional] [default to 'm']

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

