# -*- coding: utf-8 -*-
import sys
from openpyxl import Workbook
import datetime

def type(fn):
    def wrap(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except ValueError:
            print('请输入数字: ')
            fn(*args, **kwargs)
    return wrap

class Buy:
    name_table, price_table, number_table, weight_table = [], [], [], []
    total_price, total_weight = [], []

    def enter_name(self):
        self.name = input('请输入商品名称: ')
        self.name_table.append(self.name)

    @type
    def enter_price(self):
        self.price = int(input('请输入商品价格: '))
        self.price_table.append(self.price)
        self.total_price.append(self.price * self.number)

    @type
    def enter_number(self):
        self.number = int(input('请输入购买数量: '))
        self.number_table.append(self.number)

    @type
    def enter_weight(self):
        self.weight = int(input('请输入商品重量: '))
        self.weight_table.append(self.weight)
        self.total_weight.append(self.weight * self.number)

    def print_table(self):
        print('序号', '\t', '名称', '\t', '价格', '\t', '数量', '\t', '重量', '\t')
        for i in range(len(self.name_table)):
            print('{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}'.
                format(i, self.name_table[i],self.price_table[i],self.number_table[i],self.weight_table[i]))

    def print_detailed_table(self):
        print('名称', '\t', '总价格', '\t', '总重量', '\t', '重量占比', '\t', '商品加成', '\t', '商品估算成本')
        for i in range(len(self.name_table)):
            print('{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}'.
                format(self.name_table[i], self.total_price[i], self.total_weight[i], round(self.total_weight[i]/sum(self.total_weight)*100, 2),
                       2,3))
        print('-' * 30)
        print('总价值: {0}      总重量: {1}'.format(sum(self.total_price),sum(self.total_weight)))

    def delete_item(self, i):
        self.name_table.pop(i)
        self.price_table.pop(i)
        self.number_table.pop(i)
        self.weight_table.pop(i)
        self.total_weight.pop(i)
        self.total_price.pop(i)

    def save_excel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = '成本计算单'
        ws.append(['名称:', '数量:', '总价格(円):', '总重量(g):', '重量占比(%):', '商品加成(円):', '商品估算成本价(円):'])
        # ws.append(['商品总数:', i+1, '总价值(円):', total_price, '总重量(g):', total_weight])
        wb.save(r'E:\%s.xlsx' % datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M"))

        # TODO 保存excel

    def exit_buy(self):
        sys.exit('exit...')

class Japen(Buy):
    def enter_data(self):
        super(Japen, self).enter_name()
        super(Japen, self).enter_number()
        super(Japen, self).enter_price()
        super(Japen, self).enter_weight()
        j.if_print()

    def if_print(self):
        print_choose = input('是否打印购物列表(y/N/d): ')
        if print_choose == 'y':
            super(Japen, self).print_table()
            self.if_del()
        elif print_choose == 'd':
            super(Japen, self).print_detailed_table()
            self.weight_price()
        else:
            self.enter_data()

    @type
    def if_del(self):
        del_choose = input('是否删除某一行(y/N): ')
        if del_choose == 'y':
            del_idx = int(input('请输入删除的序号: '))
            super(Japen, self).delete_item(del_idx)
        else:
            self.enter_data()

    def weight_price(self):
        freight_weight = [1000, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10000, 11000, 12000, 13000, 14000, 15000,
                      16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
        freight_price = [1500, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 3750, 3950, 4150, 4350, 4550, 4750,
                     4950, 5150, 5350, 5550, 5750, 5950, 6150, 6350, 6550, 6750, 6950, 7150, 7350]
        for i, v in enumerate(freight_weight):
            if sum(self.total_weight) < v:
                print('此批货物估算重量为{0}g,运费估算为{1}円.'.format(v, freight_price[i]))
                break
        if_quit = input('是否保存并退出(y/N): ')
        if if_quit == 'y':
            super(Japen, self).save_excel()
            super(Japen, self).exit_buy()
        else:
            self.enter_data()

j = Japen()
while True:
    j.enter_data()
