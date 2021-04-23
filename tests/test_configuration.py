import unittest

from src.exceptions import FileNotFoundError
from src.configuration import Configuration
from src.utils import make_dirs, remove_dir


class TestConfiguration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        remove_dir('./fakes/f1')
        remove_dir('./fakes/f2')
        remove_dir('./fakes/f3')

    @classmethod
    def tearDownClass(cls):
        remove_dir('./fakes/f1')
        remove_dir('./fakes/f2')
        remove_dir('./fakes/f3')

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            _ = Configuration('unexistent_file.json')

    def test_valid_file(self):
        make_dirs('./fakes/f1')
        make_dirs('./fakes/f2')
        make_dirs('./fakes/f3')
        configuration = Configuration('tests/fixtures/configuration.json')
        self.assertIsInstance(configuration, Configuration)
        self.assertIsInstance(configuration.to_dict(), list)
        self.assertIsInstance(configuration.configs, list)

    def test_invalid_file(self):
        with self.assertRaises(ValueError):
            _ = Configuration('tests/fixtures/configuration_invalid.json')
