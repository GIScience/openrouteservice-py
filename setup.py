# -*- coding: utf-8 -*-
import sys


try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()
  
if sys.version_info <= (2, 6):
  error = 'Requires Python Version 2.7 or above... exiting.'
  print >> sys.stderr, error
  sys.exit(1)

setup(name='openrouteservice',
      version='0.2',
      description='Python client for requests to openrouteservice API services',
      long_description=readme(),
      classifiers=[
              'Development Status :: 4 - Beta',
              'License :: OSI Approved :: Apache Software License',
              'Operating System :: OS Independent',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              ],
      keywords='routing accessibility router OSM ORS openrouteservice openstreetmap isochrone POI',
      url='https://github.com/GIScience/openrouteservice-py',
      author='Nils Nolde',
      author_email='nils.nolde@gmail.com',
      license='Apache-2.0',
      packages=['openrouteservice'],
      install_requires = [
              'requests',],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose',
                     'responses',
                     'mock'],
      zip_safe=False)