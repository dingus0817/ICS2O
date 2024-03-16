
import pygame

color_dict = {
    'red':(255,0,0),
    'orange':(255,165,0),
    'yellow':(255,200,40),
    'green':(0,255,0),
    'blue':(0,0,255),
    'purple':(255,0,255),
    'white':(255,255,255),
    'black':(0,0,0)
    }

def validateColour(colour):
    '''validate colour'''
    color = colour
    validColour = False
    if color in color_dict:
        validColour = True
    else:
        print("you must enter a valid colour")
    return validColour

print("\ntoday we're going to draw a house!")
validColour = False
buildingColour = ""
roofColour = ""
while not validColour:
    buildingColour = input("enter the colour of the house (red, orange, yellow, green, blue, purple, white): ")
    validColour = validateColour(buildingColour)

validColour = False
while not validColour:
    roofColour = input("enter the colour of the roof (red, orange, yellow, green, blue, purple, white): ")
    validColour = validateColour(roofColour)
    
numWindow = int(input("enter the number of windows (min: 1, max: 3): "))
numGarage = int(input("enter the number of garages (min: 0, max: 2): "))

pygame.init()
screenInfo = pygame.display.Info()
W = 1000 
H = 600
screen = pygame.display.set_mode((W,H))

def drawBuilding(x,y,width,height):
    pygame.draw.rect(screen, color_dict[buildingColour],(x,y,width,height),0)

def drawRoof(a,b,c,d,e,f):
    pygame.draw.polygon(screen,color_dict[roofColour],((a,b),(c,d),(e,f)),0)

def drawWindow(x,y,width,height):
    pygame.draw.rect(screen,color_dict['white'],(x,y,width,height),0)
    pygame.draw.rect(screen,color_dict['black'],(x,y,width,height),5)

def drawDoor(x,y,width,height):
    pygame.draw.rect(screen,color_dict['black'],(x,y,width,height),0)

def drawGarage(x,y,width,height):
    pygame.draw.rect(screen,building_colour(buildingColour),(x,y,width,height),0)
    pygame.draw.rect(screen,color_dict['black'],(x,y,width,height),5)

running = True
while running:
    pygame.event.pump()
    screen.fill(color_dict['black'])
    drawBuilding(100,300,400,300)
    drawRoof(80,300,520,300,300,150)
    drawWindow(370,450,70,70)
    drawDoor(170,450,70,150)

    if numWindow == 2:
        drawWindow(370,320,70,70)
    elif numWindow == 3:
        drawWindow(370,320,70,70)
        drawWindow(170,320,70,70)

    if numGarage == 1:
        drawGarage(500,380,220,220)
    elif numGarage == 2:
        drawGarage(500,380,220,220)
        drawGarage(720,380,220,220)
    
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False


pygame.quit()
