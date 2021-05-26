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

"""Initialize openrouteservice."""
import pkg_resources

__version__ = pkg_resources.get_distribution("openrouteservice").version


def get_ordinal(number):
    """Produces an ordinal (1st, 2nd, 3rd, 4th) from a number."""

    if number == 1:
        return "st"
    elif number == 2:
        return "nd"
    elif number == 3:
        return "rd"
    else:
        return "th"


from openrouteservice.client import Client  # noqa
