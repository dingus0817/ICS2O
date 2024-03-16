#File name: AnimationExerciseQ1.py
#Description: This program moves a square from the right side to the left
#Author: Jamie Zhang

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
PINK = (255,183,224)

boxX = 800
boxY = 250

shiftX = 5

while True:
    pygame.event.clear()
    surface.fill(WHITE)
    pygame.draw.rect(surface,PINK,(boxX,boxY,50,50),0)
    pygame.display.update()
    pygame.time.delay(10)
    boxX = boxX - shiftX
    if boxX < 0:
        boxX = boxX + shiftX
pygame.quit()
