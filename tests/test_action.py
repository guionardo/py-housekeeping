# -*- coding: utf-8 -*-
import unittest

from src.action import Action


class TestAction(unittest.TestCase):

    def test_invalid_action_config(self):
        with self.assertRaises(ValueError):
            _ = Action({'action': 'error'})

    def test_valid_action_config(self):
        action = Action({'action': 'delete',
                        'action_destiny': '.'})
        self.assertIsInstance(str(action), str)
        action = Action({'action': 'move',
                        'action_destiny': '.'})
