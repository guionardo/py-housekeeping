import unittest
import os
import shutil

from src.utils import make_dirs


class TestUtils(unittest.TestCase):

    TEST_FOLDER = os.path.abspath('./test_folder')

    def setUp(self) -> None:
        self.clear_dirs()
        return super().setUp()

    def clear_dirs(self):
        if os.path.isdir(self.TEST_FOLDER):
            shutil.rmtree(self.TEST_FOLDER)

    def test_make_dirs(self):
        result = make_dirs(self.TEST_FOLDER)
        self.assertTrue(result)
