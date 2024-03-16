#File name: AnimationExerciseQ2.py
#Description: This program animates a square so it
# exits from the left and enters from the right
#Author: Jamie Zhang


import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
PINK = (255,183,224)

boxS = 50
boxX = 800
boxY = 250

shiftX = 5
reset = boxX

while True:
    pygame.event.clear()
    surface.fill(WHITE)
    pygame.draw.rect(surface,PINK,(boxX,boxY,boxS,boxS),0)
    pygame.display.update()
    pygame.time.delay(10)
    boxX = boxX - shiftX
    if boxX == 0 - boxS:
        boxX = reset
pygame.quit()
