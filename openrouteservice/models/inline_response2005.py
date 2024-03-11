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

class InlineResponse2005(object):
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
        'bbox': 'list[float]',
        'features': 'list[GeoJSONIsochronesResponseFeatures]',
        'metadata': 'GeoJSONIsochronesResponseMetadata',
        'type': 'str'
    }

    attribute_map = {
        'bbox': 'bbox',
        'features': 'features',
        'metadata': 'metadata',
        'type': 'type'
    }

    def __init__(self, bbox=None, features=None, metadata=None, type=None):  # noqa: E501
        """InlineResponse2005 - a model defined in Swagger"""  # noqa: E501
        self._bbox = None
        self._features = None
        self._metadata = None
        self._type = None
        self.discriminator = None
        if bbox is not None:
            self.bbox = bbox
        if features is not None:
            self.features = features
        if metadata is not None:
            self.metadata = metadata
        if type is not None:
            self.type = type

    @property
    def bbox(self):
        """Gets the bbox of this InlineResponse2005.  # noqa: E501

        Bounding box that covers all returned isochrones  # noqa: E501

        :return: The bbox of this InlineResponse2005.  # noqa: E501
        :rtype: list[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this InlineResponse2005.

        Bounding box that covers all returned isochrones  # noqa: E501

        :param bbox: The bbox of this InlineResponse2005.  # noqa: E501
        :type: list[float]
        """

        self._bbox = bbox

    @property
    def features(self):
        """Gets the features of this InlineResponse2005.  # noqa: E501


        :return: The features of this InlineResponse2005.  # noqa: E501
        :rtype: list[GeoJSONIsochronesResponseFeatures]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this InlineResponse2005.


        :param features: The features of this InlineResponse2005.  # noqa: E501
        :type: list[GeoJSONIsochronesResponseFeatures]
        """

        self._features = features

    @property
    def metadata(self):
        """Gets the metadata of this InlineResponse2005.  # noqa: E501


        :return: The metadata of this InlineResponse2005.  # noqa: E501
        :rtype: GeoJSONIsochronesResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InlineResponse2005.


        :param metadata: The metadata of this InlineResponse2005.  # noqa: E501
        :type: GeoJSONIsochronesResponseMetadata
        """

        self._metadata = metadata

    @property
    def type(self):
        """Gets the type of this InlineResponse2005.  # noqa: E501


        :return: The type of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2005.


        :param type: The type of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(InlineResponse2005, dict):
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
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
