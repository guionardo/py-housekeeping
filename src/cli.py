""" CLI usage

# With configuration file: Just
"""
import sys
import json
import logging
from exceptions import JustExitException
import tempfile


def get_arguments(args=sys.argv[1:]):
    parsed_args = ParsedArguments([
        ArgumentOption('help', 'Help', default=False, default_option=True),
        ArgumentOption(
            'config-file', 'Configuration File', default=None),
        ArgumentOption(
            'folder', 'Source folder', default=None),
        ArgumentOption(
            'max-count', 'Maximum file count in folder', default=0),
        ArgumentOption(
            'max-size', 'Maximum folder size', default=0),
        ArgumentOption(
            'max-age', 'Maximum file age', default=0),
        ArgumentOption(
            'action', 'Action [delete, move, compress]', default=None),
        ArgumentOption(
            'destiny', 'Action destiny folder', default=None)
    ], args)

    # "folder": "./fakes/f1",
    # "rules": {
    #     "max_file_count": 100,
    #     "max_folder_size": 1024000,
    #     "max_file_age": "1m"
    # },
    # "action": "delete",
    # "action_destiny": "./bkp"
    # parsed_args = parse_arguments(args)

    if parsed_args.config_file:
        return parsed_args.config_file, None

    if parsed_args.help:
        raise JustExitException('\n'.join(parsed_args.show_help()))

    configuration = [{
        'folder': parsed_args.folder,
        'rules': {
            'max_file_count': int(parsed_args.max_count),
            'max_folder_size': int(parsed_args.max_size),
            'max_file_age': parsed_args.max_age
        },
        'action': parsed_args.action,
        'action_destiny': parsed_args.destiny
    }]
    f = tempfile.NamedTemporaryFile(mode='w')
    f.write(json.dumps(configuration))
    f.flush()
    return f.name, f


class ArgumentOption:
    _slots_ = ['name', 'description', 'optional', 'value', 'set', 'default', 'default_option']

    def __init__(self, name, description=None, optional=True, default=True, default_option=False):
        self.name = name
        self.description = str(description or '')
        self.optional = bool(optional)
        self.default = default
        self.value = default
        self.set = False
        self.default_option = default_option
        if not name:
            raise ValueError("ArgumentOption 'name' must be informed")

    def __str__(self):
        fmt = '[--{0} VALUE] {1} (default={2})' if self.optional else '--{0} VALUE {1} (default={2})'
        return fmt.format(self.name, self.description, self.default)

    def __repr__(self):
        return str({'name': self.name,
                    'description': self.description,
                    'optional': self.optional,
                    'value': self.value,
                    'default': self.default})


class ParsedArguments:
    __slots__ = ['_options']
    LOG = logging.getLogger(__name__)

    def __init__(self, options, args=sys.argv[1:]):
        """
        args = list of string arguments
        options = list of ArgumentOption
        """
        self._options = {option.name: option for option in options}
        key = None
        value = None
        opts = {}
        for arg in args:
            if arg.startswith('--'):  # key
                key = arg[2:]
                opts[key] = opts.get(key, True)
            elif key:  # value for key
                opts[key] = arg
                key = None
            else:  # value without key
                raise ValueError("Argument without previous key", value)

        unknown_options = []
        for key in opts.keys():
            if key in self._options.keys():
                self._options[key].value = opts[key]
                self._options[key].set = True
            else:
                unknown_options.append("--{0}={1}".format(key, opts[key]))

        missing = []
        options_count = 0
        default_option = None
        for key in self._options.keys():
            if self._options[key].default_option:
                default_option = self._options[key]
            if self._options[key].set:
                options_count += 1
            elif not self._options[key].optional:
                missing.append("--{0}".format(key))

        if unknown_options:
            self.LOG.warn('Unknown options (ignored): %s', unknown_options)

        if missing:
            raise ValueError("Missing mandatory options: %s", missing)

        if options_count == 0:
            default_option.value = True

    def __getattr__(self, name):
        if name in self._options.keys():
            return self._options[name].value
        name = name.replace('_', '-')
        if name in self._options.keys():
            return self._options[name].value

    def show_help(self):
        help = []
        if not self._options:
            help.append('No options defined')
        else:
            help.append('Options:')
            for option in self._options:
                help.append(str(self._options[option]))
        return help


def parse_arguments(args=sys.argv[1:]):
    key = None
    value = None
    parsed = {'_': []}
    for arg in args:
        if arg.startswith('--'):
            if key:
                parsed[key] = True
            key = arg[2:]
        else:
            value = arg
        if not value:
            continue
        if key:
            parsed[key] = value
            key = None
        else:
            parsed['_'].append(value)
        value = None

    return parsed
