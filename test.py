from stack import Stack

func_map = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

def cacl(expr):
    stack = Stack()
    d = []
    [d.append(x) for x in expr]
    for idx, c in enumerate(expr):
        if c in '(+-*/':
            stack.push(c)
        elif c.strip() == '':
            pass
        else:
            if stack.top is None:
                c = int(c)
                stack.push(c)
                continue
            if c != ')':
                c = int(c)
                try:
                    dd = d[idx+1]
                except IndexError as e:
                    pass
                if dd in '*/':
                    stack.push(c)
                else:
                    if stack.top.value in '+-*/':
                        s = stack.pop()
                        if not isinstance(stack.top.value, (int, float)):
                            raise Exception('wrong expr')
                        v = stack.pop()
                        v = func_map[s](v, c)
                        stack.push(v)
                    else:
                        stack.push(c)
            if c == ')':
                if isinstance(stack.top.value, (int, float)):
                    v = stack.pop()
                    if stack.top.value == '(':
                        stack.pop()
                        stack.push(v)
                    else:
                        raise Exception('wrong expr')
                else:
                    raise Exception('wrong expr')
    while stack.top:
        c = stack.pop()
        if not isinstance(c, (int, float)):
            raise Exception('wrong expr')
        if stack.top is None:
            return c
        else:
            if stack.top.value in '+-*/':
                s = stack.pop()
                if not isinstance(stack.top.value, (int, float)):
                    raise Exception('wrong expr')
                v = stack.pop()
                v = func_map[s](v, c)
                if stack.top is None:
                    return v
                stack.push(v)
            else:
                raise Exception('wrong expr')

if __name__ == '__main__':
    #print(cacl('(3 + 4) * 5 / ((2 + 3) * 3)'))
    print(cacl('3+4*5*6-2-2*2*3/2'))
