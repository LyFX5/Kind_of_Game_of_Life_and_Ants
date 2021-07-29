
# 0 spase
# 1 friend
# 2 wall

import random

class Creature():
    def __init__(self,negh,calor,pos,onMe):
        self.negh = negh
        self.pos = pos
        self.calor = calor
        self.onMe = onMe

    def move(self): # после каждого мув можно делать сет соседи чтоб окружение повлияло на организм и например спустило вниз
        if self.negh[2] == 0:
            print("I win")
        else:
            if self.negh[2].getCalor() == 0: # если впереди пусто
                self.goStr()
                # можно добавить чтоб с какой то вероятностью всеравно прыгал на соседа
            elif self.negh[2].getCalor() == 2: # стена
                if self.negh[0] != 0:
                    if self.negh[0].getCalor() == 1:
                        self.jump(self.negh[0],0)
            else:
                a = random.randint(0,1)
                if a == 1:
                    self.jump(self.negh[2],1)

    def goStr(self):
        self.pos[0] += 8
        for t in self.onMe:
            p = t.getPos()
            t.setPos(p[0]+8, p[1])
        

    def jump(self,fr,fb):
        h = len(fr.onMe)+1
        if fb == 0:
            d = -1
        else:
            d = 1
        self.pos[0] = self.pos[0]+(d*8)
        self.pos[1] -= (h*8)
        for t in self.onMe:
            p = t.getPos()
            t.setPos(p[0]+(d*8), p[1]-(h*8))
            

    def setNegh(self,ng):
        self.negh = ng

    def getPos(self):
        return self.pos

    def setPos(self,x,y):
        self.pos = [x,y]

    def getNegh(self):
        return self.negh

    def getOnMe(self):
        return self.onMe

    def setOnMe(self,onm):
        self.onMe = onm

    def getCalor(self):
        return self.calor
    





        
