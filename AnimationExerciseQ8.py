#File name: AnimationExerciseQ8.py
#Description: This program animates a rocket blasting off the top of the screen into space
#Author: Jamie Zhang

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
#ORANGE = (255,165,0)

rocketX1 = 200
rocketY1 = 500
rocketX2 = 200
rocketY2 = 500
rocketX3 = 230
rocketY3 = 500
rocketX4 = 215
rocketY4 = 470
fireX1 = 200
fireY1 = 600
fireX2 = 230
fireY2 = 600
fireX3 = 215
fireY3 = 680

shiftY = 5


while True:
    pygame.event.clear()
    surface.fill(WHITE)
    pygame.draw.rect(surface,BLACK,(rocketX1,rocketY1,30,100),0)
    pygame.draw.polygon(surface,BLACK,(
        (rocketX2,rocketY2),(rocketX3,rocketY3),(rocketX4,rocketY4)),0)
    pygame.draw.polygon(surface,YELLOW,(
        (fireX1,fireY1),(fireX2,fireY2),(fireX3,fireY3)),0)
    
    pygame.display.update()
    pygame.time.delay(10)

    rocketY1 = rocketY1 - shiftY
    rocketY2 = rocketY2 - shiftY
    rocketY3 = rocketY3 - shiftY
    rocketY4 = rocketY4 - shiftY
    fireY1 = fireY1 - shiftY
    fireY2 = fireY2 - shiftY
    fireY3 = fireY3 - shiftY

    if (fireY3 < 0):
        rocketY1 = rocketY1 + shiftY
        rocketY2 = rocketY2 + shiftY
        rocketY3 = rocketY3 + shiftY
        rocketY4 = rocketY4 + shiftY
        fireY1 = fireY1 + shiftY
        fireY2 = fireY2 + shiftY
        fireY3 = fireY3 + shiftY
    
pygame.quit()
