class Node:
    def __init__(self, value):
        self.value = value # 节点的值
        self.next = None # 节点的指向游标


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top # 节点的游标指向之前的栈顶
        self.top = node # 自己变成栈顶

    def pop(self):
        node = self.top
        self.top = node.next # 栈顶游标指向下一个数据节点
        return node.value # 最上层的弹出

if __name__ == '__main__':
    stack = Stack()
    exp = '({a * [x/(x+y)]})'
    for c in exp:
        if c in '{[(':
            stack.push(c)
        elif c in '}])':
            v = stack.top.value
            if c == '}' and v != '{':
                raise Exception('failed')
            if c == ']' and v != '[':
                raise Exception('failed')
            if c == ')' and v != '(':
                raise Exception('failed')
            stack.pop()
    if stack.top is not None:
        raise Exception('failed')
    print("ok")