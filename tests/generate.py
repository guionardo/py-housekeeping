import datetime
import os
import random
import shutil
import uuid


def mkdir(folder):
    if os.path.isdir(folder):
        return True

    os.makedirs(folder)


def generate(folder, count):
    for i in range(count):
        size = random.choice([1024, 5120, 102400])
        filename = os.path.join(
            folder, '{0:0>6d}_{1}'.format(i, uuid.uuid1()))
        with open(filename, 'w') as f:
            f.write('0' * size)


def folder_count(folder_name):
    for _, _, files in os.walk(folder_name):
        return len(files)


def clear_folder(folder_name):
    for root, _, files in os.walk(folder_name):
        for file_ in files:
            file_name = os.path.join(root, file_)
            os.unlink(file_name)


def remove_folder(folder_name):
    if not os.path.isdir(folder_name):
        return
    clear_folder(folder_name)
    shutil.rmtree(folder_name)


def generate_aged(folder_name, count, age_in_minutes, percent_aged):
    for i in range(count):
        size = random.choice([1024, 5120, 102400])
        filename = os.path.join(
            folder_name, '{0:0>6d}_{1}'.format(i, uuid.uuid1()))
        with open(filename, 'w') as f:
            f.write('0' * size)
        if (float(i+1) / float(count)) <= percent_aged:
            continue
        new_age = (datetime.datetime.now() -
                   datetime.timedelta(minutes=age_in_minutes)).strftime('%m%d%H%M')
        os.system('touch -c -t {0} {1}'.format(new_age, filename))

# folders = ['./fakes/f1', './fakes/f2', './fakes/f3']
# mkdir('./fakes/bkp')
# for folder in folders:
#     mkdir(folder)
#     generate(folder, 10000)
