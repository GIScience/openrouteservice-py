# OpenpoiservicePoiRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**PoisFilters**](PoisFilters.md) |  | [optional] 
**geometry** | [**PoisGeometry**](PoisGeometry.md) |  | 
**limit** | **int** | The limit of objects to be returned in the response. | [optional] 
**request** | **str** | Examples: &#x60;&#x60;&#x60; #### JSON bodies for POST requests ##### Pois around a buffered point {   \&quot;request\&quot;: \&quot;pois\&quot;,   \&quot;geometry\&quot;: {     \&quot;bbox\&quot;: [       [8.8034, 53.0756],       [8.7834, 53.0456]     ],     \&quot;geojson\&quot;: {       \&quot;type\&quot;: \&quot;Point\&quot;,       \&quot;coordinates\&quot;: [8.8034, 53.0756]     },     \&quot;buffer\&quot;: 250   } }  ##### Pois given categories {   \&quot;request\&quot;: \&quot;pois\&quot;,   \&quot;geometry\&quot;: {     \&quot;bbox\&quot;: [       [8.8034, 53.0756],       [8.7834, 53.0456]     ],     \&quot;geojson\&quot;: {       \&quot;type\&quot;: \&quot;Point\&quot;,       \&quot;coordinates\&quot;: [8.8034, 53.0756]     },     \&quot;buffer\&quot;: 100   },   \&quot;limit\&quot;: 200,   \&quot;filters\&quot;: {     \&quot;category_ids\&quot;: [180, 245]   } }  ##### Pois given category groups {   \&quot;request\&quot;: \&quot;pois\&quot;,   \&quot;geometry\&quot;: {     \&quot;bbox\&quot;: [       [8.8034, 53.0756],       [8.7834, 53.0456]     ],     \&quot;geojson\&quot;: {       \&quot;type\&quot;: \&quot;Point\&quot;,       \&quot;coordinates\&quot;: [8.8034, 53.0756]     },     \&quot;buffer\&quot;: 100   },   \&quot;limit\&quot;: 200,   \&quot;filters\&quot;: {     \&quot;category_group_ids\&quot;: [160]   } }  ##### Pois statistics {   \&quot;request\&quot;: \&quot;stats\&quot;,   \&quot;geometry\&quot;: {     \&quot;bbox\&quot;: [       [8.8034, 53.0756],       [8.7834, 53.0456]     ],     \&quot;geojson\&quot;: {       \&quot;type\&quot;: \&quot;Point\&quot;,       \&quot;coordinates\&quot;: [8.8034, 53.0756]     },     \&quot;buffer\&quot;: 100   } }  ##### Pois categories as a list {     \&quot;request\&quot;: \&quot;list\&quot; } &#x60;&#x60;&#x60;  | 
**sortby** | **str** | Either you can sort by category or the distance to the geometry object provided in the request. | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

