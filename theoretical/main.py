import math
import pygame
import random
import csv
from pendulum import *
import statistics

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import math
import numpy as np

# matplotlib
style.use('fivethirtyeight')

STEPS = 70

# screen constants
WIDTH = 1000
HEIGHT = 1000

l = 0.00000001  # m^2
AREA = 0.6 / 100

fnetList = []

mass = 0.0002150  # mass, kg
k = 0.000292818221
# spring constant (N/m)
C = 1.0  #
P = 1.225  # Density of air

period = 2*math.pi * math.sqrt(mass/k)
freq = 1/period

print("period:", period)

print("frequency:", freq)

# Pendulum
# Arguments: initx, inity, mass, k , myC, myP, myA, STEPS
isStationary = False
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

for it in range(2000):
    time = 0

    pend = Pendulum(WIDTH // 2, HEIGHT // 2, mass, k, C, P, l, STEPS)
    pend.y = HEIGHT*(1/4)

    yvals = []
    timevals = []

    done = False
    while not done:
        if time > 200:
            done = True
            plt.scatter(timevals, yvals);
            plt.title(str(l))
            plt.savefig("plots/" + "it" + str(l) + ".png")
            plt.clf()
            l += 0.00000001
        for event in pygame.event.get():
            # Pressing E enters fractal generator mode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    print("for later")
            # if event.type == pygame.MOUSEBUTTONDOWN:
            # mx, my = event.pos
            # left click sets pendulum position
            # if event.button == 1:
            #    pend = Pendulum(mx, my, MASS, k, FRICTION, STEPS)
            # right click creates pendulum at mouse
            # if event.button == 2:
            #    magnets.append(Magnet(mx, my, STRENGTH))

            # if event.button == 3 and len(magnets) != 0:
            #    magnets.pop()

            if event.type == pygame.QUIT:
                done = True
        pend.update(WIDTH, HEIGHT, isStationary)

        yvals.append(pend.y)
        timevals.append(time)
        # if len(yvals) % 1000 == 0:

        with open("SAs/" + str(it) + ".csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([time, pend.y])

        screen.fill((255, 255, 255))
        # draw pendulum
        # print(int(pend.x),int(pend.y))
        pygame.draw.line(screen, (0, 0, 0), (WIDTH // 2, 0), (WIDTH // 2, pend.y), 5)
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(WIDTH // 2 - (l * 100) // 2, int(pend.y), l * 100, 10))
        # pygame.draw.circle(screen, (0, 0, 0), (int(pend.x),int(pend.y)),10)
        pygame.display.flip()
        clock.tick()
        print(time)
        time += clock.get_rawtime() / 1000

