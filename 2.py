# 寻找 1 到 10000的happy number。
# happy number值， 对一个数字的每一位取平方后相加， 对得到的结果反复执行上一步， 直到最后只有一位， 如果等于1， 这个数成为happy number。
# 例如：19 是happy number， 因为
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def loop(y):
    while True:
        l = fin()
        for i in range(len(l)):
            y += int(l[i])**2
        if len(str(y)) == 1:
            if y == 1:
                print('{} is a happy number.'.format(l))
                break
            else:break
        else:
            print(1111)
            break

def fin():
    for j in range(1, 11):
        j = str(j)
        k = iter(j)
        return list(k)

loop(0)