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

class OptimizationJobs(object):
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
        'delivery': 'list[float]',
        'description': 'str',
        'id': 'int',
        'location': 'list[list[float]]',
        'location_index': 'object',
        'pickup': 'list[float]',
        'priority': 'float',
        'service': 'object',
        'setup': 'float',
        'skills': 'list[int]',
        'time_windows': 'list[list[int]]'
    }

    attribute_map = {
        'delivery': 'delivery',
        'description': 'description',
        'id': 'id',
        'location': 'location',
        'location_index': 'location_index',
        'pickup': 'pickup',
        'priority': 'priority',
        'service': 'service',
        'setup': 'setup',
        'skills': 'skills',
        'time_windows': 'time_windows'
    }

    def __init__(self, delivery=None, description=None, id=None, location=None, location_index=None, pickup=None, priority=0, service=None, setup=None, skills=None, time_windows=None):  # noqa: E501
        """OptimizationJobs - a model defined in Swagger"""  # noqa: E501
        self._delivery = None
        self._description = None
        self._id = None
        self._location = None
        self._location_index = None
        self._pickup = None
        self._priority = None
        self._service = None
        self._setup = None
        self._skills = None
        self._time_windows = None
        self.discriminator = None
        if delivery is not None:
            self.delivery = delivery
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if location is not None:
            self.location = location
        if location_index is not None:
            self.location_index = location_index
        if pickup is not None:
            self.pickup = pickup
        if priority is not None:
            self.priority = priority
        if service is not None:
            self.service = service
        if setup is not None:
            self.setup = setup
        if skills is not None:
            self.skills = skills
        if time_windows is not None:
            self.time_windows = time_windows

    @property
    def delivery(self):
        """Gets the delivery of this OptimizationJobs.  # noqa: E501

        an array of integers describing multidimensional quantities for delivery   # noqa: E501

        :return: The delivery of this OptimizationJobs.  # noqa: E501
        :rtype: list[float]
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this OptimizationJobs.

        an array of integers describing multidimensional quantities for delivery   # noqa: E501

        :param delivery: The delivery of this OptimizationJobs.  # noqa: E501
        :type: list[float]
        """

        self._delivery = delivery

    @property
    def description(self):
        """Gets the description of this OptimizationJobs.  # noqa: E501

        a string describing this job   # noqa: E501

        :return: The description of this OptimizationJobs.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OptimizationJobs.

        a string describing this job   # noqa: E501

        :param description: The description of this OptimizationJobs.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this OptimizationJobs.  # noqa: E501

        an integer used as unique identifier   # noqa: E501

        :return: The id of this OptimizationJobs.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OptimizationJobs.

        an integer used as unique identifier   # noqa: E501

        :param id: The id of this OptimizationJobs.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this OptimizationJobs.  # noqa: E501

        coordinates array in `[lon, lat]`   # noqa: E501

        :return: The location of this OptimizationJobs.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this OptimizationJobs.

        coordinates array in `[lon, lat]`   # noqa: E501

        :param location: The location of this OptimizationJobs.  # noqa: E501
        :type: list[list[float]]
        """

        self._location = location

    @property
    def location_index(self):
        """Gets the location_index of this OptimizationJobs.  # noqa: E501

        index of relevant row and column in custom matrix   # noqa: E501

        :return: The location_index of this OptimizationJobs.  # noqa: E501
        :rtype: object
        """
        return self._location_index

    @location_index.setter
    def location_index(self, location_index):
        """Sets the location_index of this OptimizationJobs.

        index of relevant row and column in custom matrix   # noqa: E501

        :param location_index: The location_index of this OptimizationJobs.  # noqa: E501
        :type: object
        """

        self._location_index = location_index

    @property
    def pickup(self):
        """Gets the pickup of this OptimizationJobs.  # noqa: E501

        an array of integers describing multidimensional quantities for pickup   # noqa: E501

        :return: The pickup of this OptimizationJobs.  # noqa: E501
        :rtype: list[float]
        """
        return self._pickup

    @pickup.setter
    def pickup(self, pickup):
        """Sets the pickup of this OptimizationJobs.

        an array of integers describing multidimensional quantities for pickup   # noqa: E501

        :param pickup: The pickup of this OptimizationJobs.  # noqa: E501
        :type: list[float]
        """

        self._pickup = pickup

    @property
    def priority(self):
        """Gets the priority of this OptimizationJobs.  # noqa: E501

        an integer in the range [0, 100] describing priority level (defaults to 0)   # noqa: E501

        :return: The priority of this OptimizationJobs.  # noqa: E501
        :rtype: float
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this OptimizationJobs.

        an integer in the range [0, 100] describing priority level (defaults to 0)   # noqa: E501

        :param priority: The priority of this OptimizationJobs.  # noqa: E501
        :type: float
        """

        self._priority = priority

    @property
    def service(self):
        """Gets the service of this OptimizationJobs.  # noqa: E501

        job service duration (defaults to 0), in seconds   # noqa: E501

        :return: The service of this OptimizationJobs.  # noqa: E501
        :rtype: object
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this OptimizationJobs.

        job service duration (defaults to 0), in seconds   # noqa: E501

        :param service: The service of this OptimizationJobs.  # noqa: E501
        :type: object
        """

        self._service = service

    @property
    def setup(self):
        """Gets the setup of this OptimizationJobs.  # noqa: E501

        job setup duration (defaults to 0), in seconds   # noqa: E501

        :return: The setup of this OptimizationJobs.  # noqa: E501
        :rtype: float
        """
        return self._setup

    @setup.setter
    def setup(self, setup):
        """Sets the setup of this OptimizationJobs.

        job setup duration (defaults to 0), in seconds   # noqa: E501

        :param setup: The setup of this OptimizationJobs.  # noqa: E501
        :type: float
        """

        self._setup = setup

    @property
    def skills(self):
        """Gets the skills of this OptimizationJobs.  # noqa: E501

        Array of integers defining mandatory skills for this job   # noqa: E501

        :return: The skills of this OptimizationJobs.  # noqa: E501
        :rtype: list[int]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this OptimizationJobs.

        Array of integers defining mandatory skills for this job   # noqa: E501

        :param skills: The skills of this OptimizationJobs.  # noqa: E501
        :type: list[int]
        """

        self._skills = skills

    @property
    def time_windows(self):
        """Gets the time_windows of this OptimizationJobs.  # noqa: E501

        Array of `time_window` arrays describing valid slots for job service start and end, in week seconds, i.e. 28800 = Mon, 8 AM.   # noqa: E501

        :return: The time_windows of this OptimizationJobs.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._time_windows

    @time_windows.setter
    def time_windows(self, time_windows):
        """Sets the time_windows of this OptimizationJobs.

        Array of `time_window` arrays describing valid slots for job service start and end, in week seconds, i.e. 28800 = Mon, 8 AM.   # noqa: E501

        :param time_windows: The time_windows of this OptimizationJobs.  # noqa: E501
        :type: list[list[int]]
        """

        self._time_windows = time_windows

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
        if issubclass(OptimizationJobs, dict):
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
        if not isinstance(other, OptimizationJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other