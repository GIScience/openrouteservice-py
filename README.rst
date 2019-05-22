.. image:: https://travis-ci.com/GIScience/openrouteservice-py.svg?branch=master
    :target: https://travis-ci.com/GIScience/openrouteservice-py
    :alt: Build status

.. image:: https://coveralls.io/repos/github/GIScience/openrouteservice-py/badge.svg?branch=master
    :target: https://coveralls.io/github/GIScience/openrouteservice-py?branch=master
    :alt: Coveralls coverage

.. image:: https://readthedocs.org/projects/openrouteservice-py/badge/?version=latest
   :target: http://openrouteservice-py.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://badge.fury.io/py/openrouteservice.svg
    :target: https://badge.fury.io/py/openrouteservice
    :alt: PyPI version

.. image:: https://anaconda.org/nilsnolde/openrouteservice/badges/installer/conda.svg
    :target: https://conda.anaconda.org/nilsnolde/openrouteservice
    :alt: Conda install

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/GIScience/openrouteservice-py/master?filepath=examples%2Fbasic_example.ipynb
    :alt: MyBinder

Quickstart
==================================================

Description
--------------------------------------------------
The openrouteservice library gives you painless access to the openrouteservice_ (ORS) routing API's.
It performs requests against our API's for

- directions_
- isochrones_
- `matrix routing calculations`_
- places_
- elevation_
- `Pelias geocoding`_
- `Pelias reverse geocoding`_
- `Pelias structured geocoding`_
- `Pelias autocomplete`_
- Optimization_

For further details, please visit:

- homepage_
- `ORS API documentation`_
- `openrouteservice-py documentation`_

We also have a repo with a few useful examples here_.

For support, please ask our forum_.

By using this library, you agree to the ORS `terms and conditions`_.

.. _openrouteservice: https://openrouteservice.org
.. _homepage: https://openrouteservice.org
.. _`ORS API documentation`: https://openrouteservice.org/documentation/
.. _`openrouteservice-py documentation`: http://openrouteservice-py.readthedocs.io/en/latest/
.. _directions: https://openrouteservice.org/documentation/#/reference/directions/directions/directions-service
.. _`Pelias geocoding`: https://github.com/pelias/documentation/blob/master/search.md#available-search-parameters
.. _`Pelias reverse geocoding`: https://github.com/pelias/documentation/blob/master/reverse.md#reverse-geocoding-parameters
.. _`Pelias structured geocoding`: https://github.com/pelias/documentation/blob/master/structured-geocoding.md
.. _`Pelias autocomplete`: https://github.com/pelias/documentation/blob/master/autocomplete.md
.. _isochrones: https://openrouteservice.org/documentation/#/reference/isochrones/isochrones/isochrones-service
.. _elevation: https://github.com/GIScience/openelevationservice/
.. _`reverse geocoding`: https://openrouteservice.org/documentation/#/reference/geocoding/geocoding/geocoding-service
.. _`matrix routing calculations`: https://openrouteservice.org/documentation/#/reference/matrix/matrix/matrix-service-(post)
.. _places: https://github.com/GIScience/openpoiservice
.. _Optimization: https://github.com/VROOM-Project/vroom/blob/master/docs/API.md
.. _here: https://github.com/GIScience/openrouteservice-examples/tree/master/python
.. _`terms and conditions`: https://openrouteservice.org/terms-of-service/
.. _forum: https://ask.openrouteservice.org/c/sdks

Requirements
-----------------------------
openrouteservice-py is tested against CPython 2.7, 3.4, 3.5, 3.6, 3.7 and 3.8-dev, and PyPy3.5.

For setting up a testing environment, install ``requirements-dev.txt``::

    pip install -r requirements-dev.txt

Installation
------------------------------
To install from PyPI, simply use pip::

	pip install openrouteservice

To install the latest and greatest from source::

   	pip install git+git://github.com/GIScience/openrouteservice-py@development

For ``conda`` users::

  conda install -c nilsnolde openrouteservice

