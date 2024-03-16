#File name: AnimationExerciseQ4.py
#Description: This program animates a light being turned on and off in a house
#Author: Jamie Zhang

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (124,200,124)
BLUE = (56,52,133)
BROWN = (133,94,66)
DARK_BROWN = (89,36,4)
ORANGE = (255,119,0)
YELLOW = (255,183,11)
GREY = (103,108,112)


while True:
    pygame.event.clear()
    surface.fill(BLUE)
    # moon and stars
    pygame.draw.circle(surface,WHITE,(650,100),100,0)
    pygame.draw.circle(surface,WHITE,(30,80),5,0)
    pygame.draw.circle(surface,WHITE,(150,140),5,0)
    pygame.draw.circle(surface,WHITE,(270,50),5,0)
    pygame.draw.circle(surface,WHITE,(430,100),5,0)
    # grass
    pygame.draw.rect(surface, GREEN, (0,380,800,220),0)
    # trees
    pygame.draw.polygon(surface, BLACK, ((100,125),(50,350),(150,350)),0)
    pygame.draw.line(surface, BLACK, (100,350),(100,380),30)
    pygame.draw.polygon(surface, BLACK, ((200,125),(150,350),(250,350)),0)
    pygame.draw.line(surface, BLACK, (200,350),(200,380),30)
    pygame.draw.polygon(surface, BLACK, ((300,125),(250,350),(350,350)),0)
    pygame.draw.line(surface, BLACK, (300,350),(300,380),30)
    pygame.draw.polygon(surface, BLACK, ((400,125),(350,350),(450,350)),0)
    pygame.draw.line(surface, BLACK, (400,350),(400,380),30)
    pygame.draw.polygon(surface, BLACK, ((700,125),(650,350),(750,350)),0)
    pygame.draw.line(surface, BLACK, (700,350),(700,380),30)
    # house
    pygame.draw.polygon(surface, BROWN, ((380,200),(520,150),(680,200),(680,400),(380,400)),0) 
    pygame.draw.polygon(surface, BROWN, ((680,200),(710,180),(710,380),(680,400)),0)
    # roof
    pygame.draw.polygon(surface, DARK_BROWN, ((520,150),(700,220),(775,205),(570,130)),0)
    pygame.draw.polygon(surface, DARK_BROWN, ((520,150),(380,200),(380,210),(330,210),(560,128),(570,130)),0)
    # wood texture
    pygame.draw.line(surface, DARK_BROWN, (380,200),(680,200),2)
    pygame.draw.line(surface, DARK_BROWN, (380,250),(680,250),2)
    pygame.draw.line(surface, DARK_BROWN, (380,300),(680,300),2)
    pygame.draw.line(surface, DARK_BROWN, (380,350),(680,350),2)
    # pillars
    pygame.draw.line(surface, DARK_BROWN, (382,200),(382,400), 20)
    pygame.draw.line(surface, DARK_BROWN, (678,200),(678,400), 20)
    # door and windows
    pygame.draw.rect(surface, DARK_BROWN, (450,300,70,100),0)
    pygame.draw.rect(surface, WHITE, (550,300,70,70),0)
    pygame.draw.circle(surface, WHITE, (520,220),30,0)
    # shadows
    pygame.draw.polygon(surface,GREY,((380,400),(300,430),(380,450),(600,430),(680,400)),0)
    pygame.draw.polygon(surface,GREY,((85,380),(115,380),(0,460)),0)
    pygame.draw.polygon(surface,GREY,((185,380),(215,380),(100,460)),0)
    pygame.draw.polygon(surface,GREY,((285,380),(315,380),(200,460)),0)
    # campfire
    pygame.draw.circle(surface,ORANGE,(250,500),40,0)
    pygame.draw.polygon(surface,ORANGE,((210,500),(290,500),(250,350)),0)
    pygame.draw.circle(surface,YELLOW,(250,530),30,0)
    pygame.draw.polygon(surface,YELLOW,((220,530),(280,530),(250,450)),0)
    pygame.draw.polygon(surface,BROWN,((200,505),(260,525),(260,545),(190,520)),0)
    pygame.draw.polygon(surface,BROWN,((300,505),(240,525),(240,545),(310,520)),0)
    pygame.draw.circle(surface,GREY,(210,540),20,0)
    pygame.draw.circle(surface,GREY,(250,550),20,0)
    pygame.draw.circle(surface,GREY,(290,540),20,0)
        
    pygame.display.update()
    pygame.time.delay(1000)

    pygame.draw.rect(surface, BLACK, (550,300,70,70),0)
    pygame.display.update()
    pygame.time.delay(1000)
    
    
    
pygame.quit()
