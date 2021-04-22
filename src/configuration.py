# -*- coding: utf-8 -*-
import json
import os
import logging

from folder_config import FolderConfig


class Configuration:

    LOG = logging.getLogger(__name__)

    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)

        with open(filename) as f:
            configs = json.loads(f.read())

        if not isinstance(configs, list):
            raise ValueError('Invalid JSON configuration (list expected)')

        self._configs = [FolderConfig(config) for config in configs]
        self.LOG.info('Configuration')
        for config in self._configs:
            self.LOG.info(str(config))

    @staticmethod
    def to_dict():
        return [FolderConfig.to_dict()]

    @property
    def configs(self):
        return self._configs
