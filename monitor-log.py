# 结合 tail -f 和规则解析， 写一个日志监控程序， 使用tail -f 逐行读入日志，并用规则解析程序来匹配，当匹配的打印一条日志

import re

file = '/Users/a123/Desktop/456.txt'

def tail(x):
    with open(x, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line: continue
            else:
                #m = match('&', '^1', '9')
                if re.findall('are', line):
                    print(line, end='')
fuck = {
    '&': lambda x, y: x and y,
    '|': lambda x, y: x or y,
    '!': lambda x: not x
}

def match(x, a, b):
    if x == '&' or x == '|':
        print(fuck[x](a, b))
    if x == '!':
        print(fuck[x](a))

if __name__ == '__main__':
    tail(file)
