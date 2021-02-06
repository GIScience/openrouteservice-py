import unittest
import codecs
import openrouteservice

from urllib.parse import urlparse, parse_qsl

# For relative imports to work in Python 3.6
import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.key = "sample_key"
        self.client = openrouteservice.Client(self.key)

    def assertURLEqual(self, first, second, msg=None):
        """Check that two arguments are equivalent URLs. Ignores the order of
        query arguments.
        """
        first_parsed = urlparse(first)
        second_parsed = urlparse(second)
        self.assertEqual(first_parsed[:3], second_parsed[:3], msg)

        first_qsl = sorted(parse_qsl(first_parsed.query))
        second_qsl = sorted(parse_qsl(second_parsed.query))
        self.assertEqual(first_qsl, second_qsl, msg)

    @staticmethod
    def u(string):
        """Create a unicode string, compatible across all versions of Python."""
        # NOTE(cbro): Python 3-3.2 does not have the u'' syntax.
        return codecs.unicode_escape_decode(string)[0]

    def assertDictContainsSubset(self, a, b, **kwargs):
        """Replaces deprecated unittest.TestCase.assertDictContainsSubset"""
        c = dict([(k, b[k]) for k in a.keys() if k in b.keys()])
        self.assertEqual(a, c)


@pytest.fixture(scope="function")
def simpletestcase():
    test_case = TestCase()
    test_case.setUp()
    yield test_case
