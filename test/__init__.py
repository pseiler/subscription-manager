from __future__ import print_function, division, absolute_import

import os
import pytest

from subscription_manager import ga_loader
ga_loader.init_ga()
import six
from . import rhsm_display
rhsm_display.set_display()

if six.PY2:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')


get_decorator = lambda cond: pytest.mark.skipif(
    not os.environ.get(cond),
    reason=f"{cond} is not set.",
)
get_skip_decorator = lambda cond: pytest.mark.skipif(
    os.environ.get(cond),
    reason=f"{cond} is set."
)

subman_test_functional = get_decorator("SUBMAN_TEST_FUNCTIONAL")
subman_test_zypper = get_decorator("SUBMAN_TEST_ZYPPER")
subman_test_skip_dbus = get_skip_decorator("SUBMAN_TEST_SKIP_DBUS")
subman_test_py2 = pytest.mark.skipif(not six.PY2, reason="This test requires Python 2.")
