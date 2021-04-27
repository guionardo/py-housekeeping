try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

class JustExitException(Exception):
    pass