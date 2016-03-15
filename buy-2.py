# -*- coding: utf-8 -*-

def type(fn):
    def wrap(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except ValueError as e:
            print('请输入数字: ')
            fn(*args, **kwargs)
    return wrap

class Buy:
    item_table, item_detailed_table = [], []   # 列表,详细列表

    def enter_name(self):
        self.name = input('请输入商品名称: ')

    @type
    def enter_price(self):
        self.price = int(input('请输入商品价格: '))

    @type
    def enter_number(self):
        self.number = int(input('请输入购买数量: '))

    @type
    def enter_weight(self):
        self.weight = int(input('请输入商品重量: '))

class Japen(Buy):
    def enter_data(self):
        super(Japen, self).enter_name()
        super(Japen, self).enter_number()
        super(Japen, self).enter_price()
        super(Japen, self).enter_weight()

    freight_weight = [1000, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10000, 11000, 12000, 13000, 14000, 15000,\
                      16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
    freight_price = [1500, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 3750, 3950, 4150, 4350, 4550, 4750,\
                     4950, 5150, 5350, 5550, 5750, 5950, 6150, 6350, 6550, 6750, 6950, 7150, 7350]

j = Japen()
j.enter_data()