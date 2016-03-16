# -*- coding: utf-8 -*-
import re

file = '/Users/a123/Desktop/456.txt'

def tail(x):
    with open(x, 'r') as f:
        f.seek(0, 2) # 指针移动到文章尾部
        while True:
            line = f.readline()
            if not line: continue
            else:
                def rere(par, li = line): # 减少书写长度
                    return re.findall(par, li)
                if match('&', match('&', rere('^is'), rere('was')), match('!', rere('789'), None)): # 可嵌套多表达式
                    print(line, end='')
logic = {
    '&': lambda x, y: x and y,
    '|': lambda x, y: x or y,
    '!': lambda x: not x
}

def match(x, a, b): # 定义a,b两个表达式之间的逻辑关系
    if x == '&' or x == '|':
        return logic[x](a, b)
    if x == '!':
        return logic[x](a)

if __name__ == '__main__':
    tail(file)
