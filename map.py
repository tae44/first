class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = hash(key)

    def __eq__(self, other):
        return self.key == other.key

class Map:
    def __init__(self, init_size):
        self.__slot = [[] for _ in range(init_size)]
        # for _ in range(init_size):
        #     self.__slot.append([])
        self.__size = init_size

    def put(self, key, value):
        node = Node(key, value)
        address = node.key % self.__size
        self.__slot[address].append(node)

    def get(self, key, default=None):
        _key = hash(key)
        address = _key % self.__size
        for node in self.__slot[address]:
            if node.key == _key:
                return node.value
        return default

    def remove(self, key):
        address = hash(key) % self.__size
        try:
            self.__slot[address].remove(Node(key, None))
        except ValueError:
            pass
        # for idx, node in enumerate(self.__slot[address][:]):
        #     if node.key == key:
        #         self.__slot[address].pop(idx)

if __name__ == '__main__':
    map = Map(16)

    for i in range(20):
        map.put(i, i)

    map.remove(3)

    for i in range(20):
        print(map.get(i))