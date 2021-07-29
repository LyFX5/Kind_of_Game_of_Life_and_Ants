import random

class Creature():
    def __init__(self,negh,calor,pos):
        self.negh = negh
        self.calor = calor
        self.pos = pos

    def changeCalor1(self):
        q = 0
        for n in self.negh:
            if n.getCalor() == 0:
                q += 1
        if q > 2:
            self.calor = 1
            return True
        else:
            return False

    def changeCalor2(self):
        sc = self.calor
        q = 0
        p = 0
        for n in self.negh:
            if n.getCalor() == 0:
                q += 1
            else:
                p += 1
        if q > p:
            self.calor = 0
        elif p > q:
            self.calor = 1
        else:
            if sc == 0:
                a = random.randint(1,10)
                if a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
                    c = 1-sc
                else:
                    c = sc
                self.calor = c
            else:
                a = random.randint(1,10)
                if a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
                    c = 1-sc
                else:
                    c = sc
                self.calor = c

                
    def getCalor(self):
        return self.calor

    def setNegh(self,ng):
        self.negh = ng

    def getPos(self):
        return self.pos
