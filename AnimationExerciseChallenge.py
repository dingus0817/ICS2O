#File name: AnimationExerciseChallenge.py
#Description: This program animates a smiley that bounces around the screen
#Author: Jamie Zhang

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)

faceX = 400
faceY = 300
faceR = 50

eyeX1 = faceX - 25
eyeY1 = faceY - 10
eyeX2 = faceX + 25
eyeY2 = faceY - 10
smileX = faceX - 25
smileY = faceY + 5

shiftX = 5
shiftY = 5

while True:
    pygame.event.clear()
    surface.fill(WHITE)

    pygame.draw.circle(surface,YELLOW,(faceX,faceY),faceR,0)
    pygame.draw.circle(surface,BLACK,(eyeX1,eyeY1),5,0)
    pygame.draw.circle(surface,BLACK,(eyeX2,eyeY2),5,0)
    pygame.draw.arc(surface,BLACK,(smileX,smileY,50,30),3.14,6.28,3)
        
    pygame.display.update()
    pygame.time.delay(10)

    faceX = faceX + shiftX
    faceY = faceY + shiftY
    eyeX1 = faceX - 25
    eyeY1 = faceY - 10
    eyeX2 = faceX + 25
    eyeY2 = faceY - 10
    smileX = faceX - 25
    smileY = faceY + 5

    if (faceX > 750 or faceX < 50):
        shiftX = -shiftX
    if (faceY > 550 or faceY < 50):
        shiftY = -shiftY

pygame.quit()

