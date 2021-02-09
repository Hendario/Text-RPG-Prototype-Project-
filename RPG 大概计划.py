import csv
import time
import json
import random
import os


class Userdata():
    def welcome(self,name):
        print('欢迎你加入我们，【%s】'%name)

    def save(self):
        f = open('username.txt','w+')
        fw = f.writelines(playername)
        f.close()

    def menu(self):
        print('1.创建新用户')
        print('2.使用已有用户')

class playerdata():
    def __init__(self):
        x = 0

    def player_stat(self,血量,攻击,防御):
        self.player_health = 血量
        self.player_health = 攻击
        self.player_defense = 防御

    def player_wealth(self,金钱数量):
        self.player_money = 金钱数量
        return self.player_health

    def player_money_add(self,旧的钱,新的钱):
        总钱 = 旧的钱 + 新的钱
        return 总钱

class npc:
    def __init__(self):
        self.npcname = None
        self.npc_health = None
        self.npc_attack = None

    def npcdata(self,npcname,npchealth,npcattack):
        self.npcname = npcname
        self.npc_health = npchealth
        self.npc_attack = npcattack

    def npcexist(self,npcname):
        npctext = 'npc.txt'
        npcfile = open(npctext,'r')
        a = npcfile.readlines()
        if str(npcname) not in a:
            print(('There\'s no %1s in <%2s>')%(npcname,npctext))
        else:
            print('Detected! %1s is in <%2s>'%(npcname,npctext))

class Music:
    def __init__(self):
        self.music1 = 'test1.mp3'
        self.music1 = os.startfile(self.music1)
        return 'This is a music file'

    def battlemusic(self=0):
        music1 = 'test1.mp3'
        music1 = os.startfile(music1)
        return music1
    def backgroundmusic(self):
        pass
    def closemusic(self):
        pass


def loading(x):
    print('游戏正在加载中，请耐心等待')
    while x != 99 and x < 100:
        time.sleep(0.1)
        x += 1
        print('游戏加载中,进度已加载%1s...'%x)
    if x == 99:
        #a_hour = 3600
        a_sec = 1
        time.sleep(a_sec)
        x += 1
    if x == 100:
        print('感谢你的等待！游戏开始！')
    else:
        print('Error')

def Gamesystem():
    You = '你'

    player = {'health': 100, 'speed': 20, 'attack': 50, 'level': 1}

    npc1 = {'name': 'npc1', 'health': 100, 'speed': 25, 'attack': 21, 'level': random.randint(0, 10)}
    npc2 = {'name': 'npc2', 'health': 100, 'speed': 25, 'attack': 30, 'level': random.randint(0, 10)}
    npc3 = {'name': 'npc3', 'health': 100, 'speed': 25, 'attack': 40, 'level': random.randint(0, 10)}
    list1 = [npc1, npc2, npc3]

    def menu():
        print('This is a menu')

    def attack_monster(monster):
        decision = input('你发现了一只等级为%1s的[%2s],是否靠近？' % (npc1.get('level'), 'npc1'))
        monster_health = monster.get('health')
        player_health = player.get('health')
        while monster_health > 0 and player_health > 0 and decision.upper() != 'EXIT':
            decision = input('是否攻击？')
            if decision.upper() == 'YES':
                monster_attack = random.randint(0, monster.get('attack'))
                player_attack = random.randint(0, player.get('attack'))
                print('你对[%1s]造成了%2s的伤害' % (monster.get('name'), player_attack))
                monster_health -= player_attack
                print('[%1s]血条:%2s' % (monster.get('name'), monster_health))
                if monster_health <= 0:
                    print('---------------------')
                    print('你赢了！')
                    print('---------------------')
                    break
                player_health -= monster_attack
                if player_health <= 0:
                    print('---------------------')
                    print('你输了')
                    print('---------------------')
                    break
                print('[%1s]对你造成了%2s的伤害' % (monster.get('name'), monster_attack))
                print('[%1s]血条:%2s' % (You, player_health))

    def game_play(monster):
        attack_monster(monster)

    def random_monster(list):
        choose_monster = random.randint(0, len(list) - 1)
        return list[choose_monster]

    def startthegame(list):
        decision = input('要开始游戏吗？(YES?)\n')
        while decision.upper() == 'YES' and decision.upper() != 'EXIT':
            if decision.upper() == 'EXIT':
                break
            game_play(random_monster(list))

    startthegame(list1)


playername = input('欢迎你，我们的新用户，请问你的名字是？\n')

def main():
    userdata = Userdata()
    y = playerdata()
    userdata.save()
    userdata.welcome(playername)
    loading(0)
    Music.battlemusic()
    Gamesystem()

if __name__=="__main__":
    main()



