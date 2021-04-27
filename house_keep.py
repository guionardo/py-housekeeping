# -*- coding: utf-8 -*-
import json
import logging
import os
import sys

from src.configuration import Configuration
from src.house_keeper import HouseKeeper
from src.logger import setup_logging
from src.exceptions import FileNotFoundError, JustExitException
from src.cli import get_arguments

setup_logging()

LOGGER = logging.getLogger(__name__)


def main(args=sys.argv[1:]):
    from src.singleton import Singleton
    singleton = None
    try:
        singleton = Singleton('.')

        config_file, file_handler = get_arguments(args)

        if not os.path.isfile(config_file):
            raise FileNotFoundError(config_file)

        configuration = Configuration(config_file)
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
        del singleton


if __name__ == '__main__':
    main()
