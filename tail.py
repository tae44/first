# ex: python tail.py -n 3 ../456.txt
# import sys
# command, d = [], []
# [command.append(i) for i in sys.argv]
# with open(command[3], 'r') as f:
#     [d.append(x) for x in f.readlines()]
#     d.reverse()
#     for x in range(int(command[2])):print(d[x])

import time

def tail(list=[], pos=None):
    while True:
        list = []
        with open('/Users/a123/Desktop/456.txt') as f:
            [list.append(x) for x in f.readlines()]
            list.reverse()
            pos = f.tell()
            return list, pos

while True:
    l1, p1 = tail()
    time.sleep(0.1)
    l2, p2 = tail()
    if p1 > p2: print(l1[0])
    elif p1 < p2: print(l2[0])
    else: continue

# def r1():
#     while True:
#         d = []
#         with open('/Users/a123/Desktop/456.txt') as f:
#             [d.append(x) for x in f.readlines()]
#             d.reverse()
#             pos = f.tell()
#             return d[0], pos
# def r2():
#     while True:
#         d = []
#         with open('/Users/a123/Desktop/456.txt') as f:
#             [d.append(x) for x in f.readlines()]
#             d.reverse()
#             pos = f.tell()
#             return d[0], pos
#
# while True:
#     d1, pos1 = r1()
#     time.sleep(0.1)
#     d2, pos2 = r2()
#     if pos1 == pos2: continue
#     else:
#         if pos1 > pos2:
#             print(d1)
#         else:
#             print(d2)