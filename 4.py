#写一个带一个default_user参数的装饰器， 此装饰器检查传入函数的关键字参数， 如果没有名为user的参数， 使用default_user 作为user参数传递给函数。
#例如：
#@inject_user(default_user=comyn)
#def do_something(*args, **kwargs):
#    print(kwargs['user'])
#调用 do_something() 时能输出 comyn

from functools import partial

def inject_user(default_user):
    def inject(fn):
        def wrap(user,*args,**kwargs):
            if user is None:
                return fn(user,*args,**kwargs)
            return fn(user,*args,**kwargs)
        return wrap
    return inject

@inject_user(default_user='comyn')
def pri(user):
    print('{} is good.'.format(user))
