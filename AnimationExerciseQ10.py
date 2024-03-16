#File name: AnimationExerciseQ10.py
#Description: This program shows a happy face pop on and off the window at random locations
#Author: Jamie Zhang

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)

while True:
    pygame.event.clear()
    surface.fill(WHITE)
    from random import randint

    faceX = randint(0,WIDTH)
    faceY = randint(0,HEIGHT)

    eyeX1 = faceX - 25
    eyeY1 = faceY - 10
    eyeX2 = faceX + 25
    eyeY2 = faceY - 10
    smileX = faceX - 25
    smileY = faceY + 5
    
    pygame.draw.circle(surface,YELLOW,(faceX,faceY),50,0)
    pygame.draw.circle(surface,BLACK,(eyeX1,eyeY1),5,0)
    pygame.draw.circle(surface,BLACK,(eyeX2,eyeY2),5,0)
    pygame.draw.arc(surface,BLACK,(smileX,smileY,50,30),3.14,6.28,3)
        
    pygame.display.update()
    pygame.time.delay(1000)

    pygame.draw.circle(surface,WHITE,(faceX,faceY),50,0)
    pygame.display.update()
    pygame.time.delay(1000)

pygame.quit()
