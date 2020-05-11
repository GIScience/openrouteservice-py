# -*- coding: utf-8 -*-
# Copyright (C) 2018 HeiGIT, University of Heidelberg.
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

"""Performs requests to the ORS optimization API."""


def optimization(client,
                 jobs=None,
                 vehicles=None,
                 shipments=None,
                 matrix=None,
                 geometry=None,
                 dry_run=None):
    """Optimize a fleet of vehicles on a number of jobs.

    For more information, visit https://github.com/VROOM-Project/vroom/blob/master/docs/API.md.

    Example:

        >>> from openrouteservice import Client, optimization
        >>> coordinates = [[8.688641, 49.420577], [8.680916, 49.415776]]
        >>> jobs, vehicles = list(), list()
        >>> for idx, coord in enumerate(coordinates):
                jobs.append(optimization.Job(id=idx, location=coord))
                vehicles.append(optimization.Vehicle(id=idx, location=coord))
        >>> api = Client(key='somekey')
        >>> result = api.optimization(jobs=jobs, vehicles=vehicles)

    :param jobs: The Job objects to fulfill.
    :type jobs: list of Job

    :param vehicles: The vehicles to fulfill the :class:`openrouteservice.optimization.Job`'s.
    :type vehicles: list of Vehicle

    :param shipments: The Shipment objects to fulfill.
    :type shipments: list of Shipment

    :param matrix: Specify a custom cost matrix. If not specified, it will be calculated with
        the :meth:`openrouteservice.matrix.matrix` endpoint.
    :type matrix: list of lists of int

    :param geometry: If the geometry of the resulting routes should be calculated. Default False.
    :type geometry: bool

    :param dry_run: Print URL and parameters without sending the request.
    :param dry_run: boolean

    :returns: Response of optimization endpoint.
    :rtype: dict
    """

    assert all([isinstance(x, Vehicle) for x in vehicles])

    params = {"vehicles": [vehicle.__dict__ for vehicle in vehicles]}

    if jobs:
        assert all([isinstance(x, Job) for x in jobs])
        params['jobs'] = [job.__dict__ for job in jobs]
    if shipments:
        assert all([isinstance(x, Shipment) for x in shipments])
        params['shipments'] = list()

        for shipment in shipments:
            shipment_dict = dict()
            if getattr(shipment, 'pickup'):
                assert isinstance(shipment.pickup, ShipmentStep)
                shipment_dict['pickup'] = shipment.pickup.__dict__
            if getattr(shipment, 'delivery'):
                assert isinstance(shipment.delivery, ShipmentStep)
                shipment_dict['delivery'] = shipment.delivery.__dict__
            shipment_dict['amount'] = shipment.amount
            shipment_dict['skills'] = shipment.skills
            shipment_dict['priority'] = shipment.priority

            params['shipments'].append(shipment_dict)

    if geometry is not None:
        params.update({"options": {"g": geometry}})

    if matrix:
        params['matrix'] = matrix

    return client.request("/optimization", {}, post_json=params, dry_run=dry_run)


class Job(object):
    """
    Class to create a Job object for optimization endpoint.

    Full documentation at https://github.com/VROOM-Project/vroom/blob/master/docs/API.md#jobs.
    """
    def __init__(self,
                 id,
                 location=None,
                 location_index=None,
                 service=None,
                 amount=None,
                 skills=None,
                 priority=None,
                 time_windows=None
                 ):
        """
        Create a job object for the optimization endpoint.

        :param id: Integer used as unique identifier.
        :type id: int

        :param location: Location of the job, as [lon, lat]. Optional if custom matrix is provided.
        :type location: tuple of float or list of float

        :param location_index: Index of relevant row and column in custom matrix. Mandatory if custom
            matrix is provided. Irrelevant when no custom matrix is provided.
        :type location_index: int

        :param service: Optional job service duration in seconds
        :type service: int

        :param amount: An array of integers describing multidimensional quantities.
        :type amount: list of int or tuple of int

        :param skills: An array of integers defining mandatory skills for this job.
        :type skills: list of int or tuple of int

        :param priority: An integer in the [0, 10] range describing priority level (defaults to 0).
        :type priority: int

        :param time_windows: An array of time_window objects describing valid slots for job service start.
        :type time_windows: list of lists of int
        """

        self.id = id

        if location is not None:
            self.location = location

        if location_index is not None:
            self.location_index = location_index

        if service is not None:
            self.service = service

        if amount is not None:
            self.amount = amount

        if skills is not None:
            self.skills = skills

        if priority is not None:
            self.priority = priority

        if time_windows is not None:
            self.time_windows = time_windows


