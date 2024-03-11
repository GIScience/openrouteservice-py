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

class SnappingResponseLocations(object):
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
        'location': 'list[float]',
        'name': 'str',
        'snapped_distance': 'float'
    }

    attribute_map = {
        'location': 'location',
        'name': 'name',
        'snapped_distance': 'snapped_distance'
    }

    def __init__(self, location=None, name=None, snapped_distance=None):  # noqa: E501
        """SnappingResponseLocations - a model defined in Swagger"""  # noqa: E501
        self._location = None
        self._name = None
        self._snapped_distance = None
        self.discriminator = None
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if snapped_distance is not None:
            self.snapped_distance = snapped_distance

    @property
    def location(self):
        """Gets the location of this SnappingResponseLocations.  # noqa: E501

        {longitude},{latitude} coordinates of the closest accessible point on the routing graph  # noqa: E501

        :return: The location of this SnappingResponseLocations.  # noqa: E501
        :rtype: list[float]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SnappingResponseLocations.

        {longitude},{latitude} coordinates of the closest accessible point on the routing graph  # noqa: E501

        :param location: The location of this SnappingResponseLocations.  # noqa: E501
        :type: list[float]
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this SnappingResponseLocations.  # noqa: E501

        Name of the street the closest accessible point is situated on. Only for `resolve_locations=true` and only if name is available.  # noqa: E501

        :return: The name of this SnappingResponseLocations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnappingResponseLocations.

        Name of the street the closest accessible point is situated on. Only for `resolve_locations=true` and only if name is available.  # noqa: E501

        :param name: The name of this SnappingResponseLocations.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def snapped_distance(self):
        """Gets the snapped_distance of this SnappingResponseLocations.  # noqa: E501

        Distance between the `source/destination` Location and the used point on the routing graph in meters.  # noqa: E501

        :return: The snapped_distance of this SnappingResponseLocations.  # noqa: E501
        :rtype: float
        """
        return self._snapped_distance

    @snapped_distance.setter
    def snapped_distance(self, snapped_distance):
        """Sets the snapped_distance of this SnappingResponseLocations.

        Distance between the `source/destination` Location and the used point on the routing graph in meters.  # noqa: E501

        :param snapped_distance: The snapped_distance of this SnappingResponseLocations.  # noqa: E501
        :type: float
        """

        self._snapped_distance = snapped_distance

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
        if issubclass(SnappingResponseLocations, dict):
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
        if not isinstance(other, SnappingResponseLocations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
