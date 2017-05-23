try:
    import unittest2 as unittest
except ImportError:
    import unittest

from subscription_manager.i18n import configure_i18n


class TestI18N(unittest.TestCase):
    def test_configure_i18n(self):
        configure_i18n()
