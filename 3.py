#写一个find函数， 传入两个列表， 其中origin和items， items具有默认值[3, 4]。查找items中每个元素在origin中的所有位置。返回值为字典， key是items中的元素， value是位置的元组。
#例如： find([2, 3, 5,3, 4, 2, 7, 4]) 返回 {3:(1, 3), 4:(4, 7)}

from functools import partial

def find(li1,li2):
    ret = li1
    result, t3, t4 = {}, [], []
    for i,v in enumerate(ret):
        if li2[0] == v:
            t3.append(i)
        if li2[1] == v:
            t4.append(i)
    result[li2[0]]=t3
    result[li2[1]]=t4
    print(result)

f = partial(find,li2=[3,4])
f([1,2,3,1,9,6,5,4,3,0,8,4,1])