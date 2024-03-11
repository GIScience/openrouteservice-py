# InlineResponse2002Violations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **str** | string describing the cause of violation. Possible violation causes are:             - \&quot;delay\&quot; if actual service start does not meet a task time window and is late on a time window end             - \&quot;lead_time\&quot; if actual service start does not meet a task time window and is early on a time window start             - \&quot;load\&quot; if the vehicle load goes over its capacity             - \&quot;max_tasks\&quot; if the vehicle has more tasks than its max_tasks value             - \&quot;skills\&quot; if the vehicle does not hold all required skills for a task             - \&quot;precedence\&quot; if a shipment precedence constraint is not met (pickup without matching delivery, delivery before/without matching pickup)             - \&quot;missing_break\&quot; if a vehicle break has been omitted in its custom route             - \&quot;max_travel_time\&quot; if the vehicle has more travel time than its max_travel_time value             - \&quot;max_load\&quot; if the load during a break exceed its max_load value  | [optional] 
**duration** | **float** | Earliness (resp. lateness) if &#x60;cause&#x60; is \&quot;lead_time\&quot; (resp \&quot;delay\&quot;)  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

