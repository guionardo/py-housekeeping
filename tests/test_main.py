import unittest
from house_keep import main
from src.utils import make_dirs
from .generate import generate, clear_folder, folder_count, remove_folder, generate_aged


class TestMain(unittest.TestCase):
    FOLDER = './fakes_main'

    def test_main(self):
        make_dirs(self.FOLDER)
        clear_folder(self.FOLDER)
        generate(self.FOLDER, 20)
        file_count = folder_count(self.FOLDER)

        main(['--folder', self.FOLDER, '--max-count', '10', '--action', 'delete'])
        new_file_count = folder_count(self.FOLDER)
        self.assertEqual(10, new_file_count)
        remove_folder(self.FOLDER)

    def test_main_by_age(self):
        remove_folder(self.FOLDER)
        make_dirs(self.FOLDER)
        generate_aged(self.FOLDER, 100, age_in_minutes=5, percent_aged=0.5)
        file_count = folder_count(self.FOLDER)
        main(['--folder', self.FOLDER, '--max-age', '1m', '--action', 'delete'])
        new_file_count = folder_count(self.FOLDER)
        self.assertEqual(file_count / 2, new_file_count)
        remove_folder(self.FOLDER)
