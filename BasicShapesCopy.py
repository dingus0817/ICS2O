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
# my custom colours
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
                               
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
while True:
    gameWindow.fill(WHITE)
    pygame.draw.line(gameWindow, BLUE, (0,0), (300,300), 20)
    pygame.draw.rect(gameWindow, GREEN, (200,50,200,100), 1)
    pygame.draw.circle(gameWindow, RED, (320, 240), 20, 2)
    pygame.draw.ellipse(gameWindow, RED, (100,350,200,100), 5)
    pygame.draw.arc(gameWindow, BLUE, (100,350,200,100),0, 3.14, 10)
    #-----------------------------------#

    # try some drawings here
    pygame.draw.line(gameWindow, ORANGE, (0, 800), (600,0), 10)
    pygame.draw.rect(gameWindow, PINK, (300, 200, 300, 200), 5)
    pygame.draw.circle(gameWindow, PURPLE, (400, 300), 100, 5)
    pygame.draw.ellipse(gameWindow, CYAN, (600, 400, 100, 50), 4)
    pygame.draw.arc(gameWindow, BLUE, (400, 250, 300, 550), 0, 3.14, 10)

    #-----------------------------------#
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings
    pygame.event.clear()

    
