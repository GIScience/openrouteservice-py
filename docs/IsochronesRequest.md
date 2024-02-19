# IsochronesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_units** | **str** | Specifies the area unit. Default: m.  | [optional] [default to 'm']
**attributes** | **list[str]** | List of isochrones attributes | [optional] 
**id** | **str** | Arbitrary identification string of the request reflected in the meta information. | [optional] 
**intersections** | **bool** | Specifies whether to return intersecting polygons.  | [optional] [default to False]
**interval** | **float** | Interval of isochrones or equidistants. This is only used if a single range value is given. Value in **seconds** for time and **meters** for distance. | [optional] 
**location_type** | **str** | &#x60;start&#x60; treats the location(s) as starting point, &#x60;destination&#x60; as goal. | [optional] [default to 'start']
**locations** | **list[list[float]]** | The locations to use for the route as an array of &#x60;longitude/latitude&#x60; pairs in WGS 84 (EPSG:4326) | 
**options** | [**RouteOptions**](RouteOptions.md) |  | [optional] 
**range** | **list[float]** | Maximum range value of the analysis in **seconds** for time and **metres** for distance.Alternatively a comma separated list of specific range values. Ranges will be the same for all locations. | 
**range_type** | **str** | Specifies the isochrones reachability type. | [optional] [default to 'time']
**smoothing** | **float** | Applies a level of generalisation to the isochrone polygons generated as a &#x60;smoothing_factor&#x60; between &#x60;0&#x60; and &#x60;100.0&#x60;. Generalisation is produced by determining a maximum length of a connecting line between two points found on the outside of a containing polygon. If the distance is larger than a threshold value, the line between the two points is removed and a smaller connecting line between other points is used. Note that the minimum length of this connecting line is ~1333m, and so when the &#x60;smoothing_factor&#x60; results in a distance smaller than this, the minimum value is used. The threshold value is determined as &#x60;(maximum_radius_of_isochrone / 100) * smoothing_factor&#x60;. Therefore, a value closer to 100 will result in a more generalised shape. The polygon generation algorithm is based on Duckham and al. (2008) &#x60;\&quot;Efficient generation of simple polygons for characterizing the shape of a set of points in the plane.\&quot;&#x60; | [optional] 
**units** | **str** | Specifies the distance units only if &#x60;range_type&#x60; is set to distance. Default: m.  | [optional] [default to 'm']

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

