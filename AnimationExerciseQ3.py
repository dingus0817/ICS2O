#File name: AnimationExerciseQ3.py
#Description: This program writes a scrolling message from left to right
#Author: Jamie Zhang


import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLUE = (0,0,255)

textL = 0
textStart = 0
textX = -200
textY = 270
font = pygame.font.SysFont("Courier New Bold",60)

shiftX = 5

while True:
    pygame.event.clear()
    surface.fill(WHITE)
    text = font.render("it's muffin time",1,BLUE)
    surface.blit(text,(textX,textY))
    pygame.display.update()
    pygame.time.delay(10)
    textX = textX + shiftX
    if textX > WIDTH:
        textX = textX - shiftX
pygame.quit()
    
