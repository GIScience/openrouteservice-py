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

class JsonExportResponse(object):
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
        'edges': 'list[JsonExportResponseEdges]',
        'edges_count': 'int',
        'edges_extra': 'list[JsonExportResponseEdgesExtra]',
        'nodes': 'list[JsonExportResponseNodes]',
        'nodes_count': 'int',
        'warning': 'JSONIndividualRouteResponseWarnings'
    }

    attribute_map = {
        'edges': 'edges',
        'edges_count': 'edges_count',
        'edges_extra': 'edges_extra',
        'nodes': 'nodes',
        'nodes_count': 'nodes_count',
        'warning': 'warning'
    }

    def __init__(self, edges=None, edges_count=None, edges_extra=None, nodes=None, nodes_count=None, warning=None):  # noqa: E501
        """JsonExportResponse - a model defined in Swagger"""  # noqa: E501
        self._edges = None
        self._edges_count = None
        self._edges_extra = None
        self._nodes = None
        self._nodes_count = None
        self._warning = None
        self.discriminator = None
        if edges is not None:
            self.edges = edges
        if edges_count is not None:
            self.edges_count = edges_count
        if edges_extra is not None:
            self.edges_extra = edges_extra
        if nodes is not None:
            self.nodes = nodes
        if nodes_count is not None:
            self.nodes_count = nodes_count
        if warning is not None:
            self.warning = warning

    @property
    def edges(self):
        """Gets the edges of this JsonExportResponse.  # noqa: E501


        :return: The edges of this JsonExportResponse.  # noqa: E501
        :rtype: list[JsonExportResponseEdges]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this JsonExportResponse.


        :param edges: The edges of this JsonExportResponse.  # noqa: E501
        :type: list[JsonExportResponseEdges]
        """

        self._edges = edges

    @property
    def edges_count(self):
        """Gets the edges_count of this JsonExportResponse.  # noqa: E501


        :return: The edges_count of this JsonExportResponse.  # noqa: E501
        :rtype: int
        """
        return self._edges_count

    @edges_count.setter
    def edges_count(self, edges_count):
        """Sets the edges_count of this JsonExportResponse.


        :param edges_count: The edges_count of this JsonExportResponse.  # noqa: E501
        :type: int
        """

        self._edges_count = edges_count

    @property
    def edges_extra(self):
        """Gets the edges_extra of this JsonExportResponse.  # noqa: E501


        :return: The edges_extra of this JsonExportResponse.  # noqa: E501
        :rtype: list[JsonExportResponseEdgesExtra]
        """
        return self._edges_extra

    @edges_extra.setter
    def edges_extra(self, edges_extra):
        """Sets the edges_extra of this JsonExportResponse.


        :param edges_extra: The edges_extra of this JsonExportResponse.  # noqa: E501
        :type: list[JsonExportResponseEdgesExtra]
        """

        self._edges_extra = edges_extra

    @property
    def nodes(self):
        """Gets the nodes of this JsonExportResponse.  # noqa: E501


        :return: The nodes of this JsonExportResponse.  # noqa: E501
        :rtype: list[JsonExportResponseNodes]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this JsonExportResponse.


        :param nodes: The nodes of this JsonExportResponse.  # noqa: E501
        :type: list[JsonExportResponseNodes]
        """

        self._nodes = nodes

    @property
    def nodes_count(self):
        """Gets the nodes_count of this JsonExportResponse.  # noqa: E501


        :return: The nodes_count of this JsonExportResponse.  # noqa: E501
        :rtype: int
        """
        return self._nodes_count

    @nodes_count.setter
    def nodes_count(self, nodes_count):
        """Sets the nodes_count of this JsonExportResponse.


        :param nodes_count: The nodes_count of this JsonExportResponse.  # noqa: E501
        :type: int
        """

        self._nodes_count = nodes_count

    @property
    def warning(self):
        """Gets the warning of this JsonExportResponse.  # noqa: E501


        :return: The warning of this JsonExportResponse.  # noqa: E501
        :rtype: JSONIndividualRouteResponseWarnings
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this JsonExportResponse.


        :param warning: The warning of this JsonExportResponse.  # noqa: E501
        :type: JSONIndividualRouteResponseWarnings
        """

        self._warning = warning

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
        if issubclass(JsonExportResponse, dict):
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
        if not isinstance(other, JsonExportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
