import datetime

from file_age import parse_file_age


class Rule:
    def __init__(self, rule):
        self.max_file_count = rule.get('max_file_count', 0)
        self.max_folder_size = rule.get('max_folder_size', 0)
        self.max_file_age = parse_file_age(rule.get('max_file_age', 0))

        if not isinstance(self.max_file_count, int):
            raise ValueError('Invalid max_file_count rule: ' +
                             str(self.max_file_count))
        if not isinstance(self.max_folder_size, int):
            raise ValueError('Invalid max_folder_size rule: ' +
                             str(self.max_folder_size))
        if self.max_file_count <= 0 and \
            self.max_folder_size <= 0 and \
                self.max_file_age.seconds <= 0:
            raise ValueError('Invalid rule: no restrictions are defined')

    def __str__(self):
        rules = {}
        if self.max_file_count > 0:
            rules['max_file_count'] = self.max_file_count
        if self.max_folder_size > 0:
            rules['max_folder_size'] = self.max_folder_size
        if self.max_file_age.seconds > 0 or self.max_file_age.days > 0:
            rules['max_file_age'] = str(
                datetime.datetime.now()-self.max_file_age)
        return str(rules)

    @staticmethod
    def to_dict():
        return {
            'max_file_count': 0,
            'max_folder_size': 0,
            'max_file_age': 0
        }
