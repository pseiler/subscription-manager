from __future__ import print_function, division, absolute_import


import six
from . import rhsm_display
rhsm_display.set_display()

if six.PY2:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

import pytest

subman_marker_dbus = pytest.mark.dbus
subman_marker_functional = pytest.mark.functional
subman_marker_zypper = pytest.mark.zypper
subman_marker_slow = pytest.mark.slow
# This allows us to set higher timeout limit for tests that are known to be slow
subman_marker_slow_timeout = pytest.mark.timeout(40)
