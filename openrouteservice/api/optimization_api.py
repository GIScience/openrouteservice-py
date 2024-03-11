# coding: utf-8

"""
    Openrouteservice

    This is the openrouteservice API documentation for ORS Core-Version 7.1.1. Documentations for [older Core-Versions](https://github.com/GIScience/openrouteservice-docs/releases) can be rendered with the [Swagger-Editor](https://editor-next.swagger.io/).  # noqa: E501

    OpenAPI spec version: 7.1.1
    Contact: support@smartmobility.heigit.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openrouteservice.api_client import ApiClient


class OptimizationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def optimization_post(self, body, **kwargs):  # noqa: E501
        """Optimization Service  # noqa: E501

        The optimization endpoint solves [Vehicle Routing Problems](https://en.wikipedia.org/wiki/Vehicle_routing_problem) and can be used to schedule multiple vehicles and jobs, respecting time windows, capacities and required skills.  This service is based on the excellent [Vroom project](https://github.com/VROOM-Project/vroom). Please also consult its [API documentation](https://github.com/VROOM-Project/vroom/blob/master/docs/API.md).  General Info: - The expected order for all coordinates arrays is `[lon, lat]` - All timings are in seconds - All distances are in meters - A `time_window` object is a pair of timestamps in the form `[start, end]`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.optimization_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OptimizationBody body: The request body of the optimization request. (required)
        :return: JSONResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.optimization_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.optimization_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def optimization_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Optimization Service  # noqa: E501

        The optimization endpoint solves [Vehicle Routing Problems](https://en.wikipedia.org/wiki/Vehicle_routing_problem) and can be used to schedule multiple vehicles and jobs, respecting time windows, capacities and required skills.  This service is based on the excellent [Vroom project](https://github.com/VROOM-Project/vroom). Please also consult its [API documentation](https://github.com/VROOM-Project/vroom/blob/master/docs/API.md).  General Info: - The expected order for all coordinates arrays is `[lon, lat]` - All timings are in seconds - All distances are in meters - A `time_window` object is a pair of timestamps in the form `[start, end]`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.optimization_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OptimizationBody body: The request body of the optimization request. (required)
        :return: JSONResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method optimization_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `optimization_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/optimization', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JSONResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
