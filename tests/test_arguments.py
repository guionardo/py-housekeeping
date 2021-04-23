import unittest

from src.house_keep import get_arguments


class TestArguments(unittest.TestCase):

    def test_valid_arguments_returns_success(self):
        argv = ['some_file']
        args = get_arguments(argv)
        self.assertEquals('some_file', args[0])

    def test_missing_arguments_throws_typeerror(self):
        argv = []
        with self.assertRaises(TypeError):
            get_arguments(argv)
