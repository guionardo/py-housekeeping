import os


class Action:

    ACTIONS = ['delete', 'move', 'compress']

    def __init__(self, config):
        self.action = config.get('action', 'delete').lower()
        if self.action not in self.ACTIONS:
            raise ValueError("Action must be " +
                             str(self.ACTIONS)+": "+str(self.action))
        if self.action == 'delete':
            self.action_destiny = None
        else:
            self.action_destiny = config.get('action_destiny', None)
            if not self.action_destiny:
                raise ValueError("Action destiny for '" +
                                 self.action+"' must be defined")
            self.action_destiny = os.path.realpath(self.action_destiny)
            if not os.path.isdir(self.action_destiny):
                os.makedirs(self.action_destiny)

    def __str__(self):
        action = {'action': self.action}
        if self.action_destiny:
            action['action_destiny'] = self.action_destiny
        return str(action)

    @staticmethod
    def to_dict():
        return {
            "action": 'delete',
            "action_destiny": ''
        }
