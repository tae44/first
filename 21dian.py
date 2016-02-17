# -*- coding: utf-8 -*-
import random
import sys

class Game:
    puke = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6',\
      '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J',\
      'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K'] #牌库
    puke_score = { #牌所对应的分值
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }
    people_pai = [] #玩家牌库
    cpu_pai = [] #CPU牌库
    def __init__(self, money):
        self.money = money

    def fapai(self): #发牌
        x = random.choice(self.puke)
        self.people_pai.append(x)
        self.puke.remove(x)
        x = random.choice(self.puke)
        self.cpu_pai.append(x)
        self.puke.remove(x)
        x = random.choice(self.puke)
        self.people_pai.append(x)
        self.puke.remove(x)
        x = random.choice(self.puke)
        self.cpu_pai.append(x)
        self.puke.remove(x)

    def result(self):
        if p1.judge == 0 and p2.judge == 0: #双方都不要牌了
            print ('玩家的手牌是:', '\t', self.people_pai, '\t玩家的分数是:', '\t', p1.score)
            print ('CPU的手牌是:', '\t', self.cpu_pai, '\tCPU的分数是:', '\t', p2.score)
            if len(p1.people_pai) == 5 and p1.score <= 21:
                print ('玩家获胜!')
            elif len(p2.cpu_pai) == 5 and p2.score <= 21:
                print ('CPU获胜!')
            elif len(p1.people_pai) == 5 and len(p2.cpu_pai) == 5 and p1.score <= 21 < p2.score:
                print ('玩家获胜!')
            elif len(p1.people_pai) == 5 and len(p2.cpu_pai) == 5 and p2.score <= 21 < p1.score:
                print ('CPU获胜!')
            elif p1.score <= 21 < p2.score:
                print ('玩家获胜!')
            elif p2.score <= 21 < p1.score:
                print ('CPU获胜!')
            elif 21 >= p1.score > p2.score:
                print ('玩家获胜!')
            elif 21 >= p2.score > p1.score:
                print ('CPU获胜!')
            elif p1.score > p2.score > 21:
                print ('CPU获胜!')
            elif p2.score > p1.score > 21:
                print ('玩家获胜!')
            elif p1.score == p2.score:
                print ('打平了!')
            sys.exit('游戏结束!')

class People(Game):
    def __init__(self, money, judge):
        Game.__init__(self, money)
        self.judge = judge

    def zhuapai(self): #抓牌
        print ('你现在的手牌是:', self.people_pai)
        zhua = input('是否抓牌(y/n)?')
        if zhua == 'y':
            x = random.choice(self.puke)
            print ('你抓了一张%s.' % x)
            self.people_pai.append(x)
            self.puke.remove(x)
            if len(self.people_pai) == 3:
                self.score = self.puke_score.get(self.people_pai[0])+self.puke_score.get(self.people_pai[1])\
                +self.puke_score.get(self.people_pai[2]) #根据手里牌库有的牌,当做字典的key,去get对应的数值
            elif len(self.people_pai) == 4:
                self.score = self.puke_score.get(self.people_pai[0])+self.puke_score.get(self.people_pai[1])\
                +self.puke_score.get(self.people_pai[2])+self.puke_score.get(self.people_pai[3])
            elif len(self.people_pai) == 5:
                self.score = self.puke_score.get(self.people_pai[0])+self.puke_score.get(self.people_pai[1])\
                +self.puke_score.get(self.people_pai[2])+self.puke_score.get(self.people_pai[3])\
                +self.puke_score.get(self.people_pai[4])
            p2.zhuapai()
        elif zhua == 'n':
            if len(self.people_pai) == 2:
                self.score = self.puke_score.get(self.people_pai[0])+self.puke_score.get(self.people_pai[1])
            self.judge = 0
            p1.result() #判断双方是否都不要牌
            p2.zhuapai()
        else:
            print ('输入错误!')
            self.zhuapai()

class Cpu(Game):
    def __init__(self, money, judge):
        Game.__init__(self, money)
        self.judge = judge

    def zhua(self):
        if self.score > 15:
            print ('CPU不要了!')
            self.judge = 0
            p1.result()
            p1.zhuapai()
        else:
            x = random.choice(self.puke)
            self.cpu_pai.append(x)
            self.puke.remove(x)
            print ('CPU抽了一张手牌.')
            if p1.judge == 0:
                p2.zhuapai()
                p1.result()
            else:
                p1.zhuapai()

    def zhuapai(self):
        if len(self.cpu_pai) == 2:
            self.score = self.puke_score.get(self.cpu_pai[0])+self.puke_score.get(self.cpu_pai[1])
            p2.zhua()
        elif len(self.cpu_pai) == 3:
            self.score = self.puke_score.get(self.cpu_pai[0])+self.puke_score.get(self.cpu_pai[1])\
            +self.puke_score.get(self.cpu_pai[2])
            p2.zhua()
        elif len(self.cpu_pai) == 4:
            self.score = self.puke_score.get(self.cpu_pai[0])+self.puke_score.get(self.cpu_pai[1])\
            +self.puke_score.get(self.cpu_pai[2])+self.puke_score.get(self.cpu_pai[3])
            p2.zhua()
        elif len(self.cpu_pai) == 5:
            self.score = self.puke_score.get(self.cpu_pai[0])+self.puke_score.get(self.cpu_pai[1])\
            +self.puke_score.get(self.cpu_pai[2])+self.puke_score.get(self.cpu_pai[3])\
            +self.puke_score.get(self.cpu_pai[4])
            p2.zhua()

p1=People(200,1)
p2=Cpu(200,1)
p1.fapai()
p1.zhuapai()
