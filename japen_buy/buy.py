# -*- coding: utf-8 -*-
from openpyxl import Workbook
import datetime

def buy():
    global total_weight
    o, total_price, total_weight = 0, 0, 0
    name_list, price_list, num_list, weight_list = [], [], [], []
    while True:
        name = input('请输入商品名称: ')
        price = int(input('请输入商品单价(円): '))
        num = int(input('请输入商品数量: '))
        weight = int(input('请输入商品单个重量(g): '))
        name_list.append(name)
        price_list.append(price)
        num_list.append(num)
        weight_list.append(weight)
        o += 1
        choose = input('是否打印购物列表(y/N): ')
        if choose == 'y':
            print('-'*60)
            for i in range(o):
                total_price += price_list[i]*num_list[i]
                total_weight += weight_list[i]*num_list[i]
                print(i, '名称:', name_list[i], '单价(円):', price_list[i], '单重(g):', weight_list[i])
            freight()
            delete = int(input('是否删除某一行(输入-1不删除任何数据并显示详细情况): '))
            if delete == -1:
                print('-'*60)
                for j in range(o):
                    proportion = weight_list[j]*num_list[j]/total_weight
                    print(j, '名称:', name_list[j], '数量:', num_list[j], '总价格(円):', price_list[j]*num_list[j], '总重量(g):', weight_list[j]*num_list[j], \
                          '重量占比(%):', round(proportion*100, 1), '商品加成(円):', round((freight_price_total*proportion)/num_list[j]), \
                          '商品估算成本价(円):', price_list[j]+round((freight_price_total*proportion)/num_list[j]))
                print('商品总数:', i+1, '总价值(円):', total_price, '总重量(g):', total_weight)
                print('-'*60)
                if_quit = input('是否要保存退出（y/N): ')
                if if_quit == 'y':
                    wb = Workbook()
                    ws = wb.active
                    ws.title = '成本计算单'
                    for k in range(o):
                        proportion = weight_list[k]*num_list[k]/total_weight
                        ws.append(['名称:', name_list[k], '数量:', num_list[k], '总价格(円):', price_list[k]*num_list[k], '总重量(g):', weight_list[k]*num_list[k], \
                          '重量占比(%):', round(proportion*100, 1), '商品加成(円):', round((freight_price_total*proportion)/num_list[k]), \
                          '商品估算成本价(円):', price_list[k]+round((freight_price_total*proportion)/num_list[k])])
                    ws.append(['商品总数:', i+1, '总价值(円):', total_price, '总重量(g):', total_weight])
                    wb.save(r'E:\%s.xlsx' % datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M")) #时区问题
                    break
                else:
                    total_price, total_weight = 0, 0
            else:
                name_list.pop(delete)
                num_list.pop(delete)
                price_list.pop(delete)
                weight_list.pop(delete)
                o -= 1
                total_price, total_weight = 0, 0
        else: continue

def freight():
    global freight_price_total
    freight_weight = [1000, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10000, 11000, 12000, 13000, 14000, 15000,\
                      16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
    freight_price = [1500, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 3750, 3950, 4150, 4350, 4550, 4750,\
                     4950, 5150, 5350, 5550, 5750, 5950, 6150, 6350, 6550, 6750, 6950, 7150, 7350]
    for k in freight_weight:
        if k > total_weight:
            l = freight_weight.index(k)
            difference = k - total_weight
            if difference > 250:
                freight_price_total = freight_price[l]
                print('估算出的物流重量档位为 %.1f kg. 物流费用大概为 %d 円.' % ((k/1000), freight_price_total))
            else:
                freight_price_total = freight_price[l+1]
                print('货物重量接近升级档位, 因此物流费用上涨为 %d 円.' % freight_price_total)
            break

buy()
