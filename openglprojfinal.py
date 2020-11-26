import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
print("Welcome to the Attractor Generator! The readme.txt explains how to use the program.\n")
import pygame
from pygame.locals import*
import time
import math
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
angle = 0.01
display = (1250,950)
color1 = [255/255, 0/255, 127/255]
color2 = [0, 255/255,0]
color3 = [51/255,204/255,204/255]

colors = [ color1, color2, color3
]
x = 0.01
y = 0
z = 0
randcol = [[1,1,1], [1,51/255,204/255], [204/255,51/255,255/255], [51/255,51/255,255/255], [51/255,153/255,255/255], [51/255,255/255,255/255], [51/255,255/255,102/255], [255/255,153/255,51/255], [255/255,255/255,51/255]]
def rossler(a = 0.2, b = 0.2, c = 5.7, colors = colors):
    x = 0.01
    y = 0
    z = 0
    #parameters of rossler attractor
    # a, b, and c are the variables that create a chaotic attractor
    
    dt = 0.01
    dx = 0
    dy = 0
    dz = 0
    count = 0
    while(count !=10000):        
        if(count >= 7500):
            glColor3d(colors[2][0], colors[2][1],colors[2][2])
        elif(count >= 5000):
            glColor3d(colors[1][0], colors[1][1], colors[1][2])
        else:
            glColor3d(colors[0][0],colors[0][1], colors[0][2])
        #formula for the three differential equations
        dx = (-(y+z)) * dt
        dy = (x + a*y) * dt
        dz = (b + z*(x-c)) * dt
        
        glVertex3d(x,y,z)
        
        x = x + dx
        y = y + dy
        z = z + dz
        count+=1
def lorenz(a = 10.0, b = 28, c = 8/3, colors = colors):
    x = 0.01
    y = 0
    z = 0
    # a = sigma
    # b = rho
    # c = beta
    count = 0
    dt = 0.01
    dx = 0
    dy = 0
    dz = 0
    while(count !=10000):        
        if(count >= 7500):
            glColor3d(colors[2][0], colors[2][1],colors[2][2])
        elif(count >= 5000):
            glColor3d(colors[1][0], colors[1][1], colors[1][2])
        else:
            glColor3d(colors[0][0],colors[0][1], colors[0][2])
        #differential equations
        dx = (a*(y - x)) * dt
        dy = (x*(b - z) - y) * dt
        dz = (x*y - c*z) * dt
        
        glVertex3d(x,y,z)
        
        x = x + dx
        y = y + dy
        z = z + dz
        count+=1


def fourwing(a = 0.3, b = 0.01, c = -0.4, colors = colors):
    x = 0.01
    y = 0
    z = 0
    count = 0
    dt = 0.01
    dx = 0
    dy = 0
    dz = 0
    while(count !=10000):        
        if(count >= 7500):
            glColor3d(colors[2][0], colors[2][1],colors[2][2])
        elif(count >= 5000):
            glColor3d(colors[1][0], colors[1][1], colors[1][2])
        else:
            glColor3d(colors[0][0],colors[0][1], colors[0][2])
        dx = (a*x + y*z) * dt
        dy = (b*x + c*y - x*z) * dt
        dz = (-z - x*y) * dt
        
        glVertex3d(x,y,z)
        
        x = x + dx
        y = y + dy
        z = z + dz
        count+=1 
def stringtoarr(string): 
    li = list(string.split(",")) 
    return li

        

    
choice = input("What would you like 1. Lorenz 2. Rössler 3. Four-Wing ")
if choice == "1":
    lorenzc = input("Would you like 1. normal 2. change inital conditions and color or 3. random? ")
    if lorenzc== "2":
        lorenz2 = input("What do you want sigma, rho, and beta to be? Please input the number as follows: a,b,c ")
        lorenzc1 = input("What colors would you like? The Attractor can be colored four times. enter as r,g,b \n color 1: ")
        lorenzc1 = stringtoarr(lorenzc1)
        lorenzc2 = input("color 2: ")
        lorenzc2 = stringtoarr(lorenzc2)
        lorenzc3 = input("color 3: ")
        lorenzc3 = stringtoarr(lorenzc3)
        lorenzc4 = input("color 4: ")
        lorenzc4 = stringtoarr(lorenzc4)
        lorenzcolor = [[int(lorenzc1[0])/255, int(lorenzc1[1])/255, int(lorenzc1[2])/255], [int(lorenzc2[0])/255, int(lorenzc2[1])/255, int(lorenzc2[2])/255], [int(lorenzc3[0])/255, int(lorenzc3[1])/255, int(lorenzc3[2])/255], [int(lorenzc4[0])/255, int(lorenzc4[1])/255, int(lorenzc4[2])/255]]
        lorenzuser = stringtoarr(lorenz2)
    if lorenzc == "3":
        lvalue1 = random.randint(12,50)
        lvalue2 = random.randint(4, 30)
        randcolorsl = [randcol[random.randint(0,8)],randcol[random.randint(0,8)],randcol[random.randint(0,8)] ]
