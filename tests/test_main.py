import unittest

from house_keep import main
from src.utils import make_dirs

from .generate import folder_count, generate, generate_aged, remove_folder


class TestMain(unittest.TestCase):
    FOLDER = './fakes_main'
    DESTINY = './fakes_destiny'

    def setUp(self):
        remove_folder(self.FOLDER)
        make_dirs(self.FOLDER)
        remove_folder(self.DESTINY)
        make_dirs(self.DESTINY)

    def tearDown(self):
        remove_folder(self.FOLDER)
        remove_folder(self.DESTINY)

    def test_main(self):
        generate(self.FOLDER, 20)
        file_count = folder_count(self.FOLDER)
        self.assertEqual(20, file_count)

        main(['--folder', self.FOLDER, '--max-count', '10', '--action', 'delete'])
        new_file_count = folder_count(self.FOLDER)
        self.assertEqual(10, new_file_count)

    def test_main_by_age(self):
        generate_aged(self.FOLDER, 1000, age_in_minutes=5, percent_aged=0.5)
        file_count = folder_count(self.FOLDER)
        self.assertEqual(1000, file_count)
        main(['--folder', self.FOLDER, '--max-age', '1m', '--action', 'delete'])
        new_file_count = folder_count(self.FOLDER)
        self.assertEqual(file_count / 2, new_file_count)

    def test_main_compress(self):
        generate(self.FOLDER, 1000)
        file_count = folder_count(self.FOLDER)
        self.assertEqual(1000, file_count)
        main(['--folder', self.FOLDER, '--max-count', '1',
             '--action', 'compress', '--destiny', self.DESTINY])
        new_file_count = folder_count(self.FOLDER)
        self.assertEqual(1, new_file_count)
        destiny_file_count = folder_count(self.DESTINY)
        self.assertEqual(1, destiny_file_count)
