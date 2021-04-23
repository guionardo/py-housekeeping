# -*- coding: utf-8 -*-
import unittest

from src.action import Action


class TestAction(unittest.TestCase):

    def test_invalid_action_config(self):
        with self.assertRaises(ValueError):
            _ = Action({'action': 'error'})
