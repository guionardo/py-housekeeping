import logging
import os
import shutil

from exceptions import FileNotFoundError

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


def remove_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
