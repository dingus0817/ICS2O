#File name: BusinessCard.py
#Description: This program draws a design for a business card on pygame
#Author: Jamie Zhang

# ------------------------------------------------#
# Company description:
# My business, J.Scribbles, is designing and producing vinyl stickers
# Logo: Replicates a sticker, the heart represents creativity and passion,
# connects symbol of hearts and creativity with the business name in the logo
# Catchphrase: A sticker a day keeps the boredom away
# The target audience is mostly girls aged 13-20
# It will be seen and sold online and through e-commerce
# Stickers that will be produced include original works as well as requests
# or designs made by others
# -------------------------------------------------#

# initializing pygame
import pygame
pygame.init()
WIDTH = 1050
HEIGHT = 600
surface = pygame.display.set_mode((WIDTH,HEIGHT))

# colours
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
LILAC = (218,218,249)
BANANA = (255,249,191)
WISTERIA = (149,53,83)

# ----------------- main program starts 
while True:         
    # drawing background
    surface.fill(LILAC)
    pygame.draw.rect(surface, BANANA, (10,10,1030,580),20)
    # drawing logo
    pygame.draw.circle(surface, WHITE, (250,250),170,0)
    pygame.draw.circle(surface, BLACK, (250,250),160,2)
    font = pygame.font.SysFont("Ink Free",60)
    text = font.render("J.Scribbles",1,WISTERIA)
    surface.blit(text,(115,160))
    pygame.draw.arc(surface, WISTERIA, (180,250,70,70),0.523,3.49,5)
    pygame.draw.arc(surface, WISTERIA, (245,250,70,70),-0.349,2.79,5)
    pygame.draw.line(surface, WISTERIA, (185,300),(250,370),5)
    pygame.draw.line(surface, WISTERIA, (310,300),(250,370),5)
    # drawing catchphrase 
    pygame.draw.polygon(
        surface, WHITE,((110,430),(415,430),(415,485),(560,485),(560,530),
                        (90,530),(90,485),(110,485),(110,430)),0)
    font = pygame.font.SysFont("Segoe Script",35)
    text = font.render("a sticker a day",1,WISTERIA)
    surface.blit(text,(120,430))
    text = font.render("keeps the boredom away",1,WISTERIA)
    surface.blit(text,(100,480))
    font = pygame.font.SysFont("Ink Free",30)
    text = font.render("We believe that creativity inspires creativity",1,WISTERIA)
    surface.blit(text,(400,70))
    # rendering information
    font = pygame.font.SysFont("Segoe Script",40)
    text = font.render("sticker info:",1,WISTERIA)
    surface.blit(text,(600,130))
    pygame.draw.line(surface, WISTERIA, (500,180),(800,180),3)
    font = pygame.font.SysFont("Ink Free",30)
    text = font.render("- Vinyl",1,WISTERIA)
    surface.blit(text,(600,190))
    text = font.render("- Original artwork",1,WISTERIA)
    surface.blit(text,(600,230))
    text = font.render("- Requests",1,WISTERIA)
    surface.blit(text,(600,270))
    text = font.render("- Your own original artwork",1,WISTERIA)
    surface.blit(text,(600,310))
    # rendering contact info
    font = pygame.font.SysFont("Ink Free",40)
    text = font.render("CALL US AT: 416 439 0000",1,WISTERIA)
    surface.blit(text,(500,380))
    text = font.render("VISIT US AT:",1,WISTERIA)
    surface.blit(text,(500,430))
    text = font.render("www.jscribbles.ca",1,WISTERIA)
    surface.blit(text,(600,480))
    # drawing cat sticker 
    pygame.draw.ellipse(surface, WHITE, (370,240,190,140), 0)
    pygame.draw.polygon(surface, WHITE, ((500,300),(360,320),(410,200)),0)
    pygame.draw.polygon(surface, WHITE, ((430,300),(560,320),(520,200)),0)
    pygame.draw.ellipse(surface, GREY, (380,250,170,120), 0)
    pygame.draw.polygon(surface, GREY, ((480,300),(380,320),(410,210)),0)
    pygame.draw.polygon(surface, GREY, ((450,300),(550,320),(520,210)),0)
    pygame.draw.circle(surface, BLACK, (430,290),5,0)
    pygame.draw.circle(surface, BLACK, (500,290),5,0)
    pygame.draw.polygon(surface, BLACK, ((460,310),(470,310),(465,315)),0)
    pygame.draw.line(surface, BLACK, (420,315),(390,310),3)
    pygame.draw.line(surface, BLACK, (420,325),(390,325),3)
    pygame.draw.line(surface, BLACK, (510,315),(540,310),3)
    pygame.draw.line(surface, BLACK, (510,325),(540,325),3)

    pygame.display.update()      # --------- pygame is updated 
    pygame.event.clear()
# -----------------------------------------
pygame.quit()       
