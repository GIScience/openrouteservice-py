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

class ProfileParametersRestrictions(object):
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
        'axleload': 'float',
        'hazmat': 'bool',
        'height': 'float',
        'length': 'float',
        'maximum_incline': 'int',
        'maximum_sloped_kerb': 'float',
        'minimum_width': 'float',
        'smoothness_type': 'str',
        'surface_type': 'str',
        'track_type': 'str',
        'weight': 'float',
        'width': 'float'
    }

    attribute_map = {
        'axleload': 'axleload',
        'hazmat': 'hazmat',
        'height': 'height',
        'length': 'length',
        'maximum_incline': 'maximum_incline',
        'maximum_sloped_kerb': 'maximum_sloped_kerb',
        'minimum_width': 'minimum_width',
        'smoothness_type': 'smoothness_type',
        'surface_type': 'surface_type',
        'track_type': 'track_type',
        'weight': 'weight',
        'width': 'width'
    }

    def __init__(self, axleload=None, hazmat=False, height=None, length=None, maximum_incline=6, maximum_sloped_kerb=0.6, minimum_width=None, smoothness_type='good', surface_type='sett', track_type='grade1', weight=None, width=None):  # noqa: E501
        """ProfileParametersRestrictions - a model defined in Swagger"""  # noqa: E501
        self._axleload = None
        self._hazmat = None
        self._height = None
        self._length = None
        self._maximum_incline = None
        self._maximum_sloped_kerb = None
        self._minimum_width = None
        self._smoothness_type = None
        self._surface_type = None
        self._track_type = None
        self._weight = None
        self._width = None
        self.discriminator = None
        if axleload is not None:
            self.axleload = axleload
        if hazmat is not None:
            self.hazmat = hazmat
        if height is not None:
            self.height = height
        if length is not None:
            self.length = length
        if maximum_incline is not None:
            self.maximum_incline = maximum_incline
        if maximum_sloped_kerb is not None:
            self.maximum_sloped_kerb = maximum_sloped_kerb
        if minimum_width is not None:
            self.minimum_width = minimum_width
        if smoothness_type is not None:
            self.smoothness_type = smoothness_type
        if surface_type is not None:
            self.surface_type = surface_type
        if track_type is not None:
            self.track_type = track_type
        if weight is not None:
            self.weight = weight
        if width is not None:
            self.width = width

    @property
    def axleload(self):
        """Gets the axleload of this ProfileParametersRestrictions.  # noqa: E501

        Axleload restriction in tons.  # noqa: E501

        :return: The axleload of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._axleload

    @axleload.setter
    def axleload(self, axleload):
        """Sets the axleload of this ProfileParametersRestrictions.

        Axleload restriction in tons.  # noqa: E501

        :param axleload: The axleload of this ProfileParametersRestrictions.  # noqa: E501
        :type: float
        """

        self._axleload = axleload

    @property
    def hazmat(self):
        """Gets the hazmat of this ProfileParametersRestrictions.  # noqa: E501

        Specifies whether to use appropriate routing for delivering hazardous goods and avoiding water protected areas. Default is `false`.   # noqa: E501

        :return: The hazmat of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: bool
        """
        return self._hazmat

    @hazmat.setter
    def hazmat(self, hazmat):
        """Sets the hazmat of this ProfileParametersRestrictions.

        Specifies whether to use appropriate routing for delivering hazardous goods and avoiding water protected areas. Default is `false`.   # noqa: E501

        :param hazmat: The hazmat of this ProfileParametersRestrictions.  # noqa: E501
        :type: bool
        """

        self._hazmat = hazmat

    @property
    def height(self):
        """Gets the height of this ProfileParametersRestrictions.  # noqa: E501

        Height restriction in metres.   # noqa: E501

        :return: The height of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ProfileParametersRestrictions.

        Height restriction in metres.   # noqa: E501

        :param height: The height of this ProfileParametersRestrictions.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def length(self):
        """Gets the length of this ProfileParametersRestrictions.  # noqa: E501

        Length restriction in metres.  # noqa: E501

        :return: The length of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this ProfileParametersRestrictions.

        Length restriction in metres.  # noqa: E501

        :param length: The length of this ProfileParametersRestrictions.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def maximum_incline(self):
        """Gets the maximum_incline of this ProfileParametersRestrictions.  # noqa: E501

        Specifies the maximum incline as a percentage. `3`, `6` (default), `10`, `15.  # noqa: E501

        :return: The maximum_incline of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: int
        """
        return self._maximum_incline

    @maximum_incline.setter
    def maximum_incline(self, maximum_incline):
        """Sets the maximum_incline of this ProfileParametersRestrictions.

        Specifies the maximum incline as a percentage. `3`, `6` (default), `10`, `15.  # noqa: E501

        :param maximum_incline: The maximum_incline of this ProfileParametersRestrictions.  # noqa: E501
        :type: int
        """

        self._maximum_incline = maximum_incline

    @property
    def maximum_sloped_kerb(self):
        """Gets the maximum_sloped_kerb of this ProfileParametersRestrictions.  # noqa: E501

        Specifies the maximum height of the sloped curb in metres. Values are `0.03`, `0.06` (default), `0.1`.  # noqa: E501

        :return: The maximum_sloped_kerb of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._maximum_sloped_kerb

    @maximum_sloped_kerb.setter
    def maximum_sloped_kerb(self, maximum_sloped_kerb):
        """Sets the maximum_sloped_kerb of this ProfileParametersRestrictions.

        Specifies the maximum height of the sloped curb in metres. Values are `0.03`, `0.06` (default), `0.1`.  # noqa: E501

        :param maximum_sloped_kerb: The maximum_sloped_kerb of this ProfileParametersRestrictions.  # noqa: E501
        :type: float
        """

        self._maximum_sloped_kerb = maximum_sloped_kerb

    @property
    def minimum_width(self):
        """Gets the minimum_width of this ProfileParametersRestrictions.  # noqa: E501

        Specifies the minimum width of the footway in metres.  # noqa: E501

        :return: The minimum_width of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._minimum_width

    @minimum_width.setter
    def minimum_width(self, minimum_width):
        """Sets the minimum_width of this ProfileParametersRestrictions.

        Specifies the minimum width of the footway in metres.  # noqa: E501

        :param minimum_width: The minimum_width of this ProfileParametersRestrictions.  # noqa: E501
        :type: float
        """

        self._minimum_width = minimum_width

    @property
    def smoothness_type(self):
        """Gets the smoothness_type of this ProfileParametersRestrictions.  # noqa: E501

        Specifies the minimum smoothness of the route. Default is `good`.  # noqa: E501

        :return: The smoothness_type of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: str
        """
        return self._smoothness_type

    @smoothness_type.setter
    def smoothness_type(self, smoothness_type):
        """Sets the smoothness_type of this ProfileParametersRestrictions.

        Specifies the minimum smoothness of the route. Default is `good`.  # noqa: E501

        :param smoothness_type: The smoothness_type of this ProfileParametersRestrictions.  # noqa: E501
        :type: str
        """
        allowed_values = ["excellent", "good", "intermediate", "bad", "very_bad", "horrible", "very_horrible", "impassable"]  # noqa: E501
        if smoothness_type not in allowed_values:
            raise ValueError(
                "Invalid value for `smoothness_type` ({0}), must be one of {1}"  # noqa: E501
                .format(smoothness_type, allowed_values)
            )

        self._smoothness_type = smoothness_type

    @property
    def surface_type(self):
        """Gets the surface_type of this ProfileParametersRestrictions.  # noqa: E501

        Specifies the minimum surface type. Default is `sett`.   # noqa: E501

        :return: The surface_type of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: str
        """
        return self._surface_type

    @surface_type.setter
    def surface_type(self, surface_type):
        """Sets the surface_type of this ProfileParametersRestrictions.

        Specifies the minimum surface type. Default is `sett`.   # noqa: E501

        :param surface_type: The surface_type of this ProfileParametersRestrictions.  # noqa: E501
        :type: str
        """

        self._surface_type = surface_type

    @property
    def track_type(self):
        """Gets the track_type of this ProfileParametersRestrictions.  # noqa: E501

        Specifies the minimum grade of the route. Default is `grade1`.   # noqa: E501

        :return: The track_type of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: str
        """
        return self._track_type

    @track_type.setter
    def track_type(self, track_type):
        """Sets the track_type of this ProfileParametersRestrictions.

        Specifies the minimum grade of the route. Default is `grade1`.   # noqa: E501

        :param track_type: The track_type of this ProfileParametersRestrictions.  # noqa: E501
        :type: str
        """

        self._track_type = track_type

    @property
    def weight(self):
        """Gets the weight of this ProfileParametersRestrictions.  # noqa: E501

        Weight restriction in tons.   # noqa: E501

        :return: The weight of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ProfileParametersRestrictions.

        Weight restriction in tons.   # noqa: E501

        :param weight: The weight of this ProfileParametersRestrictions.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def width(self):
        """Gets the width of this ProfileParametersRestrictions.  # noqa: E501

        Width restriction in metres.  # noqa: E501

        :return: The width of this ProfileParametersRestrictions.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ProfileParametersRestrictions.

        Width restriction in metres.  # noqa: E501

        :param width: The width of this ProfileParametersRestrictions.  # noqa: E501
        :type: float
        """

        self._width = width

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
        if issubclass(ProfileParametersRestrictions, dict):
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
        if not isinstance(other, ProfileParametersRestrictions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
