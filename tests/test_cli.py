import logging
import os
import unittest

from src.cli import ArgumentOption, ParsedArguments, get_arguments
from src.exceptions import JustExitException


class TestCli(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(format="%(message)s")

    def test_get_arguments_valid(self):
        file_name, handler = get_arguments(['--config-file', 'any_data'])
        self.assertEqual('any_data', file_name)

    def test_get_arguments_empty_help(self):
        with self.assertRaises(JustExitException):
            get_arguments([])

    def test_argument_option_valid(self):
        option = ArgumentOption('test', 'Test argument', True)
        self.assertIsInstance(option, ArgumentOption)

    def test_parsed_arguments(self):
        parsed = ParsedArguments([ArgumentOption('test', 'Test argument'),
                                  ArgumentOption('file', 'File name', True)],
                                 ['--test', 'file.json', '--file', 'another'])

        self.assertEqual('file.json', parsed.test)
        self.assertEqual('another', parsed.file)
        print(parsed.show_help())

    def test_cli(self):
        (filename, handler) = get_arguments(
            ['--folder', './fakes', '--max-count', '10', '--action', 'delete'])
        self.assertTrue(os.path.isfile(filename))
        del handler
        self.assertFalse(os.path.isfile(filename))
