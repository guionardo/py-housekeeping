import unittest
from datetime import timedelta
from src.file_age import parse_file_age, is_aged_file


class TestFileAge(unittest.TestCase):

    def test_file_age_default(self):
        self.assertEqual(0, parse_file_age(None).seconds)

    def test_file_age_timedelta(self):
        self.assertEqual(5, parse_file_age(timedelta(seconds=5)).seconds)

    def test_file_age_int(self):
        self.assertEqual(5, parse_file_age(5).seconds)

    def test_file_age_seconds(self):
        self.assertEqual(5, parse_file_age('5s').seconds)

    def test_file_age_minutes(self):
        self.assertEqual(60, parse_file_age('1m').seconds)

    def test_file_age_hours(self):
        self.assertEqual(3600, parse_file_age('1h').seconds)

    def test_file_age_days(self):
        self.assertEqual(1, parse_file_age('1d').days)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            parse_file_age('1w')

    def test_is_aged_file(self):
        self.assertTrue(is_aged_file(0, 5))
