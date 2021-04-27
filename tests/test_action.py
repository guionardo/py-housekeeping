# -*- coding: utf-8 -*-
import os
import unittest

from src.action import Action

from utils import remove_dir


class TestAction(unittest.TestCase):

    TEST_PATH = './test_path'

    @classmethod
    def setUpClass(cls):
        remove_dir(cls.TEST_PATH)

    @classmethod
    def tearDownClass(cls):
        remove_dir(cls.TEST_PATH)

    def test_invalid_action_config(self):
        with self.assertRaises(ValueError):
            _ = Action({'action': 'error'})

    def test_valid_action_config(self):
        action = Action({'action': 'delete',
                        'action_destiny': '.'})
        self.assertIsInstance(str(action), str)
        action = Action({'action': 'move',
                        'action_destiny': '.'})
        self.assertIsInstance(str(action), str)
        self.assertIsInstance(action.to_dict(), dict)

    def test_invalid_destiny(self):
        with self.assertRaises(ValueError):
            _ = Action({'action': 'move',
                       'action_destiny': ''})

    def test_create_destiny(self):
        _ = Action({'action': 'move',
                    'action_destiny': self.TEST_PATH})
        self.assertTrue(os.path.isdir(self.TEST_PATH))
