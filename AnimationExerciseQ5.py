#File name: AnimationExerciseQ5.py
#Description: This program animates a stickman waving
#Author: Jamie Zhang


import pygame                           
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

RED  =(255,  0,  0)
GREEN=(  0,255,  0)
BLUE =(  0,  0,255)
CYAN =(  0,255,255)
WHITE=(255,255,255)
BLACK=(  0,  0,  0)
GREY =(128,128,128)
ORANGE = (255, 165, 0)
PEACH = (255, 203, 164)

handX = 480
handY = 100

shiftX = 1
shiftY = 4
                               
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
while True:
    pygame.event.clear()
    gameWindow.fill(WHITE)
    # head.
    pygame.draw.circle(gameWindow,PEACH,(320,80), 50, 1)
    # hair
    pygame.draw.rect(gameWindow, ORANGE, (270, 20, 100, 20)) 
    # left eye.
    pygame.draw.ellipse(gameWindow,GREY,(290,70,20,14), 7)
    # left pupil
    pygame.draw.circle(gameWindow, BLACK, (300, 77), 5)
    # left eye highlight
    pygame.draw.circle(gameWindow, WHITE, (298, 75), 3)
    # right eye.
    pygame.draw.ellipse(gameWindow,GREY,(330,70,20,14), 7)
    # right pupil
    pygame.draw.circle(gameWindow, BLACK, (340, 77), 5)
    # right eye highlight
    pygame.draw.circle(gameWindow, WHITE, (338, 75), 3)
    # mouth.
    pygame.draw.arc(gameWindow,GREY,(290, 85, 60, 30), 3.9, 0, 5)
    # body.
    pygame.draw.rect(gameWindow,ORANGE,(300, 130, 40, 200), 1)
    # left arm.
    pygame.draw.line(gameWindow,PEACH,(300,130),(250,250), 1)
    # right arm.
    pygame.draw.line(gameWindow,PEACH,(340,130),(handX,handY), 1)
    # left hand.
    pygame.draw.circle(gameWindow,PEACH,(250,250),10, 1)
    # right hand.
    pygame.draw.circle(gameWindow,PEACH,(handX,handY),10, 1)
    # left leg.
    pygame.draw.line(gameWindow,BLACK,(300,330),(250,430), 1)
    # right  leg
    pygame.draw.line(gameWindow,BLACK,(340,330),(390,430), 1)
    # left foot.
    pygame.draw.rect(gameWindow,GREEN,(225,430,25,20), 1)
    # right foot.
    pygame.draw.rect(gameWindow,GREEN,(390,430,25,20), 1)
    
    pygame.display.update()
    pygame.time.delay(20)

    handX = handX + shiftX
    handY = handY + shiftY

    if  handX < 480 or handX > 500:
        shiftX = -shiftX
    if handY < 85 or handY > 160:
        shiftY = -shiftY
    
pygame.quit()
