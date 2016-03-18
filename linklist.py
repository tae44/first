class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    num = 0

    def __init__(self):
        self.head = None # 列表的头和尾
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None: #列表为空时，头尾都是自己
            self.head = node
            self.tail = node
            self.num += 1
        else:
            self.tail.next = node #尾部的指针指向新加元素
            self.tail = node # 新加元素变为tail
            self.num += 1

    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next: # 如果下一个元素存在，游标继续往后走
            cur = cur.next
            yield cur.data

    def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        while cur_idx < idx-1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next # 新元素的指针指向原先游标的下一个
        cur.next = node # 原先的游标指向新元素新加元素
        self.num += 1
        if node.next is None:
            self.tail = node

    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        while cur_idx < idx-1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        cur.next = cur.next.next # 游标指针指向删除元素的下一个，被删除元素就没有游标指向他了
        self.num -= 1
        if cur.next is None:
            self.tail = cur

    def __len__(self):
        return self.num


if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(10):
        linked_list.append(i)
    linked_list.insert(3, 30)
    linked_list.insert(3, 40)
    linked_list.insert(10, 50)

    linked_list.remove(4)
    linked_list.remove(4)
    linked_list.remove(4)
    linked_list.remove(4)
    linked_list.remove(4)

    #for node in linked_list.iter():
    #  print(node)

    print(len(linked_list))

#TODO 判空
