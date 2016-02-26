# -*- coding: utf-8 -*-

def buy():
    global total_weight
    q = True
    o, total_price, total_weight = 0, 0, 0
    name_list, price_list, num_list, weight_list = [], [], [], []
    while q:
        name = input('请输入商品名称(输入q为退出): ')
        if name == 'q': break
        price = int(input('请输入商品单价(円): '))
        num = int(input('请输入商品数量: '))
        weight = int(input('请输入商品单个重量(g): '))
        name_list.append(name)
        price_list.append(price)
        num_list.append(num)
        weight_list.append(weight)
        o += 1
        choose = input('是否打印购物列表(y/N/q): ')
        if choose == 'y':
            print('-'*50)
            for i in range(o):
                total_price += price_list[i]*num_list[i]
                total_weight += weight_list[i]*num_list[i]
                print(i, '名称:', name_list[i], '单价(円):', price_list[i], '单重(g):', weight_list[i])
            delete = int(input('是否删除某一行(输入-1不删除任何数据并显示详细情况): '))
            if delete == -1:
                print('-'*50)
                for j in range(o):
                    print(j, '名称:', name_list[j], '数量:', num_list[j], '总价格(円):', price_list[j]*num_list[j], '总重量(g):', weight_list[j]*num_list[j], \
                          '重量占比(%):', round(weight_list[j]*num_list[j]/total_weight, 3))
                print('商品总数:', i+1, '此批货总价值(円):', total_price, '此批货总重(g):', total_weight)
                freight()
                total_price, total_weight = 0, 0
                continue
            else:
                name_list.pop(delete)
                num_list.pop(delete)
                price_list.pop(delete)
                weight_list.pop(delete)
                o -= 1
                total_price, total_weight = 0, 0
        elif choose == 'q':
            q = False
        else:
            continue

def freight():
    freight_weight = [1000, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 11000, 12000, 13000, 14000, 15000,\
                      16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
    freight_price = [1500, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 3950, 4150, 4350, 4550, 4750,\
                     4950, 5150, 5350, 5550, 5750, 5950, 6150, 6350, 6550, 6750, 6950, 7150, 7350]
    for i in freight_weight:
        if i > total_weight:
            j = freight_weight.index(i)
            difference = i - total_weight
            if difference > 250:
                print('估算出的货物重量为 %.1f kg. 物流费用大概为 %d 円.' % ((i/1000), freight_price[j]))
            else:
                print('货物重量接近升级档位, 因此物流费用上涨为 %d 円.' % (freight_price[j+1]))
            break

buy()
