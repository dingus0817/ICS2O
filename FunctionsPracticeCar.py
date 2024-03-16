import pygame                           
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

RED =(255,  0,  0)
GREEN =(  0,255,  0)
BROWN = (155,103,60)
WHITE =(255,255,255)
BLACK =(  0,  0,  0)

#---------------------------------------#
# functions                             #
#---------------------------------------#
def drawCar(carX,carY):
    pygame.draw.rect(gameWindow, RED, (carX,carY,200,50),0 )
    pygame.draw.rect(gameWindow, RED, (carX+30,carY-30,140,50),0)
    pygame.draw.circle(gameWindow, BLACK, (carX+50,carY+50),20,0)
    pygame.draw.circle(gameWindow, BLACK, (carX+150,carY+50),20,0)
def drawTree(treeX,treeY):
    pygame.draw.rect(gameWindow, BROWN,(treeX,treeY,30,200),0)
    pygame.draw.circle(gameWindow, GREEN,(treeX + 15,treeY+15),90,0)

#---------------------------------------#
# main program                          #
#---------------------------------------#
carX = WIDTH//2
carY = HEIGHT//2
shiftX = 5
inPlay = True

while inPlay:
    pygame.event.clear()    
    gameWindow.fill(WHITE)
    drawTree(WIDTH//1.7,HEIGHT//4)
    drawCar(carX,carY)
    drawTree(WIDTH//3,HEIGHT//3)
    pygame.display.update()
    pygame.time.delay(10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_LEFT]:
        carX = carX - shiftX
    if keys[pygame.K_RIGHT]:
        carX = carX + shiftX 

#---------------------------------------#
pygame.quit()
