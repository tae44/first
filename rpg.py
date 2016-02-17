# -*- coding: utf-8 -*-
import random
import string
import sys
import time

class Game:
    def __init__(self, name, level, attack, defense, blood, money): #定义等级,攻击,防御,血量,金钱
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.blood = blood
        self.money = money

    def begin_game(self):
        begin = input('请选择游戏模式(1:开始冒险  2:商店购物  3.查询状态  4:无限模式): ')
        if begin == '1':
            self.adventure()
        elif begin == '2':
            self.shop()
        elif begin == '3':
            p.state()
        elif begin == '4':
            self.loop_adventure()
        else:
            print('输入错误!')
            self.begin_game()

    def adventure(self): #冒险模式
        m.create_monster()
        print('你遇到了%s!怪物等级%d,血量%d,攻击力%d,防御力%d' % (m.name, m.level, m.blood, m.attack, m.defense))
        choose = input('你现在怎么做(1:攻击  2:逃跑): ')
        if choose == '1':
            p.action_attack()
        elif choose == '2':
            p.action_escape()
        else:
            print('错误的输入!')

    def loop_adventure(self):
        m.create_monster()
        time.sleep(1)
        print('你遇到了%s!怪物等级%d,血量%d,攻击力%d,防御力%d' % (m.name, m.level, m.blood, m.attack, m.defense))
        p.loop_play_p()

    def shop(self): #商店模式
        print('''
            ************************************
              1.补血药(+20血) ----------->  5金
              2.退出
            ************************************
        ''')
        shop_choose = input('您需要买什么: ')
        if shop_choose == '1':
            number = int(input('您需要买几个: '))
            if p.money > number * 5:
                print('购买成功!血量增加了%d!' % (number * 20))
                p.blood += number * 20
                p.money -= number * 5
            else:
                print('您的钱不够!')
                self.begin_game()
        elif shop_choose == '2':
            self.begin_game()
        else:
            print('输入错误!')
            self.shop()

    def state(self): #查询状态
        print('''                等级: %d
                攻击: %d
                防御: %d
                血量: %d
                最大血量: %d
                金钱: %d
                装备: ''' % (p.level, p.attack, p.defense, p.blood, p.max_blood, p.money))
        self.begin_game()

class Jason(Game): #主人公
    def __init__(self, name, level, attack, defense, blood, money, escape_rate, level_rate, max_blood): #增加逃跑几率,升级几率,最大血量
        Game.__init__(self, name, level, attack, defense, blood, money)
        self.escape_rate = escape_rate
        self.level_rate = level_rate
        self.max_blood = max_blood

    def action_attack(self): #攻击动作
        x = random.randint(1,4) #避免每次数值一样,生成一个随机变量
        hurt = round(abs(p.attack - m.defense * 0.7) + random.random() * x) #round函数四舍五入
        m.blood -= hurt
        print('你对%s发起了攻击, 对它造成了%d点伤害!' % (m.name, hurt))
        if m.blood <= 0:
            self.level_rate = random.random()
            print('%s死了!战斗指数大于0.555555时即可升级,此次战斗的升级指数为%f.' % (m.name, self.level_rate))
            if self.level_rate > 0.555555:
                self.level += 1
                self.max_blood = self.max_blood * random.random() * 0.4 + self.max_blood + self.level
                self.blood = self.max_blood
                self.attack = round(self.attack * random.random() * 0.3 + self.attack + self.level)
                self.defense = round(self.defense * random.random() * 0.3 + self.defense + self.level)
                print('你升级了!')
                print('''
                等级 \t\t↑ \t%d
                攻击力 \t\t↑ \t%d
                防御力 \t\t↑ \t%d
                最大血量 \t↑ \t%d
                ''' % (self.level, self.attack, self.defense, self.max_blood)
                      )
                m.drop_money()
            else:
                print('指数不够,无法升级!')
                m.drop_money()
        else:
            m.action_attack()
        self.begin_game()

    def loop_play_p(self):
        x = random.randint(1,4)
        hurt = round(abs(p.attack - m.defense * 0.7) + random.random() * x)
        m.blood -= hurt
        print('你对%s发起了攻击, 对它造成了%d点伤害!' % (m.name, hurt))
        time.sleep(0.2)
        if m.blood <= 0:
            self.level_rate = random.random()
            print('%s死了!战斗指数大于0.555555时即可升级,此次战斗的升级指数为%f.' % (m.name, self.level_rate))
            if self.level_rate > 0.555555:
                self.level += 1
                self.max_blood = self.max_blood * random.random() * 0.4 + self.max_blood + self.level
                self.blood = self.max_blood
                self.attack = round(self.attack * random.random() * 0.3 + self.attack + self.level)
                self.defense = round(self.defense * random.random() * 0.3 + self.defense + self.level)
                print('''
                你升级了!
                等级 \t\t↑ \t%d
                攻击力 \t\t↑ \t%d
                防御力 \t\t↑ \t%d
                最大血量 \t↑ \t%d
                ''' % (self.level, self.attack, self.defense, self.max_blood))
                p.loop_adventure()
            else:
                print('指数不够,无法升级!')
                p.loop_adventure()
        else:
            m.loop_play_m()

    def action_escape(self): #逃跑动作
        self.escape_rate = random.random()
        if self.escape_rate > 0.555555:
            print('逃跑成功!')
            p.begin_game()
        else:
            print('逃跑失败!')
            m.action_attack()

