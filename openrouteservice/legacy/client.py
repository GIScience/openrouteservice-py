# -*- coding: utf-8 -*-
# Copyright 2014 Google Inc. All rights reserved.
#
# Modifications Copyright (C) 2018 HeiGIT, University of Heidelberg.
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
"""Core client functionality, common across all API requests."""

from datetime import datetime
from datetime import timedelta
from urllib.parse import urlencode
import cgi
import functools
import requests
import json
import random
import time
import warnings

from openrouteservice.legacy import exceptions, __version__, get_ordinal, deprecation

_USER_AGENT = "ORSClientPython.v{}".format(__version__)
_DEFAULT_BASE_URL = "https://api.openrouteservice.org"

_RETRIABLE_STATUSES = set([503])  # noqa


class Client:
    """Performs requests to the ORS API services."""

    def __init__(
        self,
        key=None,
        base_url=_DEFAULT_BASE_URL,
        timeout=60,
        retry_timeout=60,
        requests_kwargs=None,
        retry_over_query_limit=True,
    ):
        """
        Initialize the openrouteservice client.

        :param key: ORS API key.
        :type key: string

        :param base_url: The base URL for the request. Defaults to the ORS API
            server. Should not have a trailing slash.
        :type base_url: string

        :param timeout: Combined connect and read timeout for HTTP requests, in
            seconds. Specify "None" for no timeout.
        :type timeout: int

        :param retry_timeout: Timeout across multiple retriable requests, in
            seconds.
        :type retry_timeout: int

        :param requests_kwargs: Extra keyword arguments for the requests
            library, which among other things allow for proxy auth to be
            implemented. See the official requests docs for more info:
            http://docs.python-requests.org/en/latest/api/#main-interface
        :type requests_kwargs: dict

        :param retry_over_query_limit: If True, the client will retry when query
            limit is reached (HTTP 429). Default False.
        :type retry_over_query_limit: bool
        """

        deprecation.deprecated("Client", "ApiClient")

        self._session = requests.Session()
        self._key = key
        self._base_url = base_url

        if self._base_url == _DEFAULT_BASE_URL and key is None:
            raise ValueError(
                "No API key was specified. Please visit https://openrouteservice.org/sign-up to create one."
            )

        self._timeout = timeout
        self._retry_over_query_limit = retry_over_query_limit
        self._retry_timeout = timedelta(seconds=retry_timeout)
        self._requests_kwargs = requests_kwargs or {}
        self._requests_kwargs.update(
            {
                "headers": {
                    "User-Agent": _USER_AGENT,
                    "Content-type": "application/json",
                    "Authorization": self._key,
                },
                "timeout": self._timeout,
            }
        )

        self._req = None

    def request(
        self,
        url,
        get_params=None,
        first_request_time=None,
        retry_counter=0,
        requests_kwargs=None,
        post_json=None,
        dry_run=None,
    ):
        """
        Performs HTTP GET/POST with credentials, returning the body as JSON.

        :param url: URL path for the request. Should begin with a slash.
        :type url: string

        :param get_params: HTTP GET parameters.
        :type get_params: dict or list of key/value tuples

        :param first_request_time: The time of the first request (None if no
            retries have occurred).
        :type first_request_time: datetime.datetime

        :param retry_counter: The number of this retry, or zero for first attempt.
        :type retry_counter: int

        :param requests_kwargs: Same extra keywords arg for requests as per
            __init__, but provided here to allow overriding internally on a
            per-request basis.
        :type requests_kwargs: dict

        :param post_json: HTTP POST parameters. Only specified by calling method.
        :type post_json: dict

        :param dry_run: If 'true', only prints URL and parameters. 'true' or 'false'.
        :type dry_run: string

        :raises ApiError: when the API returns an error.
        :raises Timeout: if the request timed out.

        :rtype: dict from JSON response.
        """

        if not first_request_time:
            first_request_time = datetime.now()

        elapsed = datetime.now() - first_request_time
        if elapsed > self._retry_timeout:
            raise exceptions.Timeout()

        if retry_counter > 0:
            # 0.5 * (1.5 ^ i) is an increased sleep time of 1.5x per iteration,
            # starting at 0.5s when retry_counter=1. The first retry will occur
            # at 1, so subtract that first.
            delay_seconds = 1.5 ** (retry_counter - 1)

            # Jitter this value by 50% and pause.
            time.sleep(delay_seconds * (random.random() + 0.5))

        authed_url = self._generate_auth_url(
            url,
            get_params,
        )

        # Default to the client-level self.requests_kwargs, with method-level
        # requests_kwargs arg overriding.
        requests_kwargs = requests_kwargs or {}
        final_requests_kwargs = dict(self._requests_kwargs, **requests_kwargs)

        # Determine GET/POST.
        requests_method = self._session.get

        if post_json is not None:
            requests_method = self._session.post
            final_requests_kwargs["json"] = post_json

        # Only print URL and parameters for dry_run
        if dry_run:
            print(  # noqa
                "url:\n{}\nHeaders:\n{}".format(
                    self._base_url + authed_url,
                    json.dumps(final_requests_kwargs, indent=2),
                )
            )
            return

        try:
            response = requests_method(
                self._base_url + authed_url, **final_requests_kwargs
            )
            self._req = response.request

        except requests.exceptions.Timeout:  # pragma: no cover
            raise exceptions.Timeout()

        if response.status_code in _RETRIABLE_STATUSES:
            # Retry request.
            warnings.warn(
                "Server down.\nRetrying for the {0}{1} time.".format(
                    retry_counter + 1, get_ordinal(retry_counter + 1)
                ),
                UserWarning,
                stacklevel=1,
            )

            return self.request(
                url,
                get_params,
                first_request_time,
                retry_counter + 1,
                requests_kwargs,
                post_json,
            )

        try:
            result = self._get_body(response)

            return result
        except exceptions._RetriableRequest as e:
            if (
                isinstance(e, exceptions._OverQueryLimit)
                and not self._retry_over_query_limit  # noqa
            ):
                raise

            warnings.warn(
                "Rate limit exceeded. Retrying for the {0}{1} time.".format(
                    retry_counter + 1, get_ordinal(retry_counter + 1)
                ),
                UserWarning,
                stacklevel=1,
            )
            # Retry request.
            return self.request(
                url,
                get_params,
                first_request_time,
                retry_counter + 1,
                requests_kwargs,
                post_json,
            )

    @property
    def req(self):
        """Returns request object. Can be used in case of request failure."""
        return self._req

    @staticmethod
    def _get_body(response):
        """Returns the body of a response object, raises status code exceptions if necessary."""
        content_type = response.headers["Content-Type"]
        mime_type, _ = cgi.parse_header(content_type)
        if mime_type == "application/gpx+xml":
            body = response.text
        else:
            try:
                body = response.json()
            except json.JSONDecodeError:  # pragma: no cover
                raise exceptions.HTTPError(response.status_code)

        # error = body.get('error')
        status_code = response.status_code

        if status_code == 429:
            raise exceptions._OverQueryLimit(status_code, body)
        if status_code != 200:
            raise exceptions.ApiError(status_code, body)

        return body

    @staticmethod
    def _generate_auth_url(path, params):
        """
        Returns the path and query string portion of the request URL, first adding any necessary parameters.

        :param path: The path portion of the URL.
        :type path: string

        :param params: URL parameters.
        :type params: dict or list of key/value tuples

        :rtype: string

        """

        if type(params) is dict:
            params = sorted(dict(**params).items())
        elif params is None:
            return path

        return path + "?" + _urlencode_params(params)


