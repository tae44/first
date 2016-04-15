#!/usr/bin/python
# -*- coding: UTF-8 -*-

import heapq
from itertools import chain

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
for c in chain(a, b):
    print(c)
