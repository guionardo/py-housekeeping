import shutil
import os


def remove_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
