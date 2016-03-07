# def add(num):
#     if len(str(num)) == 1:
#         return num
#     ret = 0
#     for i in str(num):
#         ret += int(i)
#     return add(ret)
#
# print(add(88))

def add(num):
    return sum([int(x)**2 for x in str(num)])
    # ret = 0
    # for i in str(num):
    #     ret += int(i)**2
    # return ret

def cacl(num):
    results = {num}
    ret = num
    while ret >= 10:
        ret = add(ret)
        if ret in results:
            return False
        results.add(ret)
    return ret == 1

for i in range(1, 10001):
    if cacl(i):
        print('{} is happy number'.format(i))