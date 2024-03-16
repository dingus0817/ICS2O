#File name: AnimationExerciseQ6-7.py
#Description: This program animates a side profile of a car driving in front of a tree
#Author: Jamie Zhang

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (135,206,235)
BROWN = (114,95,50)

carX1 = 800
carY1 = 300
carX2 = 900
carY2 = 250
carX3 = 1400
carY3 = 300
windowX1 = 920
windowY1 = 270
windowX2 = 1230
windowY2 = 270
tireX1 = 900
tireY1 = 350
tireX2 = 1400
tireY2 = 350

shiftX = 5

while True:
    pygame.event.clear()
    surface.fill(BLUE)
    # tree
    pygame.draw.circle(surface,GREEN,(615,240),80,0)
    pygame.draw.rect(surface,BROWN,(600,250,30,170),0)
    # car
    pygame.draw.rect(surface, RED, (carX1,carY1,100,50),0)
    pygame.draw.rect(surface, RED, (carX2,carY2,500,100),0)
    pygame.draw.rect(surface, RED, (carX3,carY3,100,50),0)
    # windows
    pygame.draw.rect(surface, WHITE, (windowX1,windowY1,100,50),0)
    pygame.draw.rect(surface, WHITE, (windowX2,windowY2,130,50),0)
    # tires
    pygame.draw.circle(surface,BLACK,(tireX1,tireY1),30,0)
    pygame.draw.circle(surface,BLACK,(tireX2,tireY2),30,0)
    # road/grass
    pygame.draw.rect(surface,BLACK,(0,370,WIDTH,230),0)
    pygame.draw.rect(surface,GREEN,(0,500,WIDTH,100),0)
    
    
    pygame.display.update()
    pygame.time.delay(15)

    carX1 = carX1 - shiftX
    carX2 = carX2 - shiftX
    carX3 = carX3 - shiftX
    windowX1 = windowX1 - shiftX
    windowX2 = windowX2 - shiftX
    tireX1 = tireX1 - shiftX
    tireX2 = tireX2 - shiftX 
    
pygame.quit()
    
    
