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

class JSONIndividualRouteResponseInstructions(object):
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
        'distance': 'float',
        'duration': 'float',
        'exit_bearings': 'list[int]',
        'exit_number': 'int',
        'instruction': 'str',
        'maneuver': 'JSONIndividualRouteResponseManeuver',
        'name': 'str',
        'type': 'int',
        'way_points': 'list[int]'
    }

    attribute_map = {
        'distance': 'distance',
        'duration': 'duration',
        'exit_bearings': 'exit_bearings',
        'exit_number': 'exit_number',
        'instruction': 'instruction',
        'maneuver': 'maneuver',
        'name': 'name',
        'type': 'type',
        'way_points': 'way_points'
    }

    def __init__(self, distance=None, duration=None, exit_bearings=None, exit_number=None, instruction=None, maneuver=None, name=None, type=None, way_points=None):  # noqa: E501
        """JSONIndividualRouteResponseInstructions - a model defined in Swagger"""  # noqa: E501
        self._distance = None
        self._duration = None
        self._exit_bearings = None
        self._exit_number = None
        self._instruction = None
        self._maneuver = None
        self._name = None
        self._type = None
        self._way_points = None
        self.discriminator = None
        if distance is not None:
            self.distance = distance
        if duration is not None:
            self.duration = duration
        if exit_bearings is not None:
            self.exit_bearings = exit_bearings
        if exit_number is not None:
            self.exit_number = exit_number
        if instruction is not None:
            self.instruction = instruction
        if maneuver is not None:
            self.maneuver = maneuver
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if way_points is not None:
            self.way_points = way_points

    @property
    def distance(self):
        """Gets the distance of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        The distance for the step in metres.  # noqa: E501

        :return: The distance of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this JSONIndividualRouteResponseInstructions.

        The distance for the step in metres.  # noqa: E501

        :param distance: The distance of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def duration(self):
        """Gets the duration of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        The duration for the step in seconds.  # noqa: E501

        :return: The duration of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this JSONIndividualRouteResponseInstructions.

        The duration for the step in seconds.  # noqa: E501

        :param duration: The duration of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def exit_bearings(self):
        """Gets the exit_bearings of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        Contains the bearing of the entrance and all passed exits in a roundabout.  # noqa: E501

        :return: The exit_bearings of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: list[int]
        """
        return self._exit_bearings

    @exit_bearings.setter
    def exit_bearings(self, exit_bearings):
        """Sets the exit_bearings of this JSONIndividualRouteResponseInstructions.

        Contains the bearing of the entrance and all passed exits in a roundabout.  # noqa: E501

        :param exit_bearings: The exit_bearings of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: list[int]
        """

        self._exit_bearings = exit_bearings

    @property
    def exit_number(self):
        """Gets the exit_number of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        Only for roundabouts. Contains the number of the exit to take.  # noqa: E501

        :return: The exit_number of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: int
        """
        return self._exit_number

    @exit_number.setter
    def exit_number(self, exit_number):
        """Sets the exit_number of this JSONIndividualRouteResponseInstructions.

        Only for roundabouts. Contains the number of the exit to take.  # noqa: E501

        :param exit_number: The exit_number of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: int
        """

        self._exit_number = exit_number

    @property
    def instruction(self):
        """Gets the instruction of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        The routing instruction text for the step.  # noqa: E501

        :return: The instruction of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        """Sets the instruction of this JSONIndividualRouteResponseInstructions.

        The routing instruction text for the step.  # noqa: E501

        :param instruction: The instruction of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: str
        """

        self._instruction = instruction

    @property
    def maneuver(self):
        """Gets the maneuver of this JSONIndividualRouteResponseInstructions.  # noqa: E501


        :return: The maneuver of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: JSONIndividualRouteResponseManeuver
        """
        return self._maneuver

    @maneuver.setter
    def maneuver(self, maneuver):
        """Sets the maneuver of this JSONIndividualRouteResponseInstructions.


        :param maneuver: The maneuver of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: JSONIndividualRouteResponseManeuver
        """

        self._maneuver = maneuver

    @property
    def name(self):
        """Gets the name of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        The name of the next street.  # noqa: E501

        :return: The name of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JSONIndividualRouteResponseInstructions.

        The name of the next street.  # noqa: E501

        :param name: The name of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        The [instruction](https://GIScience.github.io/openrouteservice/documentation/Instruction-Types.html) action for symbolisation purposes.  # noqa: E501

        :return: The type of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JSONIndividualRouteResponseInstructions.

        The [instruction](https://GIScience.github.io/openrouteservice/documentation/Instruction-Types.html) action for symbolisation purposes.  # noqa: E501

        :param type: The type of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def way_points(self):
        """Gets the way_points of this JSONIndividualRouteResponseInstructions.  # noqa: E501

        List containing the indices of the steps start- and endpoint corresponding to the *geometry*.  # noqa: E501

        :return: The way_points of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :rtype: list[int]
        """
        return self._way_points

    @way_points.setter
    def way_points(self, way_points):
        """Sets the way_points of this JSONIndividualRouteResponseInstructions.

        List containing the indices of the steps start- and endpoint corresponding to the *geometry*.  # noqa: E501

        :param way_points: The way_points of this JSONIndividualRouteResponseInstructions.  # noqa: E501
        :type: list[int]
        """

        self._way_points = way_points

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
        if issubclass(JSONIndividualRouteResponseInstructions, dict):
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
        if not isinstance(other, JSONIndividualRouteResponseInstructions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