from openrouteservice.legacy.directions import directions  # noqa
from openrouteservice.legacy.distance_matrix import distance_matrix  # noqa
from openrouteservice.legacy.elevation import elevation_point  # noqa
from openrouteservice.legacy.elevation import elevation_line  # noqa
from openrouteservice.legacy.isochrones import isochrones  # noqa
from openrouteservice.legacy.geocode import pelias_search  # noqa
from openrouteservice.legacy.geocode import pelias_autocomplete  # noqa
from openrouteservice.legacy.geocode import pelias_structured  # noqa
from openrouteservice.legacy.geocode import pelias_reverse  # noqa
from openrouteservice.legacy.places import places  # noqa
from openrouteservice.legacy.optimization import optimization  # noqa


def _make_api_method(func):
    """
    Provides a single entry point for modifying all API methods.

    For now this is limited to allowing the client object to be modified
    with an `extra_params` keyword arg to each method, that is then used
    as the params for each web service request.

    Please note that this is an unsupported feature for advanced use only.
    It's also currently incompatibile with multiple threads, see GH #160.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args[0]._extra_params = kwargs.pop("extra_params", None)
        result = func(*args, **kwargs)
        try:
            del args[0]._extra_params
        except AttributeError:  # pragma: no cover
            pass
        return result

    return wrapper


Client.directions = _make_api_method(directions)
Client.distance_matrix = _make_api_method(distance_matrix)
Client.elevation_point = _make_api_method(elevation_point)
Client.elevation_line = _make_api_method(elevation_line)
Client.isochrones = _make_api_method(isochrones)
Client.pelias_search = _make_api_method(pelias_search)
Client.pelias_autocomplete = _make_api_method(pelias_autocomplete)
Client.pelias_structured = _make_api_method(pelias_structured)
Client.pelias_reverse = _make_api_method(pelias_reverse)
Client.places = _make_api_method(places)
Client.optimization = _make_api_method(optimization)


def _urlencode_params(params):
    """URL encodes the parameters.

    :param params: The parameters
    :type params: list of key/value tuples.

    :rtype: string
    """
    params = [(key, val) for key, val in params]
    # Unquote unreserved chars which are incorrectly quoted
    # by urllib.urlencode, causing invalid auth signatures. See GH #72
    # for more info.
    return requests.utils.unquote_unreserved(urlencode(params))
