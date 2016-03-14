# ex: python tail.py -n 3 ../456.txt
# import sys
# command, d = [], []
# [command.append(i) for i in sys.argv]
# with open(command[3], 'r') as f:
#     [d.append(x) for x in f.readlines()]
#     d.reverse()
#     for x in range(int(command[2])):print(d[x])

import time, os

filename = '/Users/a123/Desktop/456.txt'
file = open(filename,'r')

st_size = os.stat(filename)[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        if 'article' in line:
            print(line,)