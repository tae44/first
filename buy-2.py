# -*- coding: utf-8 -*-

class Buy:
    item_table, item_detailed_table = [], []   # 列表,详细列表

    def enter_date(self):
        self.name = input('请输入商品名称: ')
        self.price = int(input('请输入商品价格: '))
        self.number = int(input('请输入购买数量: '))
        self.weight = int(input('请输入商品重量: '))
        self.table()

    def print(self):
        print_choose = input('是否打印列表(y/N): ')
        if print_choose == 'y':
            print('名称', '价格', '数量', '重量')
            [print(x) for x in self.item_table]
            detailed_choose = input('是否显示详细信息(y/N): ')
            if detailed_choose == 'y':
                print('名称', '总价', '总重', '重量占比', '价格加成', '商品估算成本价')
                [print(y) for y in self.item_detailed_table]
            else:
                self.enter_date()
        else:
            self.enter_date()

    def table(self):   # 列表生成
        self.item_table.append([self.name, self.price, self.number, self.weight])
        self.item_detailed_table.append([self.name, self.price*self.number, self.weight*self.number])
        self.total_frmae()
        self.print()

    def total(self):
        self.total_frmae()
        print('总价:', self.total_price)
        print('总重:', self.total_weight)

    def zhanbi(self):   # 计算百分比
        self.total_frmae()
        for i in range(len(self.item_table)):
            self.item_detailed_table[i].append((self.item_detailed_table[i][2]/self.total_weight)*100)
        print(self.item_detailed_table)

    def total_frmae(self):   # 计算总价和总重的框架
        self.total_price = 0
        self.total_weight = 0
        for i in range(len(self.item_table)):
            self.total_price += self.item_detailed_table[i][1]
            self.total_weight += self.item_detailed_table[i][2]

class Japen(Buy):
    freight_weight = [1000, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10000, 11000, 12000, 13000, 14000, 15000,\
                      16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
    freight_price = [1500, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 3750, 3950, 4150, 4350, 4550, 4750,\
                     4950, 5150, 5350, 5550, 5750, 5950, 6150, 6350, 6550, 6750, 6950, 7150, 7350]

    def estimate(self):   # 计算重量档位和运费
        for self.limit in self.freight_weight:
            if self.total_weight < self.limit:
                x = self.freight_weight.index(self.limit)
                break
        print('重量估算为{0}g,运费估算为{1}円'.format(self.limit, self.freight_price[x]))

j = Japen()
j.enter_date()
j.estimate()