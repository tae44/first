# 给定一个非负整数 num， 重复的加每一位， 直到最后只剩一位。
num = input('Please enter your num: ')

def loop(x,y):
    while True:
        for i in range(len(x)):
            y += int(x[i])
        if len(str(y)) == 1:
            print(y)
            break
        else:
            loop(str(y),0)
            break

loop(num,0)