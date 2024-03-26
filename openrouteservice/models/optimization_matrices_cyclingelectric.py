# coding: utf-8

"""
    Openrouteservice

    This is the openrouteservice API documentation for ORS Core-Version 7.1.1. Documentations for [older Core-Versions](https://github.com/GIScience/openrouteservice-docs/releases) can be rendered with the [Swagger-Editor](https://editor-next.swagger.io/).  # noqa: E501

    OpenAPI spec version: 7.1.1
    Contact: support@smartmobility.heigit.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OptimizationMatricesCyclingelectric(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'costs': 'list[list[int]]',
        'distances': 'list[list[int]]',
        'durations': 'list[list[int]]'
    }

    attribute_map = {
        'costs': 'costs',
        'distances': 'distances',
        'durations': 'durations'
    }

    def __init__(self, costs=None, distances=None, durations=None):  # noqa: E501
        """OptimizationMatricesCyclingelectric - a model defined in Swagger"""  # noqa: E501
        self._costs = None
        self._distances = None
        self._durations = None
        self.discriminator = None
        if costs is not None:
            self.costs = costs
        if distances is not None:
            self.distances = distances
        if durations is not None:
            self.durations = durations

    @property
    def costs(self):
        """Gets the costs of this OptimizationMatricesCyclingelectric.  # noqa: E501

        costs for a custom cost matrix that will be used within all route cost evaluations  # noqa: E501

        :return: The costs of this OptimizationMatricesCyclingelectric.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this OptimizationMatricesCyclingelectric.

        costs for a custom cost matrix that will be used within all route cost evaluations  # noqa: E501

        :param costs: The costs of this OptimizationMatricesCyclingelectric.  # noqa: E501
        :type: list[list[int]]
        """

        self._costs = costs

    @property
    def distances(self):
        """Gets the distances of this OptimizationMatricesCyclingelectric.  # noqa: E501

        distances for a custom distance matrix  # noqa: E501

        :return: The distances of this OptimizationMatricesCyclingelectric.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._distances

    @distances.setter
    def distances(self, distances):
        """Sets the distances of this OptimizationMatricesCyclingelectric.

        distances for a custom distance matrix  # noqa: E501

        :param distances: The distances of this OptimizationMatricesCyclingelectric.  # noqa: E501
        :type: list[list[int]]
        """

        self._distances = distances

    @property
    def durations(self):
        """Gets the durations of this OptimizationMatricesCyclingelectric.  # noqa: E501

        Durations for a custom travel-time matrix that will be used for all checks against timing constraints  # noqa: E501

        :return: The durations of this OptimizationMatricesCyclingelectric.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._durations

    @durations.setter
    def durations(self, durations):
        """Sets the durations of this OptimizationMatricesCyclingelectric.

        Durations for a custom travel-time matrix that will be used for all checks against timing constraints  # noqa: E501

        :param durations: The durations of this OptimizationMatricesCyclingelectric.  # noqa: E501
        :type: list[list[int]]
        """

        self._durations = durations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OptimizationMatricesCyclingelectric, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OptimizationMatricesCyclingelectric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
