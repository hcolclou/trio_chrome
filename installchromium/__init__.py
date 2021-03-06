#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Meta data"""

import os

from appdirs import AppDirs

__chromium_revision__ = '588429'
__installchromium_home__ = os.environ.get(
    'INSTALL_CHROMIUM_HOME', AppDirs('installchromium').user_data_dir)  # type: str