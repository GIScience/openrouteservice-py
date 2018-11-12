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
      version='1.1.2',
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
              'requests==2.19.1',
              'Cerberus==1.2',
              'certifi==2018.8.24',
              'chardet==3.0.4',
              'cookies==2.2.1',
              'idna==2.7',
              'six==1.11.0',
              'urllib3==1.23'],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose==1.3.7',
                     'responses==0.9.0',
                     'mock==1.23'],
      zip_safe=False)
