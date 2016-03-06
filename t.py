class A:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return self.name
    #
    # def __str__(self):
    #     return 'call __str__ name is {}'.format(self.name)
    #
    # def __bytes__(self):
    #     return 'call __bytes__ name is {}'.format(self.name).encode('utf-8')

a = A('Jason')
print(a)
# print(str(a))
# print(repr(a))
# print(bytes(a))