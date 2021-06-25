#!/usr/bin/env python3.9

from random import randbytes
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--size_in_mb', type=int, default=1)
parser.add_argument('-f', '--filename', default='large_binary_file.txt')

args = parser.parse_args()

with open('{} - {}'.format(args.size_in_mb, args.filename), 'wb+') as f_:
    f_.write(b'.'.join([randbytes(1000000) for aa in range(0, args.size_in_mb)]))
