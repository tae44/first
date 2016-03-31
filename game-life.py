# -*- coding: utf-8 -*-
import sys
import time

class People:
    skill = [] #技能列表
    age_increase = 0 #年龄计时器
    def __init__(self, name, sex, age, attraction, deposit): #姓名,性别,年龄,魅力值,存款
        self.name = name
        self.sex = sex
        self.age = age
        self.attraction = attraction
        self.deposit = deposit

    def age_add(self): #增加年龄的方法
        a = self.age_increase
        b, c = divmod(a, 12) #b为除12的商,即增加的年龄
        d = 30 + b
        self.age = d
        self.attraction -= b * 2 #b也为每年减少的魅力值基数

class Jason(People):
    def __init__(self, name, sex, age, attraction, deposit, income, lover): #增加了收入和爱人属性
        People.__init__(self, name, sex, age, attraction, deposit)
        self.income = income
        self.lover = lover

    def talk(self):
        print('游戏过程中请不要退出, 保存功能没完成.')
        print('你好, 欢迎来到这个游戏. 我的名字是 %s, 我的女友是 %s, 我现在有 %s 元存款, 收入是 %d 元/月, 初始技能是 %s, 初始魅力值为 %d.'\
        % (self.name, self.lover, self.deposit, self.income, self.skill, self.attraction))
        print()

    def do_sth(self):
        print('-' * 30)
        print('''        1. 工作
        2. 学习
        3. 与Jane交谈
        4. 查询状态''')
        print('-' * 30)
        try:
            doing = int(input('你想要做什么: '))
        except ValueError:
            print('数值不能为空!')
            self.do_sth()
        if doing == 1:
            self.work()
        elif doing == 2:
            self.study()
        elif doing == 3:
            self.talk_to_Jane()
        elif doing == 4:
            print('#' * 30)
            print('你现在的年龄是 %s 岁.' % self.age)
            print('你现在的余额有 %d 元.' % self.deposit)
            print('你现在的魅力值是 %d.' % self.attraction)
            print('你现在拥有的技能是 %s.' % self.skill)
            print('#' * 30)
            self.do_sth()

    def work(self):
        print('你现在的收入是 %d 元/月.' % self.income)
        try:
            work_time = int(input('你想要工作多长时间(月): '))
        except ValueError:
            print('数值不能为空!')
            self.work()
        time.sleep(work_time * 0.1)
        self.deposit += self.income * work_time
        print('工作完成! 你赚了 %d 元.' % (self.income * work_time))
        self.age_increase += work_time
        self.age_add()
        self.do_sth()

    def study(self):
        print('*' * 75)
        print('''        1. 蓝翔技校(学费500元, 时间3个月, 增加厨师技能, 收入增加50)
        2. 马哥培训(学费3000元, 时间6个月, 增加Linxu技能, 收入增加100)
        3. 哈弗大学(学费10000元, 时间12个月, 增加英语技能, 收入增加300)''')
        print('*' * 75)
        try:
            study_choose = int(input('请选择学校: '))
        except ValueError:
            print('数值不能为空!')
            self.study()
        if study_choose == 1:
            if self.deposit < 500:
                print('你的学费不够, 先去赚钱吧!')
                self.do_sth()
            else:
                print('欢迎加入蓝翔技校! 现在开始学习ing...')
                self.deposit -= 500
                self.age_increase += 3
                self.age_add()
                time.sleep(1)
                print('你毕业了! 技能增加厨师技能! 魅力值增加15! 收入增加了!')
                self.skill.append('Cooking')
                self.attraction += 15
                self.income += 50
                self.do_sth()
        elif study_choose == 2:
            if self.deposit < 3000:
                print('你的学费不够, 先去赚钱吧!')
                self.do_sth()
            else:
                print('欢迎加入马哥培训! 现在开始学习ing...')
                self.deposit -= 3000
                self.age_increase += 6
                self.age_add()
                time.sleep(2)
                print('你毕业了! 技能增加Linxu技能! 魅力值增加30! 收入增加了!')
                self.skill.append('Linux')
                self.attraction += 30
                self.income += 100
                self.do_sth()
        elif study_choose == 3:
            if self.deposit < 10000:
                print('你的学费不够, 先去赚钱吧!')
                self.do_sth()
            else:
                print('欢迎加入哈弗大学! 现在开始学习ing...')
                self.deposit -= 10000
                self.age_increase += 12
                self.age_add()
                time.sleep(3)
                print('你毕业了! 技能增加英语技能! 魅力值增加50! 收入增加了!')
                self.skill.append('English')
                self.attraction += 50
                self.income += 300
                self.do_sth()

    def talk_to_Jane(self):
        print('今天, 我决定去找 %s, 为了挽回我们的爱情.' % P2.name)
        print('我找到了 %s, 对她说: %s, 我们和好吧, 我不再是屌丝了!' % (P2.name, P2.name))
        if self.attraction > 70:
            print('%s说: 你确实跟以前不一样了...' % P2.name)
            if self.age > 36:
                print('但是你已经是个老炮儿了! 老娘喜欢小鲜肉! 再见!')
                sys.exit('GAME OVER!')
            else:
                print('咱们结婚吧!')
        else:
            print('%s说: 你别这样, 咱俩不可能了.' % P2.name)
            self.do_sth()

class Jane(People):
    def __init__(self, name, sex, age, attraction, deposit, lover):
        People.__init__(self, name, sex, age, attraction, deposit)
        self.lover = lover

class Peter(People):
    def __init__(self, name, sex, age, attraction, deposit, income, lover):
        People.__init__(self, name, sex, age, attraction, deposit)
        self.income = income
        self.lover = lover

P1 = Jason('Jason', 'M', 30, 30, 100, 50, 'Jane')
P1.talk()

P2 = Jane('Jane', 'F', 24, 80, 1000, 'Jason')

P3 = Peter('Peter', 'M', 28, 80, 200000, 1000, '')

print('有一天,我找到我的女朋友 %s.' % P1.lover)
print(P1.lover,'说: 我们分手吧, 我不想和穷屌丝在一起了...')
print('我说: 为什么要这样对我？')
print(P1.lover,'说: 我已经和 %s 好上了, 你以后不要再找我了.' % P3.name)

P2.lover = P3.name
P3.lover = P2.name
P1.lover = None

print('我独自站在寒风中, 悲伤不已, 发誓要好好努力, 打败 %s.' % P3.name)

P1.do_sth()