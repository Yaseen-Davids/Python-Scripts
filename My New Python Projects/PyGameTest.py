import pyautogui as py
import time
import random
import pygame
import sys
import keyboard
from pygame.locals import *
pygame.init()

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (92, 77, 90)
GREEN_1 = (46, 117, 52)
SKY = (72, 187, 219)
SUN = (247, 243, 12)


size = ((700, 500))
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GAME!")


carryOn = True

clock = pygame.time.Clock()

#- - - Main Program loop - - -#
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    screen.fill(WHITE)

    grass = pygame.draw.rect(screen, GREEN, [0, 350, 700, 400],0)
    sky = pygame.draw.rect(screen, SKY, [0, 0, 700, 350],0)
    sun = pygame.draw.ellipse(screen, SUN, [50, 50, 120, 100],0)
    tree_log = pygame.draw.rect(screen, BROWN, [500, 280, 30, 100],0)
    leaves = pygame.draw.ellipse(screen, GREEN_1, [475, 180, 80, 120],0)
    
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
