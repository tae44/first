#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import ChainMap

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
