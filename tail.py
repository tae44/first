# ex: python tail.py -n 3 ../456.txt
# import sys
# command, d = [], []
# [command.append(i) for i in sys.argv]
# with open(command[3], 'r') as f:
#     [d.append(x) for x in f.readlines()]
#     d.reverse()
#     for x in range(int(command[2])):print(d[x])

import time, os

# def tail(list=[], pos=None):
#     while True:
#         list = []
#         with open('/Users/a123/Desktop/456.txt') as f:
#             [list.append(x) for x in f.readlines()]
#             list.reverse()
#             pos = f.tell()
#             return list, pos
#
# while True:
#     l1, p1 = tail()
#     time.sleep(0.1)
#     l2, p2 = tail()
#     if p1 > p2: print(l1[0])
#     elif p1 < p2: print(l2[0])
#     else: continue

file = '/Users/a123/Desktop/456.txt'

def tail(f):
    f.seek(0,2)
    while True:
        line = f.readline()
        if not line: continue
        yield line

try:
    for i in tail(open(file, 'r')):
        print(i, end='')
except KeyboardInterrupt:
    pass
