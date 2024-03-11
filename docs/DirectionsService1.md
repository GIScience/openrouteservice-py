# DirectionsService1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_routes** | [**AlternativeRoutes**](AlternativeRoutes.md) |  | [optional] 
**attributes** | **list[str]** | List of route attributes | [optional] 
**bearings** | **list[list[float]]** | Specifies a list of pairs (bearings and deviations) to filter the segments of the road network a waypoint can snap to. \&quot;For example &#x60;bearings&#x3D;[[45,10],[120,20]]&#x60;. \&quot;Each pair is a comma-separated list that can consist of one or two float values, where the first value is the bearing and the second one is the allowed deviation from the bearing. \&quot;The bearing can take values between &#x60;0&#x60; and &#x60;360&#x60; clockwise from true north. If the deviation is not set, then the default value of &#x60;100&#x60; degrees is used. \&quot;The number of pairs must correspond to the number of waypoints. \&quot;The number of bearings corresponds to the length of waypoints-1 or waypoints. If the bearing information for the last waypoint is given, then this will control the sector from which the destination waypoint may be reached. \&quot;You can skip a bearing for a certain waypoint by passing an empty value for an array, e.g. &#x60;[30,20],[],[40,20]&#x60;. | [optional] 
**continue_straight** | **bool** | Forces the route to keep going straight at waypoints restricting uturns there even if it would be faster. | [optional] [default to False]
**coordinates** | **list[list[float]]** | The waypoints to use for the route as an array of &#x60;longitude/latitude&#x60; pairs in WGS 84 (EPSG:4326) | 
**elevation** | **bool** | Specifies whether to return elevation values for points. Please note that elevation also gets encoded for json response encoded polyline. | [optional] 
**extra_info** | **list[str]** | The extra info items to include in the response | [optional] 
**geometry** | **bool** | Specifies whether to return geometry.  | [optional] [default to True]
**geometry_simplify** | **bool** | Specifies whether to simplify the geometry. Simplify geometry cannot be applied to routes with more than **one segment** and when &#x60;extra_info&#x60; is required. | [optional] [default to False]
**id** | **str** | Arbitrary identification string of the request reflected in the meta information. | [optional] 
**ignore_transfers** | **bool** | Specifies if transfers as criterion should be ignored. | [optional] [default to False]
**instructions** | **bool** | Specifies whether to return instructions. | [optional] [default to True]
**instructions_format** | **str** | Select html for more verbose instructions. | [optional] [default to 'text']
**language** | **str** | Language for the route instructions. | [optional] [default to 'en']
**maneuvers** | **bool** | Specifies whether the maneuver object is included into the step object or not.  | [optional] [default to False]
**maximum_speed** | **float** | The maximum speed specified by user. | [optional] 
**options** | [**RouteOptions**](RouteOptions.md) |  | [optional] 
**preference** | **str** | Specifies the route preference | [optional] [default to 'recommended']
**radiuses** | **list[float]** | A list of maximum distances (measured in metres) that limit the search of nearby road segments to every given waypoint. The values must be greater than 0, the value of -1 specifies using the maximum possible search radius. The number of radiuses correspond to the number of waypoints. If only a single value is given, it will be applied to all waypoints. | [optional] 
**roundabout_exits** | **bool** | Provides bearings of the entrance and all passed roundabout exits. Adds the &#x60;exit_bearings&#x60; array to the step object in the response.  | [optional] [default to False]
**schedule** | **bool** | If true, return a public transport schedule starting at &lt;departure&gt; for the next &lt;schedule_duration&gt; minutes. | [optional] [default to False]
**schedule_duration** | **str** | The time window when requesting a public transport schedule. The format is passed as ISO 8601 duration: https://en.wikipedia.org/wiki/ISO_8601#Durations | [optional] 
**schedule_rows** | **int** | The maximum amount of entries that should be returned when requesting a schedule. | [optional] 
**skip_segments** | **list[int]** | Specifies the segments that should be skipped in the route calculation. A segment is the connection between two given coordinates and the counting starts with 1 for the connection between the first and second coordinate. | [optional] 
**suppress_warnings** | **bool** | Suppress warning messages in the response | [optional] 
**units** | **str** | Specifies the distance unit. | [optional] [default to 'm']
**walking_time** | **str** | Maximum duration for walking access and egress of public transport. The value is passed in ISO 8601 duration format: https://en.wikipedia.org/wiki/ISO_8601#Durations | [optional] [default to 'PT15M']

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

