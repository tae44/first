# 一个数如果恰好等于它的因子之和,这个数就称为"完数".例如6=1＋2＋3,编程找出1000以内的所有完数.

def fn(p):
    ret = []
    for i in range(1, p):
        if p % i == 0:
            ret.append(i)
    if sum(ret) == p:
        print('This num {} is perfect number.'.format(p))

list(map(fn, range(2,1001)))
