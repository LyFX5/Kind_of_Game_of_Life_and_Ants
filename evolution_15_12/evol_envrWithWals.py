import pygame
import sys
import random
import time
from cretureGoFarword import Creature

cal = [(255,255,255), (255,0,0), (0,0,0)]

def pp(x,y,c):
    return pygame.draw.circle(screen, cal[c], [x, y], 4, 0)


pygame.init()
screen = pygame.display.set_mode([700, 500])
screen.fill([250, 250, 250])

Popul = []
L = 10
T = 10
R = 450
B = 450
X = []
Y = []
for x in range(10,450,8):
    X.append(x)
    colomn = []
    for y in range(10,450,8):
        Y.append(y)
        if x == 226 and y > 350:
            colomn.append(Creature([],2,[x,y],[]))
            pp(x,y,2)
            pygame.display.flip()
            
        elif y == 450-8 and x < 226:
            c = random.randint(0,1)
            colomn.append(Creature([],c,[x,y],[]))
            pp(x,y,c)
            pygame.display.flip()
            
        else:
            colomn.append(Creature([],0,[x,y],[]))
            pp(x,y,0)
            pygame.display.flip()
            
    Popul.append(colomn)
    
W = len(Popul)
H = len(Popul)

def setState():
    global Popul, X, Y, W, H
    for i in range(W):
        for j in range(H):
            cr = Popul[i][j]
            if cr.getCalor() == 1:
                sx = X[i]
                sy = Y[j]
                pp(sx,sy,0)
                x = cr.getPos()[0]
                y = cr.getPos()[1]
                pp(x,y,1)
                pygame.display.flip()
                cr2 = Popul[X.index(x)][Y.index(y)]
                Popul[X.index(x)][Y.index(y)] = cr
                Popul[i][j] = cr2
    for i in range(W):
        for j in range(H):
            if Popul[i][j].getCalor() == 1:
                ng = [0,0,0,0]
                if i != 0:
                    ng[0] = (Popul[i-1][j])
                    
                if j != 0:
                    ng[1] = (Popul[i][j-1])
                    
                if i != W-1:
                    ng[2] = (Popul[i+1][j])

                if j != H-1:
                    ng[3] = (Popul[i][j+1]) ##  ===  ??

                Popul[i][j].setNegh(ng)
                cr = Popul[i][j]
                top = cr.getNegh()[1]
                if top != 0:
                    if top.getCalor() == 1:
                        onm = []
                        onm.append(top)
                        for t in top.getOnMe():
                            onm.append(t)
                            
                        Popul[i][j].setOnMe(onm)
                    else:
                        Popul[i][j].setOnMe([])
                        
print(H)
setState()
for i in range(W):
    for j in range(H):
        if Popul[i][j].calor == 1:
            for n in Popul[i][j].getNegh():
                if type(n) == int:
                    print(n,end='')
                else:
                    print(n.getCalor(),end='')
                    print("ob",end='')
                print(" ",end='')
            print(Popul[i][j].getPos())
# ??? проверить??? нужно сделать так чтобы даже если он пришел не с прыжка то всеравно становился onMe
def randChangeCalor():
    global Popul
    W = len(Popul)
    H = len(Popul)
    i = random.randint(0,W-1)
    j = random.randint(30,H-1)
    creat = Popul[i][j]
    if creat.getCalor() == 1:
        if creat.getPos()[0] == 442:
            print("They WIN")
            pp(442,creat.getPos()[1],2)
            return True
        else:
            creat.move()
            setState()
            for i in range(W):
                for j in range(H):
                    if Popul[i][j].calor == 1:
                        for n in Popul[i][j].getNegh():
                            if type(n) == int:
                                print(n,end='')
                            else:
                                print(n.getCalor(),end='')
                                print("ob",end='')
                            print(" ",end='')
                        print(Popul[i][j].getPos())
            print()
    return False

running = flag = True
sec = 0.00001

while running:
    time.sleep(sec)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = not flag
    if not flag:
        #pass
        flag = randChangeCalor()
    ##========================
    
pygame.quit()


