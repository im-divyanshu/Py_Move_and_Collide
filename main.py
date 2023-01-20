import pygame
import random

scrx=800
scry=600
screen=pygame.display.set_mode((scrx,scry))
size=40
char=pygame.image.load("char.png")
char=pygame.transform.scale(char,(size,size))
col=pygame.image.load("sign.png")
col=pygame.transform.scale(col,(size,size))
up1=False
down1=False
left1=False
right1=False
dead=False
r=200
g=200
b=200
ic=True
icspeed=2
posx=375
posy=275
speed1=.2
x=random.randint(0,scrx-size)
y=random.randint(0,scry-size)
# function for changing the location
def collect(x,y):
    screen.blit(col,(x,y))
def player(x,y):
    screen.blit(char,(x,y))

# the collision system that I wrote loooks simple but to figure i out I spent a whole day
def iscollide(posx,posy,x,y):
    dead=False
    if(posx>x and posx-size<x):
        if(posy<y and posy+size>y):
            dead=True
    if(posy>y and posy-size<y):
        if(posx>x and posx-size<x):
            dead=True
    if(y>posy and y-size<posy):
        if(x>posx and x-size<posx):
            dead=True
    if(x>posx and x-size<posx):
        if(y<posy and y+size>posy):
            dead=True
    return dead
pygame.init()
opened=True
while opened:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            opened=False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_w):
                up1=True
                down1=False
            if(event.key==pygame.K_s):
                down1=True
                up1=False
            if(event.key==pygame.K_a):
                left1=True  
                right1=False
            if(event.key==pygame.K_d):
                right1=True
                left1=False
        if(event.type==pygame.KEYUP):
            if(event.key==pygame.K_w):
                up1=False
            if(event.key==pygame.K_s):
                down1=False
            if(event.key==pygame.K_a):
                left1=False
            if(event.key==pygame.K_d):
                right1=False
    
    screen.fill((r,g,b))
    # changing the position
    if(iscollide(posx,posy,x,y)):
        x=random.randint(0,scrx-size)
        y=random.randint(0,scry-size)
        dead=False
    if(iscollide(posx,posy,x,y)):
        pass
    else:
        if(up1):
            if(posy>0):
                posy-=speed1
        if(down1):
            if(posy<scry-size):
                posy+=speed1
        if(right1):
            if(posx<scrx-size):
                posx+=speed1
        if(left1):
            if(posx>0):
                posx-=speed1

    collect(x,y)
    player(posx,posy)

    pygame.display.update()