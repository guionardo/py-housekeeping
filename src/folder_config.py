import os

from action import Action
from rule import Rule


class FolderConfig:

    def __init__(self, config):
        if not isinstance(config, dict):
            raise ValueError('Invalid Folder configuration (dict expected)')
        self.folder = config.get('folder', '')
        if not os.path.isdir(self.folder):
            raise ValueError(
                'Invalid Folder configuration (folder not found)', self.folder)
        self.folder = os.path.realpath(self.folder)
        self.rules = Rule(config.get('rules', {}))
        self.action = Action(config)
        self.description = config.get('description', '')

    def __str__(self):
        return "{0}: {1} : {2}{3}".format(
            self.folder,
            str(self.rules),
            str(self.action),
            (' ['+self.description+']') if self.description else ''
        )

    @staticmethod
    def to_dict():
        d = {
            "description": "",
            "folder": "",
            "rules": [Rule.to_dict()]
        }
        d.update(Action.to_dict())
        return d
