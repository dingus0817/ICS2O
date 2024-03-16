#File name: AnimationExerciseQ9.py
#Description: This program animates a crescent moon rising into the night sky
#Author: Jamie Zhang

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)

moonX = 700
moonY = 660
darkX = 730
darkY = 660

shiftX = 4
shiftY = 5

while True:
    pygame.event.clear()
    surface.fill(BLACK)
    pygame.draw.circle(surface,WHITE,(moonX,moonY),60,0)
    pygame.draw.circle(surface,BLACK,(darkX,darkY),50,0)
        
    pygame.display.update()
    pygame.time.delay(30)

    moonX = moonX - shiftX
    moonY = moonY - shiftY
    darkX = darkX - shiftX
    darkY = darkY - shiftY

    if (moonY == 200):
        moonX = moonX + shiftX
        moonY = moonY + shiftY
        darkX = darkX + shiftX
        darkY = darkY + shiftY
        
pygame.quit()
