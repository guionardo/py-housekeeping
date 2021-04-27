import unittest
from src.singleton import Singleton, JustExitException


class TestSingleton(unittest.TestCase):

    def test_create_singleton(self):
        Singleton.MINIMUM_INTERVAL = 120
        singleton = Singleton('.')
        with self.assertRaises(JustExitException):
            _ = Singleton('.')
        del(singleton)

    def test_corrupted_file(self):
        with open('./HOUSE_KEEP.CTRL', 'w') as f:
            f.write('error')
        singleton = Singleton('.')
        del(singleton)
