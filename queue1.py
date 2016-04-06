class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node # 队尾的指针指向新加元素
            self.tail = node # 新加元素变为tail

    def pop(self):
        if self.head is None:
            raise Exception('empty queue')
        node = self.head
        self.head = node.next # head变为删除元素的下一个
        return node.value

if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.put(i)

    for _ in range(10):
        print(q.pop())
