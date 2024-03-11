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

class JSONIndividualRouteResponseLegs(object):
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
        'arrival': 'datetime',
        'departure': 'datetime',
        'departure_location': 'str',
        'distance': 'float',
        'duration': 'float',
        'feed_id': 'str',
        'geometry': 'str',
        'instructions': 'list[JSONIndividualRouteResponseInstructions]',
        'is_in_same_vehicle_as_previous': 'bool',
        'route_desc': 'str',
        'route_id': 'str',
        'route_long_name': 'str',
        'route_short_name': 'str',
        'route_type': 'int',
        'stops': 'list[JSONIndividualRouteResponseStops]',
        'trip_headsign': 'str',
        'trip_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'arrival': 'arrival',
        'departure': 'departure',
        'departure_location': 'departure_location',
        'distance': 'distance',
        'duration': 'duration',
        'feed_id': 'feed_id',
        'geometry': 'geometry',
        'instructions': 'instructions',
        'is_in_same_vehicle_as_previous': 'is_in_same_vehicle_as_previous',
        'route_desc': 'route_desc',
        'route_id': 'route_id',
        'route_long_name': 'route_long_name',
        'route_short_name': 'route_short_name',
        'route_type': 'route_type',
        'stops': 'stops',
        'trip_headsign': 'trip_headsign',
        'trip_id': 'trip_id',
        'type': 'type'
    }

    def __init__(self, arrival=None, departure=None, departure_location=None, distance=None, duration=None, feed_id=None, geometry=None, instructions=None, is_in_same_vehicle_as_previous=None, route_desc=None, route_id=None, route_long_name=None, route_short_name=None, route_type=None, stops=None, trip_headsign=None, trip_id=None, type=None):  # noqa: E501
        """JSONIndividualRouteResponseLegs - a model defined in Swagger"""  # noqa: E501
        self._arrival = None
        self._departure = None
        self._departure_location = None
        self._distance = None
        self._duration = None
        self._feed_id = None
        self._geometry = None
        self._instructions = None
        self._is_in_same_vehicle_as_previous = None
        self._route_desc = None
        self._route_id = None
        self._route_long_name = None
        self._route_short_name = None
        self._route_type = None
        self._stops = None
        self._trip_headsign = None
        self._trip_id = None
        self._type = None
        self.discriminator = None
        if arrival is not None:
            self.arrival = arrival
        if departure is not None:
            self.departure = departure
        if departure_location is not None:
            self.departure_location = departure_location
        if distance is not None:
            self.distance = distance
        if duration is not None:
            self.duration = duration
        if feed_id is not None:
            self.feed_id = feed_id
        if geometry is not None:
            self.geometry = geometry
        if instructions is not None:
            self.instructions = instructions
        if is_in_same_vehicle_as_previous is not None:
            self.is_in_same_vehicle_as_previous = is_in_same_vehicle_as_previous
        if route_desc is not None:
            self.route_desc = route_desc
        if route_id is not None:
            self.route_id = route_id
        if route_long_name is not None:
            self.route_long_name = route_long_name
        if route_short_name is not None:
            self.route_short_name = route_short_name
        if route_type is not None:
            self.route_type = route_type
        if stops is not None:
            self.stops = stops
        if trip_headsign is not None:
            self.trip_headsign = trip_headsign
        if trip_id is not None:
            self.trip_id = trip_id
        if type is not None:
            self.type = type

    @property
    def arrival(self):
        """Gets the arrival of this JSONIndividualRouteResponseLegs.  # noqa: E501

        Arrival date and time  # noqa: E501

        :return: The arrival of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: datetime
        """
        return self._arrival

    @arrival.setter
    def arrival(self, arrival):
        """Sets the arrival of this JSONIndividualRouteResponseLegs.

        Arrival date and time  # noqa: E501

        :param arrival: The arrival of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: datetime
        """

        self._arrival = arrival

    @property
    def departure(self):
        """Gets the departure of this JSONIndividualRouteResponseLegs.  # noqa: E501

        Departure date and time  # noqa: E501

        :return: The departure of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: datetime
        """
        return self._departure

    @departure.setter
    def departure(self, departure):
        """Sets the departure of this JSONIndividualRouteResponseLegs.

        Departure date and time  # noqa: E501

        :param departure: The departure of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: datetime
        """

        self._departure = departure

    @property
    def departure_location(self):
        """Gets the departure_location of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The departure location of the leg.  # noqa: E501

        :return: The departure_location of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._departure_location

    @departure_location.setter
    def departure_location(self, departure_location):
        """Sets the departure_location of this JSONIndividualRouteResponseLegs.

        The departure location of the leg.  # noqa: E501

        :param departure_location: The departure_location of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._departure_location = departure_location

    @property
    def distance(self):
        """Gets the distance of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The distance for the leg in metres.  # noqa: E501

        :return: The distance of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this JSONIndividualRouteResponseLegs.

        The distance for the leg in metres.  # noqa: E501

        :param distance: The distance of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def duration(self):
        """Gets the duration of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The duration for the leg in seconds.  # noqa: E501

        :return: The duration of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this JSONIndividualRouteResponseLegs.

        The duration for the leg in seconds.  # noqa: E501

        :param duration: The duration of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def feed_id(self):
        """Gets the feed_id of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The feed ID this public transport leg based its information from.  # noqa: E501

        :return: The feed_id of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this JSONIndividualRouteResponseLegs.

        The feed ID this public transport leg based its information from.  # noqa: E501

        :param feed_id: The feed_id of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._feed_id = feed_id

    @property
    def geometry(self):
        """Gets the geometry of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The geometry of the leg. This is an encoded polyline.  # noqa: E501

        :return: The geometry of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this JSONIndividualRouteResponseLegs.

        The geometry of the leg. This is an encoded polyline.  # noqa: E501

        :param geometry: The geometry of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._geometry = geometry

    @property
    def instructions(self):
        """Gets the instructions of this JSONIndividualRouteResponseLegs.  # noqa: E501

        List containing the specific steps the segment consists of.  # noqa: E501

        :return: The instructions of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: list[JSONIndividualRouteResponseInstructions]
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this JSONIndividualRouteResponseLegs.

        List containing the specific steps the segment consists of.  # noqa: E501

        :param instructions: The instructions of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: list[JSONIndividualRouteResponseInstructions]
        """

        self._instructions = instructions

    @property
    def is_in_same_vehicle_as_previous(self):
        """Gets the is_in_same_vehicle_as_previous of this JSONIndividualRouteResponseLegs.  # noqa: E501

        Whether the legs continues in the same vehicle as the previous one.  # noqa: E501

        :return: The is_in_same_vehicle_as_previous of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_same_vehicle_as_previous

    @is_in_same_vehicle_as_previous.setter
    def is_in_same_vehicle_as_previous(self, is_in_same_vehicle_as_previous):
        """Sets the is_in_same_vehicle_as_previous of this JSONIndividualRouteResponseLegs.

        Whether the legs continues in the same vehicle as the previous one.  # noqa: E501

        :param is_in_same_vehicle_as_previous: The is_in_same_vehicle_as_previous of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: bool
        """

        self._is_in_same_vehicle_as_previous = is_in_same_vehicle_as_previous

    @property
    def route_desc(self):
        """Gets the route_desc of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The route description of the leg (if provided in the GTFS data set).  # noqa: E501

        :return: The route_desc of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._route_desc

    @route_desc.setter
    def route_desc(self, route_desc):
        """Sets the route_desc of this JSONIndividualRouteResponseLegs.

        The route description of the leg (if provided in the GTFS data set).  # noqa: E501

        :param route_desc: The route_desc of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._route_desc = route_desc

    @property
    def route_id(self):
        """Gets the route_id of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The route ID of this public transport leg.  # noqa: E501

        :return: The route_id of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this JSONIndividualRouteResponseLegs.

        The route ID of this public transport leg.  # noqa: E501

        :param route_id: The route_id of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._route_id = route_id

    @property
    def route_long_name(self):
        """Gets the route_long_name of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The public transport route name of the leg.  # noqa: E501

        :return: The route_long_name of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._route_long_name

    @route_long_name.setter
    def route_long_name(self, route_long_name):
        """Sets the route_long_name of this JSONIndividualRouteResponseLegs.

        The public transport route name of the leg.  # noqa: E501

        :param route_long_name: The route_long_name of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._route_long_name = route_long_name

    @property
    def route_short_name(self):
        """Gets the route_short_name of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The public transport route name (short version) of the leg.  # noqa: E501

        :return: The route_short_name of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._route_short_name

    @route_short_name.setter
    def route_short_name(self, route_short_name):
        """Sets the route_short_name of this JSONIndividualRouteResponseLegs.

        The public transport route name (short version) of the leg.  # noqa: E501

        :param route_short_name: The route_short_name of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._route_short_name = route_short_name

    @property
    def route_type(self):
        """Gets the route_type of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The route type of the leg (if provided in the GTFS data set).  # noqa: E501

        :return: The route_type of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: int
        """
        return self._route_type

    @route_type.setter
    def route_type(self, route_type):
        """Sets the route_type of this JSONIndividualRouteResponseLegs.

        The route type of the leg (if provided in the GTFS data set).  # noqa: E501

        :param route_type: The route_type of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: int
        """

        self._route_type = route_type

    @property
    def stops(self):
        """Gets the stops of this JSONIndividualRouteResponseLegs.  # noqa: E501

        List containing the stops the along the leg.  # noqa: E501

        :return: The stops of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: list[JSONIndividualRouteResponseStops]
        """
        return self._stops

    @stops.setter
    def stops(self, stops):
        """Sets the stops of this JSONIndividualRouteResponseLegs.

        List containing the stops the along the leg.  # noqa: E501

        :param stops: The stops of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: list[JSONIndividualRouteResponseStops]
        """

        self._stops = stops

    @property
    def trip_headsign(self):
        """Gets the trip_headsign of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The headsign of the public transport vehicle of the leg.  # noqa: E501

        :return: The trip_headsign of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._trip_headsign

    @trip_headsign.setter
    def trip_headsign(self, trip_headsign):
        """Sets the trip_headsign of this JSONIndividualRouteResponseLegs.

        The headsign of the public transport vehicle of the leg.  # noqa: E501

        :param trip_headsign: The trip_headsign of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._trip_headsign = trip_headsign

    @property
    def trip_id(self):
        """Gets the trip_id of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The trip ID of this public transport leg.  # noqa: E501

        :return: The trip_id of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._trip_id

    @trip_id.setter
    def trip_id(self, trip_id):
        """Sets the trip_id of this JSONIndividualRouteResponseLegs.

        The trip ID of this public transport leg.  # noqa: E501

        :param trip_id: The trip_id of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :type: str
        """

        self._trip_id = trip_id

    @property
    def type(self):
        """Gets the type of this JSONIndividualRouteResponseLegs.  # noqa: E501

        The type of the leg, possible values are currently 'walk' and 'pt'.  # noqa: E501

        :return: The type of this JSONIndividualRouteResponseLegs.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JSONIndividualRouteResponseLegs.

        The type of the leg, possible values are currently 'walk' and 'pt'.  # noqa: E501

        :param type: The type of this JSONIndividualRouteResponseLegs.  # noqa: E501
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
        if issubclass(JSONIndividualRouteResponseLegs, dict):
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
        if not isinstance(other, JSONIndividualRouteResponseLegs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
