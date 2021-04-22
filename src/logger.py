import logging

LOG_FORMAT = "%(asctime)s %(levelname)-8s %(message)s"


def setup_logging():
    logging.basicConfig(format=LOG_FORMAT,
                        level=logging.DEBUG)