This command group will install the library to your global environment. Also works in virtual environments.


Testing
---------------------------------
If you want to run the unit tests, see Requirements_. ``cd`` to the library directory and run::

	nosetests -v

``-v`` flag for verbose output (recommended).


Usage
---------------------------------

For an interactive Jupyter notebook have a look on `mybinder.org <https://mybinder.org/v2/gh/GIScience/openrouteservice-py/master?filepath=examples%2Fbasic_example.ipynb>`_.

Basic example
^^^^^^^^^^^^^^^^^^^^
.. code:: python

	import openrouteservice

	coords = ((8.34234,48.23424),(8.34423,48.26424))

	client = openrouteservice.Client(key='') # Specify your personal API key
	routes = client.directions(coords)

	print(routes)

For convenience, all request performing module methods are wrapped inside the ``client`` class. This has the
disadvantage, that your IDE can't auto-show all positional and optional arguments for the
different methods. And there are a lot!

The slightly more verbose alternative, preserving your IDE's smart functions, is

.. code:: python

    import openrouteservice
    from openrouteservice.directions import directions

	coords = ((8.34234,48.23424),(8.34423,48.26424))

	client = openrouteservice.Client(key='') # Specify your personal API key
	routes = directions(client, coords) # Now it shows you all arguments for .directions

Optimize route
^^^^^^^^^^^^^^^^^^^^^^^^^^
If you want to optimize the order of multiple waypoints in a simple `Traveling Salesman Problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_,
you can pass a ``optimize_waypoints`` parameter:

.. code:: python

	import openrouteservice

	coords = ((8.34234,48.23424),(8.34423,48.26424), (8.34523,48.24424), (8.41423,48.21424))

	client = openrouteservice.Client(key='') # Specify your personal API key
	routes = client.directions(coords, profile='cycling-regular', optimize_waypoints=True)

	print(routes)

Decode Polyline
^^^^^^^^^^^^^^^^^^^^^^^^^^
By default, the directions API returns `encoded polylines <https://developers.google.com/maps/documentation/utilities/polylinealgorithm>`_.
To decode to a ``dict``, which is a GeoJSON geometry object, simply do

.. code:: python

    import openrouteservice
    from openrouteservice import convert

    coords = ((8.34234,48.23424),(8.34423,48.26424))

    client = openrouteservice.Client(key='') # Specify your personal API key

    # decode_polyline needs the geometry only
    geometry = client.directions(coords)['routes'][0]['geometry']

    decoded = convert.decode_polyline(geometry)

    print(decoded)

Dry run
^^^^^^^^^^^^^^^^^^^^
Although errors in query creation should be handled quite decently, you can do a dry run to print the request and its parameters:

.. code:: python

    import openrouteservice

    coords = ((8.34234,48.23424),(8.34423,48.26424))

    client = openrouteservice.Client()
    client.directions(coords, dry_run='true')

Local ORS instance
^^^^^^^^^^^^^^^^^^^^
If you're hosting your own ORS instance, you can alter the ``base_url`` parameter to fit your own:

.. code:: python

    import openrouteservice

    coords = ((8.34234,48.23424),(8.34423,48.26424))

    # key can be omitted for local host
    client = openrouteservice.Client(base_url='http://localhost/ors')

    # Only works if you didn't change the ORS endpoints manually
    routes = client.directions(coords)

    # If you did change the ORS endpoints for some reason
    # you'll have to pass url and required parameters explicitly:
    routes = client.request(
      url='/new_url',
      post_json={
          'coordinates': coords,
          'profile': 'driving-car',
          'format': 'geojson'
      })

Support
--------

For general support and questions, contact our forum_.

For issues/bugs/enhancement suggestions, please use https://github.com/GIScience/openrouteservice-py/issues.


.. _forum: https://ask.openrouteservice.org/c/sdks


Acknowledgements
-----------------

This library is based on the very elegant codebase from googlemaps_.


.. _googlemaps: https://github.com/googlemaps/google-maps-services-python
