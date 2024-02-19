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

"""Prints a deprecation warning."""

import warnings


def warning(old_name, new_name):
    """Deprecation warning."""

    warnings.warn(
        "{} will be deprecated in v2.0. Please use {} instead".format(
            old_name, new_name
        ),
        DeprecationWarning,
        stacklevel=2,
    )

def deprecated(old_name, new_name):
    """Deprecation warning."""

    warnings.warn(
        "{} is deprecated. Please use {} instead. For more information on the new SDK please check out https://github.com/GIScience/openrouteservice-py".format(
            old_name, new_name
        ),
        DeprecationWarning,
        stacklevel=2,
    )