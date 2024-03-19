# coding: utf-8

"""
    Openrouteservice

    This is the openrouteservice API documentation for ORS Core-Version 8.0. Documentations for [older Core-Versions](https://github.com/GIScience/openrouteservice-docs/releases) can be rendered with the [Swagger-Editor](https://editor-next.swagger.io/).  # noqa: E501

    OpenAPI spec version: v2
    Contact: support@smartmobility.heigit.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest
import configparser

import openrouteservice
from openrouteservice.api.optimization_api import OptimizationApi  # noqa: E501
from openrouteservice.rest import ApiException
from openrouteservice import apiClient


class TestOptimizationApi(unittest.TestCase):
    """OptimizationApi unit test stubs"""

    def setUp(self):
        cfg = configparser.ConfigParser()
        cfg.read('tests-config.ini')
        self.api = OptimizationApi(apiClient(cfg['ORS']['apiKey']))  # noqa: E501

    def tearDown(self):
        pass

    def test_optimization_post(self):
        """Test case for optimization_post

        Optimization Service  # noqa: E501
        """
        body = openrouteservice.OptimizationBody(
            jobs=[{"id":1,"service":300,"amount":[1],"location":[1.98465,48.70329],"skills":[1],"time_windows":[[32400,36000]]},{"id":2,"service":300,"amount":[1],"location":[2.03655,48.61128],"skills":[1]},{"id":3,"service":300,"amount":[1],"location":[2.39719,49.07611],"skills":[2]},{"id":4,"service":300,"amount":[1],"location":[2.41808,49.22619],"skills":[2]},{"id":5,"service":300,"amount":[1],"location":[2.28325,48.5958],"skills":[14]},{"id":6,"service":300,"amount":[1],"location":[2.89357,48.90736],"skills":[14]}],
            vehicles=[{"id":1,"profile":"driving-car","start":[2.35044,48.71764],"end":[2.35044,48.71764],"capacity":[4],"skills":[1,14],"time_window":[28800,43200]},{"id":2,"profile":"driving-car","start":[2.35044,48.71764],"end":[2.35044,48.71764],"capacity":[4],"skills":[2,14],"time_window":[28800,43200]}]
        )
        response = self.api.optimization_post(body)
        self.assertEqual(response["code"], 0)


if __name__ == '__main__':
    unittest.main()