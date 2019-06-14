# -*- coding: utf-8 -*-
import sys
import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info <= (2, 6):
    error = 'Requires Python Version 2.7 or above... exiting.'
    print(sys.stderr, error)
    sys.exit(1)

here = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(here, 'README.rst')) as f:
        return f.read()


setup(
    name='openrouteservice',
    version='2.2.2',
    description='Python client for requests to openrouteservice API services',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    keywords='routing accessibility router OSM ORS openrouteservice openstreetmap isochrone POI elevation DEM',
    url='https://github.com/GIScience/openrouteservice-py',
    author='Nils Nolde',
    author_email='nils.nolde@gmail.com',
    license='Apache-2.0',
    packages=['openrouteservice'],
    install_requires=[
        'requests>=2.0'],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose>1.0',
                   'requests>=2.0',
                   'responses>=0.10',
                   'coveralls>=1.7.0',
                   'coverage>=4.5.0'],
    zip_safe=False
)
