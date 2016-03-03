# 寻找 1 到 10000的happy number。
# happy number值， 对一个数字的每一位取平方后相加， 对得到的结果反复执行上一步， 直到最后只有一位， 如果等于1， 这个数成为happy number。
# 例如：19 是happy number， 因为
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#num = input('a: ')
#
#def loop(x,y):
#    while True:
#        for i in range(len(x)):
#            y += int(x[i])**2
#        if len(str(y)) == 1:
#            if y == 1:
#                print('{} is a happy number.'.format(num))
#                break
#            else:
#                print('{} is not a happy number.'.format(num))
#                break
#        else:
#            loop(str(y),0)
#            break
#
#loop(num,0)
def fit():
    for num in range(1,10001):
        yield num

def loop(y):
    a = fit()
    for num in next(a):
        for i in range(len(str(num))):
            y += int(str(num))**2
        if len(str(y)) == 1:
            if y == 1:
                print('{} is a happy number.'.format(num))
                break
        else:
            loop(0)
            break

loop(0)