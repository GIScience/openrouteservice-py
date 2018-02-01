# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:50:14 2018

@author: gisadmin
"""

import openrouteservice


coords_valid = ((8.34234,48.23424),(8.34423,48.26424))
coords_invalid = ((1,2),(3,4))
key = '58d904a497c67e00015b45fcacecf32dfe6248f4bd208bc3dc37e113'
client = openrouteservice.Client(key)
#
#routes = client.directions(coords_valid)
#routes2=client.directions(coords_valid, instructions='false', geometry_format='geojson')
#geometry = routes2['routes'][0]['geometry']
#
#

"""Matrix"""
coords_valid = [[9.970093,48.477473],
                [9.207916,49.153868],
                [37.573242,55.801281],
                [115.663757,38.106467]]

routes = client.distance_matrix(locations=coords_valid)

print routes


"""Isochrones"""

#isochrones = client.isochrones(coords_valid)
#
#print isochrones 