class ShipmentStep(object):
    """
    Class to create a Shipment object for optimization endpoint.

    Full documentation at https://github.com/VROOM-Project/vroom/blob/master/docs/API.md#shipments.
    """
    def __init__(self,
                 id=None,
                 location=None,
                 location_index=None,
                 service=None,
                 time_windows=None
                 ):
        """
        Create a shipment step object for the optimization endpoint.

        :param id: Integer used as unique identifier.
        :type id: int

        :param location: Location of the job, as [lon, lat]. Optional if custom matrix is provided.
        :type location: tuple of float or list of float

        :param location_index: Index of relevant row and column in custom matrix. Mandatory if custom
            matrix is provided. Irrelevant when no custom matrix is provided.
        :type location_index: int

        :param service: Optional job service duration in seconds
        :type service: int

        :param time_windows: An array of time_window objects describing valid slots for job service start.
        :type time_windows: list of lists of int
        """

        self.id = id

        if location is not None:
            self.location = location

        if location_index is not None:
            self.location_index = location_index

        if service is not None:
            self.service = service

        if time_windows is not None:
            self.time_windows = time_windows


class Shipment(object):
    """
    Class to create a Shipment object for optimization endpoint.

    Full documentation at https://github.com/VROOM-Project/vroom/blob/master/docs/API.md#shipments.
    """
    def __init__(self,
                 pickup=None,
                 delivery=None,
                 amount=None,
                 skills=None,
                 priority=None
                 ):
        """
        Create a shipment object for the optimization endpoint.

        :param pickup: a ShipmentStep object describing pickup
        :type pickup: ShipmentStep

        :param delivery: a ShipmentStep object describing delivery
        :type delivery: ShipmentStep

        :param amount: An array of integers describing multidimensional quantities.
        :type amount: list of int or tuple of int

        :param skills: An array of integers defining mandatory skills.
        :type skills: list of int or tuple of int

        :param priority: An integer in the [0, 10] range describing priority level (defaults to 0).
        :type priority: int
        """

        if pickup is not None:
            self.pickup = pickup

        if delivery is not None:
            self.delivery = delivery

        if amount is not None:
            self.amount = amount

        if skills is not None:
            self.skills = skills

        if priority is not None:
            self.priority = priority


class Vehicle(object):
    """
    Class to create a Vehicle object for optimization endpoint.

    Full documentation at https://github.com/VROOM-Project/vroom/blob/master/docs/API.md#vehicles.
    """

    def __init__(self,
                 id,
                 profile='driving-car',
                 start=None,
                 start_index=None,
                 end=None,
                 end_index=None,
                 capacity=None,
                 skills=None,
                 time_window=None):
        """
        Create a Vehicle object for the optimization endpoint.

        :param id: Integer used as unique identifier.
        :param id: int

        :param profile: Specifies the mode of transport to use when calculating
            directions. One of ["driving-car", "driving-hgv", "foot-walking",
            "foot-hiking", "cycling-regular", "cycling-road","cycling-mountain",
            "cycling-electric",]. Default "driving-car".
        :type profile: str

        :param start: Coordinate for the vehicle to start from. If not specified, the start
            location will be the first visited job, determined by the optimization engine.
        :type start: list of float or tuple of float

        :param start_index: Index of relevant row and column in custom matrix. Irrelevant
            if no custom matrix is provided.
        :type start_index: int

        :param end: Coordinate for the vehicle to end at. If not specified, the end
            location will be the last visited job, determined by the optimization engine.
        :type end: list of float or tuple of float

        :param end_index: Index of relevant row and column in custom matrix. Irrelevant
            if no custom matrix is provided.
        :type end_index: int

        :param capacity: An array of integers describing multidimensional quantities.
        :type capacity: list of int or tuple of int

        :param skills: An array of integers defining skills for this vehicle.
        :param skills: list of int or tuple of int

        :param time_window: A time_window object describing working hours for this vehicle.
        :param time_window: list of int or tuple of int
        """

        self.id = id
        self.profile = profile

        if start is not None:
            self.start = start

        if start_index is not None:
            self.start_index = start_index

        if end is not None:
            self.end = end

        if end_index is not None:
            self.end_index = end_index

        if capacity is not None:
            self.capacity = capacity

        if skills is not None:
            self.skills = skills

        if time_window is not None:
            self.time_window = time_window