class Monster(Game): #怪物
    def __init__(self, name, level, attack, defense, blood, money, drop_rate): #增加掉落率
        Game.__init__(self, name, level, attack, defense, blood, money)
        self.drop_rate = drop_rate

    def create_monster(self): #生成怪物
        a = list(string.ascii_uppercase)
        random.shuffle(a)
        self.name = ''.join(a[:3])
        self.level = p.level + random.randint(1,2)
        x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        self.attack = p.attack + self.level + int(random.choice(x)) - random.randint(0,3)
        self.defense = p.defense + self.level + int(random.choice(x)) - random.randint(0,3)
        self.blood = p.max_blood + self.level + int(random.choice(x)) - random.randint(0,3)
        self.drop_rate = random.random()

    def action_attack(self):
        x = random.randint(1,4)
        hurt = round(abs(m.attack - p.defense * 0.8) + random.random() * x)
        p.blood -= hurt
        print('%s发起了攻击, 对你造成了%d点伤害!' % (self.name, hurt))
        if p.blood <= 0:
            print('你死了!')
            life = input('是否复活(y/N)?')
            if life == 'y':
                if p.money >= 20:
                    p.money -= 20
                    print('扣除费用20金!你现在复活了!')
                    p.blood = p.max_blood
                    p.begin_game()
                else:
                    sys.exit('你身上的钱不够!游戏结束!')
            else:
                sys.exit('游戏结束!')
        else:
            p.action_attack()

    def loop_play_m(self):
        x = random.randint(1,4)
        hurt = round(abs(m.attack - p.defense * 0.8) + random.random() * x)
        p.blood -= hurt
        print('%s发起了攻击, 对你造成了%d点伤害!' % (self.name, hurt))
        if p.blood <= 0:
            print('你死了!')
            self.money += 1
            if (self.money % 5) == 0: #每死5次会问是否继续游戏,本意为了避免栈溢出,但实际还会溢出
                if_play = input('是否继续玩(y/n): ')
                if if_play == 'y':
                    p.blood = p.max_blood
                    p.loop_adventure()
                else:
                    sys.exit('游戏结束!')
            else:
                p.blood = p.max_blood
                p.loop_adventure()
        else:
            p.loop_play_p()

    def drop_money(self):
        if self.drop_rate > 0.455555:
            x = self.drop_rate * 10 - 2
            p.money += x
            print('掉落了%d金!' % x)
        else:
            print('没有掉落任何战利品!')

p = Jason('Jason', 1, 15, 15, 30, 20, 0.5, 0.55, 30)
m = Monster('Monster', 1, 10, 10, 20, 10, 0.5)
p.begin_game()