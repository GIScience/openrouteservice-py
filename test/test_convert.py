# Copyright 2014 Google Inc. All rights reserved.
#
# Modifications Copyright (C) 2018 HeiGIT, University of Heidelberg.
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

"""Tests for the convert module."""

import unittest

from openrouteservice import convert


class ConvertTest(unittest.TestCase):

    def test_single_coord_tuple(self):
        expected = "1,2"
        ll = (1, 2)
        self.assertEqual(expected, convert._build_coords(ll))

        ll = [1, 2]
        self.assertEqual(expected, convert._build_coords(ll))

        with self.assertRaises(TypeError):
            convert._build_coords(1)

        with self.assertRaises(TypeError):
            convert._build_coords({'lat':1, 'lon':2})
            

        with self.assertRaises(TypeError):
            convert._build_coords('1,2')
            
            
    def test_multi_coord_tuple(self):
        expected = "1,2|3,4"

        ll = ((1,2),(3,4))
        self.assertEqual(expected, convert._build_coords(ll))

        ll = [(1,2),(3,4)]
        self.assertEqual(expected, convert._build_coords(ll))
        
        ll = ([1,2],[3,4])
        self.assertEqual(expected, convert._build_coords(ll))
        
        ll = [[1,2],[3,4]]
        self.assertEqual(expected, convert._build_coords(ll))
        
        with self.assertRaises(TypeError):
            convert._build_coords({{'lat':1, 'lon':2},{'lat':3, 'lon':4}})
            

        with self.assertRaises(TypeError):
            convert._build_coords('[1,2],[3,4]')
            
    def test_polyline_decode(self):
        syd_mel_route = (r"mtkeHuv|q@~@VLHz@\PR|@hBt@j@^n@L\NjALv@Jh@NXi@zBm@jC"
                         "KTy@z@qAhBa@\[Ne@DgCc@i@?[Ty@hAi@zASRi@R}@H_@N[b@kAd"
                         "Cy@`Au@d@eA|@q@h@WRe@PYHYBqADgAAcAL_A^w@~@q@`@w@Zw@C"
                         "m@K[PeA|Aa@p@g@fAiAhBuAv@]VU^k@xAUXe@TqATy@V}@f@_@VO"
                         "\Mb@[fBe@|@Mp@WbCgClKSdAq@Rm@?g@WYg@G[[}Bk@qBy@wDUm@"
                         "w@}@q@}A]o@k@y@kAjC_AjC_ApCe@z@i@j@q@f@[NsAp@u@T}A\w"
                         "ATU?WCeBm@q@MwAGUCg@SMaAi@mDQm@K}@Mq@u@mAc@i@c@Ys@[W"
                         "W_@q@e@a@cA_@w@E{BHmBXqBkBsA}@{Ao@iAB{@QYSi@qCUy@Ee@"
                         "@SDWbA_BLKLAVNb@r@J@HEHK?]k@iDe@w@COAWBUh@qBDc@?c@Q{"
                         "BGa@MQKCOBgA\{@AKEs@Wq@i@q@{@s@gAk@kA]g@g@_@I]??k@i@"
                         "yBkEa@}@W}@WkCUqC?_@Hg@ZqABg@Gm@YoAEgAMq@@jAB|CC`@{@rACH")

        points = convert.decode_polyline(syd_mel_route)['coordinates']
        self.assertAlmostEqual(8.344268, points[0][0], places=5)
        self.assertAlmostEqual(48.233826, points[0][1], places=5)
        self.assertAlmostEqual(8.343433, points[-1][0], places=5)
        self.assertAlmostEqual(48.263552, points[-1][1], places=5)
