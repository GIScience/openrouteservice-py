# -*- coding: utf-8 -*-
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

    def test_build_single_coord_tuple(self):
        expected = "1,2"
        ll = (1, 2)
        self.assertEqual(expected, convert._build_coords(ll))

        ll = [1, 2]
        self.assertEqual(expected, convert._build_coords(ll))

        with self.assertRaises(TypeError):
            convert._build_coords(1)

        with self.assertRaises(TypeError):
            convert._build_coords({'lat': 1, 'lon': 2})

        with self.assertRaises(TypeError):
            convert._build_coords('1,2')

    def test_build_multi_coord_tuple(self):
        expected = "1,2|3,4"

        ll = ((1, 2), (3, 4))
        self.assertEqual(expected, convert._build_coords(ll))

        ll = [(1, 2), (3, 4)]
        self.assertEqual(expected, convert._build_coords(ll))

        ll = ([1, 2], [3, 4])
        self.assertEqual(expected, convert._build_coords(ll))

        ll = [[1, 2], [3, 4]]
        self.assertEqual(expected, convert._build_coords(ll))

        with self.assertRaises(TypeError):
            convert._build_coords({{'lat': 1, 'lon': 2}, {'lat': 3, 'lon': 4}})

        with self.assertRaises(TypeError):
            convert._build_coords('[1,2],[3,4]')

    def test_convert_bool(self):
        self.assertEqual('true', convert._convert_bool('True'))
        self.assertEqual('true', convert._convert_bool('true'))
        self.assertEqual('true', convert._convert_bool(True))

    def test_polyline_decode_3d(self):
        syd_mel_route = (r"mlqlHat`t@OiACMvAs@HCPGJ?JAJBRFTRLJPNHDNDJ"
                         "@D?fACRAZCPAb@AF?HAfBQJEDAn@QFC@QD_@@QFe@Bg"
                         "@@KBy@?M@a@@q@?iE?C?OGgAkEwUQ{@c@gBQeAYeCIe"
                         "AWmDAIImACUOyBIeAC}@Ey@?QLC@_@@KBiAVmDF]Ni@"
                         "Zu@RYBA^_@~A{A`Ai@JCPGf@Qf@]X_@BMAMIKuBTI?G"
                         "E?A?ADOnCsB\c@DGDIl@sAJUFMBGJUP[DCD@DP@l@?R"
                         "?h@Bx@PnAAl@?BAFc@rAAB?@BRHBFEN[FQFQRg@Rw@J"
                         "g@Ny@DUDOJe@N_ADm@BkBGcC@s@Du@l@eEZgBP_AHe@"
                         "He@Fc@RuATaA?SCWAGIOQS[Qu@Ym@C}@R{@`@m@p@Wj"
                         "@]nAGBE?KGAE?E?KVcB`@eB^mAn@uALUJSj@y@fA}@f"
                         "@k@BGHM^k@r@qAHSLU^i@bA_Af@q@PYFKHIHCJ?RLFN"
                         "XjAj@tDj@rERzBLzCHp@xAdKLf@RXTDNEBCFGDEDE@G"
                         "@GDKBGRc@Xi@N[JUf@u@l@o@f@c@h@]XMfQ}D|EcAlA"
                         "ORIJQ?C?CAUKOSGwAMa@M_EsBcBqA_A{@k@q@sCcEi@"
                         "gAWo@[gAYyAMy@y@aNMyAc@uDS_As@uBMc@Ig@SeBKc"
                         "@Uy@AI@A]GGCMIiCmAGCWMqAk@")

        points = convert.decode_polyline(syd_mel_route, True)['coordinates']
        self.assertEqual(len(points[0]), 3)
        self.assertAlmostEqual(8.69201, points[0][0], places=5)
        self.assertAlmostEqual(49.410151, points[0][1], places=5)
        self.assertAlmostEqual(0.1, points[0][2], places=2)
        self.assertAlmostEqual(8.69917, points[-1][0], places=5)
        self.assertAlmostEqual(49.41868, points[-1][1], places=5)
        self.assertAlmostEqual(12.5, points[-1][2], places=2)

    def test_polyline_decode_2d(self):
        syd_mel_route = (r"u`rgFswjpAKD")

        points = convert.decode_polyline(syd_mel_route, False)['coordinates']
        self.assertEqual(len(points[0]), 2)
        self.assertAlmostEqual([13.3313, 38.10843], points[0], places=5)
        self.assertAlmostEqual([13.33127, 38.10849], points[1], places=5)

    def test_pipe_list_bad_argument(self):
        with self.assertRaises(TypeError):
            convert._pipe_list(5)

    def test_comma_list_bad_argument(self):
        with self.assertRaises(TypeError):
            convert._comma_list(5)
