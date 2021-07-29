import pygame
import sys
import random
import time
from creatureCl import Creature

cal = [(0,0,255), (255,0,0)]

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
for x in range(L,R,8):
    colomn = []
    for y in range(T,B,8):
        a = random.randint(0,1)
        if a == 0:
            c = 0
        else:
            c = 1
        colomn.append(Creature([],c,(x,y)))
        pp(x,y,c)
        pygame.display.flip()
    Popul.append(colomn)

W = len(Popul)
H = len(Popul)
for i in range(W):
    for j in range(H):
        ng = []
        if i != 0:
            ng.append(Popul[i-1][j])
        if j != 0:
            ng.append(Popul[i][j-1])
        if i != W-1:
            ng.append(Popul[i+1][j])
        if j != H-1:
            ng.append(Popul[i][j+1])
            
        Popul[i][j].setNegh(ng)
        
def randChangeCalor():
    global Popul
    i = random.randint(0,W-1)
    j = random.randint(0,H-1)
    creat = Popul[i][j]
    creat.changeCalor2()
    pos = creat.getPos()
    cl = creat.getCalor()
    x = pos[0]
    y = pos[1]
    pp(x,y,cl)
    pygame.display.flip()

running = flag = True
sec = 0.001

while running:
    time.sleep(sec)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = not flag
    if not flag:
        randChangeCalor()
    ##========================
    
pygame.quit()
