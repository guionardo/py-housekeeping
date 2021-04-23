import unittest
from src.rule import Rule


class TestRule(unittest.TestCase):

    def test_valid_rule(self):
        rule = Rule({
            'max_file_count': 100,
            'max_folder_size': 1024,
            'max_file_age': 60,
        })
        self.assertIsInstance(rule, Rule)
        self.assertIsInstance(str(rule), str)

    def test_invalid_rule(self):
        with self.assertRaises(ValueError):
            _ = Rule({
                    'max_file_count': "A",
                    'max_folder_size': 1024,
                    'max_file_age': 60,
                })
        with self.assertRaises(ValueError):
            _ = Rule({
                    'max_file_count': 100,
                    'max_folder_size': "A",
                    'max_file_age': 60,
                })
        with self.assertRaises(ValueError):
            _ = Rule({
                        'max_file_count': 0,
                        'max_folder_size': 0,
                        'max_file_age': 0,
                    })