if choice == "2":
    rosslerc = input("Would you like 1. normal 2. change inital conditions and color or 3. random? ")
    if rosslerc == "2":
        rosslerc2 = input("What do you want a, b, c to be. Please input the numbers as follows: a,b,c")
        rosslerc3 = input("What colors would you like? The attractor can be colored four times. enter as r,g,b \n color 1:")
        rosslerc3 = stringtoarr(rosslerc3)
        rosslerc4 = input("color 2: ")
        rosslerc4 = stringtoarr(rosslerc4)
        rosslerc5 = input("color 3: ")
        rosslerc5 = stringtoarr(rosslerc5)
        rosslerc6 = input("color 4: ") 
        rosslerc6 = stringtoarr(rosslerc6)
        rosslercolor = [[int(rosslerc3[0])/255, int(rosslerc3[1])/255, int(rosslerc3[2])/255 ],[int(rosslerc3[0])/255, int(rosslerc3[1])/255, int(rosslerc3[2])/255 ], [int(rosslerc3[0])/255, int(rosslerc3[1])/255, int(rosslerc3[2])/255 ], [int(rosslerc3[0])/255, int(rosslerc3[1])/255, int(rosslerc3[2])/255 ] ]   
        rossleruser = stringtoarr(rosslerc2)
    if rosslerc == "3":
        rvalue1 = round(random.uniform(0.2,0.5),2)
        rvalue2 = round(random.uniform(5, 20), 2)
        randcolorsr = [randcol[random.randint(0,8)],randcol[random.randint(0,8)],randcol[random.randint(0,8)] ]
if choice == "3":
    fourwingc = input("Would you like 1. normal 2. change inital conditions and color or 3. random? ")
    if fourwingc == "2":
        fourwingc1 = input("What do you want a, b, c to be. Please input the numbers as follows: a,b,c ")
        fourwingc2 = input("What colors would you like? The attractor can be colored four times. enter as r,g,b \n color 1: ")
        fourwingc2 = stringtoarr(fourwingc2)
        fourwingc3 = input("color 2: ")
        fourwingc3 = stringtoarr(fourwingc3)
        fourwingc4 = input("color 3: ")
        fourwingc4 = stringtoarr(fourwingc4)
        fourwingc5 = input("color 4: ")
        fourwingc5 = stringtoarr(fourwingc5)
        fourwingcolor = [[int(fourwingc2[0])/255, int(fourwingc2[1])/255, int(fourwingc2[2])/255 ], [int(fourwingc3[0])/255, int(fourwingc3[1])/255, int(fourwingc3[2])/255 ],[int(fourwingc4[0])/255, int(fourwingc4[1])/255, int(fourwingc4[2])/255 ], [int(fourwingc5[0])/255, int(fourwingc5[1])/255, int(fourwingc5[2])/255 ] ]
        fourwinguser = stringtoarr(fourwingc1)
    if fourwingc == "3":
        fvalues1 = round(random.uniform(0.15,0.5),2)
        fvalues = round(random.uniform(-0.2,0.4),2)
        randcolorsf = [randcol[random.randint(0,8)],randcol[random.randint(0,8)],randcol[random.randint(0,8)] ]
    

  
def main():
    pygame.init()
    pygame.display.set_caption('Attractor Generator')


    
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45,(display[0]/display[1]), 0.1, 1500)

    glVertex3d(0, 0, -1)

    glTranslatef(0,0,-100)
    
    clock = pygame.time.Clock()
    
    while (True) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        clock.tick(70)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glTranslatef(2,0,0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(-2,0,0)
            if event.key == pygame.K_UP:
                glTranslatef(0,-2,0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0,2,0)
            if event.key == pygame.K_CAPSLOCK:
                glTranslatef(0,0,-2)
            if event.key == pygame.K_LSHIFT:
                glTranslatef(0,0,2)
            if event.key == pygame.K_RSHIFT:
                glRotatef(1,0,1,0)
            

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            
        glEnable(GL_POINT_SMOOTH)
        glPointSize(1)
        
        glBegin(GL_POINTS)
    
        if choice == "1":
            if lorenzc == "1":
                lorenz()
            if lorenzc == "2":
                lorenz(float(lorenzuser[0]),float(lorenzuser[1]),float(lorenzuser[2]),lorenzcolor)
            if lorenzc == "3":
                lorenz(a = lvalue2,b = lvalue1, c = 8/3, colors = randcolorsl)
            

                
        if choice == "2":
            if rosslerc == "1":
                rossler()
            if rosslerc == "2":
                rossler(float(rossleruser[0]), float(rossleruser[1]), float(rossleruser[2]), rosslercolor )
            if rosslerc == "3":
                rossler(a = rvalue1, b = 0.2, c = rvalue2, colors = randcolorsr)
        
        if choice == "3":
            if fourwingc == "1":
                fourwing()
            if fourwingc == "2":
                fourwing(float(fourwinguser[0]),float(fourwinguser[1]), float(fourwinguser[2]) ,fourwingcolor )
            if fourwingc == "3":
                fourwing(a = fvalues1, b = 0.01, c = fvalues, colors = randcolorsf)




        glEnd()
        
        pygame.display.flip()


main()