# InlineResponse2002

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | status code. Possible values:   Value         | Status |  :-----------: | :-----------: |  &#x60;0&#x60; | no error raised |  &#x60;1&#x60; | internal error |  &#x60;2&#x60; | input error |  &#x60;3&#x60; | routing error |  | [optional] 
**error** | **str** | error message (present if &#x60;code&#x60; is different from &#x60;0&#x60;)  | [optional] 
**routes** | [**list[InlineResponse2002Routes]**](InlineResponse2002Routes.md) | array of &#x60;route&#x60; objects  | [optional] 
**summary** | [**InlineResponse2002Summary**](InlineResponse2002Summary.md) |  | [optional] 
**unassigned** | [**list[InlineResponse2002Unassigned]**](InlineResponse2002Unassigned.md) | array of objects describing unassigned jobs with their &#x60;id&#x60; and &#x60;location&#x60; (if provided)  | [optional] 

[[Back to Model list]](../README.md#documentation_for_models) [[Back to API list]](../README.md#documentation_for_api_endpoints) [[Back to README]](../README.md)

