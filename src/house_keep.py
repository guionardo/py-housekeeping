# -*- coding: utf-8 -*-
import json
import logging
import os
import sys

from configuration import Configuration
from house_keeper import HouseKeeper
from logger import setup_logging
from exceptions import FileNotFoundError

setup_logging()


LOGGER = logging.getLogger(__name__)


def get_arguments(args=sys.argv[1:]):
    if not args:
        raise TypeError("Usage: {0} SETUP_FILE".format(
            os.path.basename(sys.argv[0])))

    return args


def main():
    from singleton import JustExitException, Singleton
    singleton = None
    try:
        singleton = Singleton('.')
        arguments = get_arguments()
        if not os.path.isfile(arguments[0]):
            raise FileNotFoundError(arguments[0])
        configuration = Configuration(arguments[0])
        house_keeper = HouseKeeper(configuration)
        house_keeper.run()
    except JustExitException as exc:
        LOGGER.warn("%s", exc)
    except Exception as exc:
        LOGGER.error("Init error: %s", exc)
        if 'JUST EXIT' not in exc.args:
            LOGGER.info("Configuration data expected: \n%s",
                        json.dumps(Configuration.to_dict(), indent=2))

    finally:
        del(singleton)


if __name__ == '__main__':
    main()
