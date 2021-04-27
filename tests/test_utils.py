import os
import shutil
import unittest

from src.utils import make_dirs


class TestUtils(unittest.TestCase):

    TEST_FOLDER = os.path.abspath('./test_folder')

    def setUp(self):
        self.clear_dirs()

    def tearDown(self):
        self.clear_dirs()

    def clear_dirs(self):
        if os.path.isdir(self.TEST_FOLDER):
            shutil.rmtree(self.TEST_FOLDER)

    def test_make_dirs(self):
        result = make_dirs(self.TEST_FOLDER)
        self.assertTrue(result)
