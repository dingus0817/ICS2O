from math import sqrt                   # only sqrt function is needed from the math module
from random import randint              # only randint function is needed from the random module

import pygame
pygame.init()
WIDTH = 800
HEIGHT= 600
TOP = 0
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
GREEN = (0,255,0)
outline=0

font = pygame.font.SysFont("Arial",30)

#---------------------------------------#
# functions                             #
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def drawMessages():
    poppedText=font.render("Balloons popped: " + str(popped),1,WHITE)
    gameWindow.blit(poppedText,(0,0))
    timeText = font.render(str(round(elapsed/1000)) + " seconds",1,WHITE)
    gameWindow.blit(timeText,(0,35))
    

def redrawGameWindow():
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow,GREEN,(0,400,800,200),outline)
    for count in range(numBalloons):
        if notPopped[count]:
            pygame.draw.circle(gameWindow, balloonCLR[count], (balloonX[count], balloonY[count]), balloonR[count], outline)
    drawMessages()
    pygame.display.update()
     
#---------------------------------------#
# main program                          #
#---------------------------------------#
numBalloons = 20
balloonX = []
balloonY = []
balloonR = []
balloonSPEED = []
balloonCLR = []
notPopped = []

for count in range(numBalloons):
    balloonX.append(randint(0,WIDTH))
    balloonY.append(randint(HEIGHT//2,HEIGHT))
    balloonR.append(randint(20,50))
    balloonSPEED.append(randint(1,5))
    randomCLR =(randint(50,255),randint(50,255),randint(50,255))
    balloonCLR.append(randomCLR)
    notPopped.append(True)
    
popped = 0
flownAway = 0
BEGIN = pygame.time.get_ticks()
elapsed = 0
clock = pygame.time.Clock()
FPS = 24

inPlay = True
while inPlay and (flownAway + popped < numBalloons):
    redrawGameWindow()
    clock.tick(FPS)
    elapsed = pygame.time.get_ticks() - BEGIN
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:           
                inPlay = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            (cursorX,cursorY)=pygame.mouse.get_pos()
            for count in range(numBalloons):
                if notPopped[count] and distance(cursorX, cursorY, balloonX[count], balloonY[count]) < balloonR[count]:
                    notPopped[count] = False
                    popped = popped + 1
        
# move the balloon up
    for count in range(numBalloons):
        balloonY[count] = balloonY[count] - balloonSPEED[count]
        if notPopped[count] and (balloonY[count] < TOP - balloonR[count]):
            flownAway = flownAway + 1
            notPopped[count] = False

#---------------------------------------#    
pygame.quit()

print("Game Over!")
print("Time:", round(elapsed/1000), "seconds")
print("Score:", popped)
print("Flown away:", flownAway)

##from math import sqrt
##from random import randint
##
##import pygame
##pygame.init()
##WIDTH = 800
##HEIGHT= 600
##TOP = 0
##gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))
##
##WHITE = (255,255,255)
##GREEN = (  0,255,  0)
##BLACK = (  0,  0,  0)
##outline=0
##font = pygame.font.SysFont("Courier New Bold",36)
##
###---------------------------------------#
### functions                             #
###---------------------------------------#
##def distance(x1, y1, x2, y2):
##    return sqrt((x1-x2)**2 + (y1-y2)**2)
##
##def drawMessages():
##    elapsedGraphics = font.render(str(round(elapsed/1000.0,1)),1,GREEN)
##    poppedGraphics = font.render("popped: "+str(popped),1,GREEN)
##    flownAwayGraphics = font.render("flown away: "+str(flownAway),1,GREEN)
##    gameWindow.blit(elapsedGraphics,(100,100))
##    gameWindow.blit(poppedGraphics,(100,150))
##    gameWindow.blit(flownAwayGraphics,(100,200))    
##
##def redrawGameWindow():
##    gameWindow.fill(BLACK)
##    pygame.draw.rect(gameWindow, GREEN, (0,HEIGHT*0.66, WIDTH,HEIGHT), outline)
##    for i in range(numBalloons):
##        if balloonVisible[i]:
##            pygame.draw.circle(gameWindow, baloonCLR[i], (baloonX[i], baloonY[i]), baloonR[i], outline)
##    drawMessages()
##    pygame.display.update()
##    
###---------------------------------------#
### main program                          #
###---------------------------------------#
##numBalloons = 20
##baloonX = []
##baloonY = []
##baloonR = []
##baloonSPEED = []
##baloonCLR=[]
##balloonVisible = []
##
##for i in range(numBalloons):            # generate the balloons
##    baloonX.append(randint(0, WIDTH))
##    baloonY.append(randint(HEIGHT/2, HEIGHT))
##    baloonR.append(randint(20,50))
##    baloonSPEED.append(randint(1,5))
##    baloonCLR.append((randint(0,255), randint(0,255), randint(0,255)))
##    balloonVisible.append(True)
##
##flownAway = 0    
##popped = 0
##BEGIN = pygame.time.get_ticks()
##elapsed = 0
##clock = pygame.time.Clock()
##FPS = 24
##
##inPlay = True
##while inPlay and (popped+flownAway < numBalloons):
##    redrawGameWindow()
##    clock.tick(FPS)
##    elapsed = pygame.time.get_ticks() - BEGIN
##
##    for event in pygame.event.get():
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_ESCAPE:           
##                inPlay = False
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            for i in range(numBalloons):
##                (cursorX,cursorY)=pygame.mouse.get_pos()
##                if balloonVisible[i] and distance(cursorX, cursorY, baloonX[i], baloonY[i])< baloonR[i]:
##                    balloonVisible[i] = 0
##                    popped = popped + 1
##
### move the balloons up
##    for i in range(numBalloons):
##        baloonY[i] = baloonY[i] - baloonSPEED[i]
##        if balloonVisible[i] and (baloonY[i]< TOP - baloonR[i]):
##            flownAway = flownAway + 1
##            balloonVisible[i] = False
##
###---------------------------------------#
##pygame.quit()
##
##print("Game Over!")
##print("time:",str(round(elapsed/1000.0,1)),"seconds")
##print("popped:",popped)
##print("flown away:",flownAway)
