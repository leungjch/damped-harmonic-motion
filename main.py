import math
import pygame
import random
import csv
from pendulum import *
import statistics 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import numpy as np

# matplotlib
style.use('fivethirtyeight')

STEPS = 1000

# screen constants
WIDTH = 1000
HEIGHT = 1000

l = 0.10582
AREA = pow(l, 2)

fnetList = []

mass = 2.150      # mass, kg
k = 25.89249337
         # spring constant (N/m)
C = 1.28        # 
P = 1.225      # Density of air

# Pendulum
# Arguments: initx, inity, mass, k , myC, myP, myA, STEPS
pend = Pendulum(WIDTH//2, HEIGHT//2, mass, k, C, P, AREA, STEPS)
pend.y = (HEIGHT*3)//4
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

time = 0

isStationary = False
yvals = []
done = False
while not done:
    for event in pygame.event.get():
            # Pressing E enters fractal generator mode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                   print("for later")
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #mx, my = event.pos
                # left click sets pendulum position
                #if event.button == 1:
                #    pend = Pendulum(mx, my, MASS, k, FRICTION, STEPS)
                # right click creates pendulum at mouse
                #if event.button == 2:
                #    magnets.append(Magnet(mx, my, STRENGTH))

                #if event.button == 3 and len(magnets) != 0:
                #    magnets.pop()

            
            if event.type == pygame.QUIT:
                    done = True
    pend.update(WIDTH, HEIGHT, isStationary)

    
    yvals.append(pend.y)
    if len(yvals) % 1000 == 0: 
        plt.scatter(range(len(yvals)), yvals, marker='o');
        plt.savefig("plots/"+str(len(yvals))+".png")


    with open("position.csv","a") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow([time,pend.y])
    
    if (pend.y) < 1:
        with open("peaks.csv","a", newline = '') as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time,pend.y, 1])
    screen.fill((255,255,255))
    # draw pendulum
    #print(int(pend.x),int(pend.y))
    pygame.draw.line(screen, (0,0,0), (WIDTH//2, 0), (WIDTH//2, pend.y), 5)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH//2-(l*100)//2, int(pend.y), l*100, 10))
    #pygame.draw.circle(screen, (0, 0, 0), (int(pend.x),int(pend.y)),10)
    pygame.display.flip()
    clock.tick()
    time += clock.get_rawtime()/1000
    print(time)

