import os
import random
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
            f.write('0'*size)


folders = ['./fakes/f1', './fakes/f2', './fakes/f3']
mkdir('./fakes/bkp')
for folder in folders:
    mkdir(folder)
    generate(folder, 10000)
