#写一个find函数， 传入两个列表， 其中origin和items， items具有默认值[3, 4]。查找items中每个元素在origin中的所有位置。返回值为字典， key是items中的元素， value是位置的元组。
#例如： find([2, 3, 5,3, 4, 2, 7, 4]) 返回 {3:(1, 3), 4:(4, 7)}

from functools import partial

def find(li1,li2):
    ret = li1
    result = {}
    for i,v in enumerate(ret):
        if li2[0] == v:
            print('3 index is {}'.format(i))
        if li2[1] == v:
            print('4 index is {}'.format(i))

f = partial(find,li2=[3,4])
f([1,2,3,1,9,6,5,4,3,0,8,4,1])