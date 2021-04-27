import logging
import os
import time

from exceptions import JustExitException


class Singleton:

    LOG = logging.getLogger(__name__)
    MINIMUM_INTERVAL = 120

    def __init__(self, folder):
        self.control_file = os.path.realpath(
            os.path.join(folder, 'HOUSE_KEEP.CTRL'))
        if os.path.isfile(self.control_file):
            try:
                with open(self.control_file) as f:
                    create_time = float(f.read())
                    if time.time()-create_time < self.MINIMUM_INTERVAL:
                        self.control_file = ''
                        raise JustExitException('Control file detected, created in {0}. Can run after {1}'.format(
                            self.fmt_time(create_time),
                            self.fmt_time(create_time+self.MINIMUM_INTERVAL)))
            except OSError as exc:
                self.LOG.error('Reading control file error: %s', exc)
                raise
            except ValueError as exc:
                self.LOG.error('Corrupted control file: %s', exc)
                os.unlink(self.control_file)

        create_time = time.time()
        with open(self.control_file, 'w') as f:
            f.write(str(create_time))
        self.LOG.debug('CREATING CONTROL FILE %s = %s',
                       self.control_file, self.fmt_time(create_time))

    @staticmethod
    def fmt_time(create_time):
        return time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(create_time))

    def __del__(self):
        if os.path.isfile(self.control_file):
            self.LOG.debug('REMOVING CONTROL FILE %s', self.control_file)
            os.unlink(self.control_file)
