# -*- coding: utf-8 -*-
import random
class People:
    def __init__(self, name, sex, age, work, nation, attraction, deposit): #姓名,性别,年龄,工作,国籍,魅力值,存款
        self.name = name
        self.sex = sex
        self.age = age
        self.work = work
        self.nation = nation
        self.attraction = attraction
        self.deposit = deposit

    def add_people(self):
        name = raw_input('请输入用户名: ')
        sex = raw_input('请输入性别: ')
        age = int(raw_input('请输入年龄: '))
        work = raw_input('请输入工作: ')
        nation = raw_input('请输入国籍: ')
        attraction = raw_input('请输入魅力值: ')
        deposit = int(raw_input('请输入存款: '))

    def select_people(self):
        print '''
        1. John
        2. Liz
        3. Peter
        '''
        select_p = raw_input('请选择人物: ')
        if select_p == '1':
            d.talk()
            d.doing_sth()
        else:
            print '其他用户还没启用,请选择1.'
            d.select_people()

class John(People):
    def __init__(self, name, sex, age, work, nation, attraction, deposit, company):
        People.__init__(self, name, sex, age, work, nation, attraction, deposit)
        self.company = company

    def talk(self):
        print '你好, 欢迎来到这个游戏. 我的名字是 %s, 我是一个 %s 工作者, 我来自 %s, 我现在有 %s 元存款, 初始魅力值为 %s.'\
        % (self.name, self.work, self.nation, self.deposit, self.attraction)

    def doing_sth(self):
        print '''
        1. 工作
        2. 就餐
        3. 约会
        4. 赌博
        5. 查询余额
        '''
        do_sth = raw_input('下面你想做什么: ')
        if do_sth == '1':
            d.work_sth()
        elif do_sth == '2':
            pass
        elif do_sth == '3':
            print '你现在还没有女朋友!'
            d.doing_sth()
        elif do_sth == '4':
            d.dubo_sth()
        elif do_sth == '5':
            print '你的余额是:', self.deposit
            d.doing_sth()
        else:
            print '选择错误!请重新输入: '
            d.doing_sth()

    def work_sth(self):
        time = int(raw_input('你想要工作多长时间(12元/时): '))
        self.deposit += time * 12 #一小时12元工资
        print '你赚了 %s 元钱.' % (time*12)
        d.doing_sth()

    def dubo_sth(self):
        o = random.randint(0,10)
        benjin = int(raw_input('请下注: ')) #赌博的本金
        dubo = raw_input('你是压大还是压小: ')
        if dubo == '大' and o >= 5:
            print '结果是 %s ,你赢了 %s 元!' % (o, benjin*2)
            self.deposit += benjin * 1.5
            d.doing_sth()
        elif dubo == '小' and o < 5:
            print '结果是 %s ,你赢了 %s 元!' % (o, benjin*2)
            self.deposit += benjin * 2
            d.doing_sth()
        else:
            print '结果是 %s ,你输了 %s 元!' %  (o, benjin*3)
            self.deposit -= benjin * 3
            d.doing_sth()

d = John('John', 'M', 29, 'IT', 'China', 50, 1000, 'TAOBAO')
d.select_people()
