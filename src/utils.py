import logging
import os

LOG = logging.getLogger(__name__)


def make_dirs(path):
    try:
        if os.path.isdir(path):
            return
        os.makedirs(path)
        if not os.path.isdir(path):
            raise FileNotFoundError()
        LOG.info('Directory created: %s', path)
        return True
    except FileNotFoundError:
        LOG.error('Failed to create directory: %s', path)
    except OSError as exc:
        LOG.error('Exception when creating directory: %s - %s', path, exc)
