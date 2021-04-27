import os
import shutil


def remove_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
