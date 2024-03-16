#File name: PongGraphics.py
#Author: Jamie Zhang

import pygame
import time
pygame.init()
screenInfo = pygame.display.Info()
WIDTH = screenInfo.current_w 
HEIGHT = screenInfo.current_h
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# loaded images
tennis = pygame.image.load("pongTennis.png")
tennis = pygame.transform.scale(tennis,(WIDTH,HEIGHT))
selectBox = pygame.image.load("selectBox.png")
woodPlank = pygame.image.load("pongWoodPlank.png")
woodPlank = pygame.transform.scale(woodPlank,(WIDTH//4,HEIGHT//4))
sunny = pygame.image.load("pongSunny.png")
sunny = pygame.transform.scale(sunny,(WIDTH,HEIGHT))
beach = pygame.image.load("pongBeach.png")
beach = pygame.transform.scale(beach,(WIDTH,HEIGHT))
volcano = pygame.image.load("pongVolcano.png")
volcano = pygame.transform.scale(volcano,(WIDTH,HEIGHT))
sky = pygame.image.load("pongSky.png")
sky = pygame.transform.scale(sky,(WIDTH,HEIGHT))
foot = pygame.image.load("pongFoot.png")
foot = pygame.transform.scale(foot,(WIDTH,HEIGHT))

pygame.mixer.music.load("wiiSportsThemeLoop.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops = -1)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)

#Classes
class Option: #Create a class for text options

    hovered = False #Is mouse over this button?
    
    def __init__(self, text, pos): #Initialize properties
        self.text = text
        self.pos = pos
        self.set_rect() #Method below
        self.draw() #Draw button
            
    def draw(self):
        self.set_rend() #Method below
        screen.blit(self.rend, self.rect) #Overlay button onto screen
        
    def set_rend(self):
        self.rend = clickFONT.render(self.text, True, self.get_color()) #Render text
        
        
    def get_color(self): #Check if colour should be white or grey, depending if mouse is hovering or not
        if self.hovered:
            return (RED) #White if mouse over
        else:
            return (BLUE) #Grey otherwise
        
    def set_rect(self):
        self.set_rend() #Method above
        self.rect = self.rend.get_rect() #Get the rect object properties from button
        self.rect.topleft = self.pos #Set position of rect object to own position
                  
# fonts used
clickFONT = pygame.font.SysFont("Courier New",int(WIDTH//19.2))
titleFont = pygame.font.SysFont("Times", int(WIDTH//10))
regularFont = pygame.font.SysFont("Times",int(WIDTH//18))

# lists of clickable text
startOptions = [(Option("PLAY", (WIDTH//2.28,HEIGHT//1.8))),(Option("SETTINGS", (WIDTH//2.66,HEIGHT//1.35)))] #Define all game buttons
settingsOptions = [
    Option("EASY",(WIDTH//10,HEIGHT//5)),(
        Option("MEDIUM",(WIDTH//10,HEIGHT//3.33))),(
            Option("HARD",(WIDTH//10,HEIGHT//2.5))),(
                Option("DEFAULT",(WIDTH//80,HEIGHT//1.5))),(
                    Option("BEACH",(WIDTH//3.8,HEIGHT//1.5))),(
                        Option("VOLCANO",(WIDTH//2.2,HEIGHT//1.5))),(
                            Option("SKY",(WIDTH//1.4,HEIGHT//1.5))),(
                                Option("FOOT",(WIDTH//1.2,HEIGHT//1.5))),(
                                    Option("<-- MAIN MENU",(WIDTH//50,HEIGHT//1.1)))]
speedSelectPos = [(WIDTH//10,HEIGHT//5),(WIDTH//10,HEIGHT//3.33),(WIDTH//10,HEIGHT//2.5)]
backgroundSelectPos = [
    (WIDTH//80,HEIGHT//1.5),(
        WIDTH//3.8,HEIGHT//1.5),(
            WIDTH//2.2,HEIGHT//1.5),(
                WIDTH//1.4,HEIGHT//1.5),(
                    WIDTH//1.2,HEIGHT//1.5)]
doneButton = [Option("DONE",(WIDTH//1.6,HEIGHT//1.5))]
postGameOptions = [Option("PLAY AGAIN",(WIDTH//10,HEIGHT//1.7)),Option("MAIN MENU",(WIDTH//1.6,HEIGHT//1.7))]

# determining the select box position and dimensions
defaultSpeed = speedSelectPos[1]
defaultSpeedWidth = settingsOptions[1].rend.get_rect()[2]
defaultSpeedHeight = settingsOptions[1].rend.get_rect()[3]
defaultBackground = backgroundSelectPos[0]
defaultBackgroundW = settingsOptions[3].rend.get_rect()[2]
defaultBackgroundH = settingsOptions[3].rend.get_rect()[3]

# determining the background
chosenBackground = sunny

# remembering player names
player1Text = ""
player2Text = ""
name1 = regularFont.render(player1Text,1,(RED))
name2 = regularFont.render(player2Text,1,(BLUE))

winningScore = 7

running = True
inStart = True
inSettings = False
inPlay = False
inPlayer1 = False
inPlayer2 = False
inGame = False
postGame = False

while running:
    while inStart:
        pygame.event.pump() #Ensure all events are current
        screen.blit(tennis,(0,0))
        textTitle = titleFont.render("PONG FOR TWO",1,WHITE)
        screen.blit(textTitle,(WIDTH//7,HEIGHT//10.8))
        
        for option in startOptions: #Iterate through all menu buttons
            if option.rect.collidepoint(pygame.mouse.get_pos()): #Check if mouse is within bounds of the button
                option.hovered = True #If so, set that to true
            else:
                option.hovered = False #Otherwise, nah
            option.draw() #Redraw the button(white or grey)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inStart = False
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startOptions[0].rect.collidepoint(pygame.mouse.get_pos()):
                    inStart = False
                    inPlay = True
                    inPlayer1 = True
                if startOptions[1].rect.collidepoint(pygame.mouse.get_pos()):
                    inStart = False
                    inSettings = True

    while inSettings:
        pygame.event.pump()
        screen.blit(tennis,(0,0))
        textSpeed = regularFont.render("BALL SPEED",1,WHITE)
        screen.blit(textSpeed,(WIDTH//12.8,HEIGHT//16))
        speedSelect = pygame.transform.scale(selectBox,(defaultSpeedWidth,defaultSpeedHeight))
        screen.blit(speedSelect,defaultSpeed)
        textMusic = regularFont.render("MUSIC",1,WHITE)
        screen.blit(textMusic, (WIDTH//1.8,HEIGHT//16))
        musicSelect = pygame.transform.scale(selectBox,(WIDTH//6,HEIGHT//6))
        screen.blit(musicSelect, (WIDTH//1.8,HEIGHT//5))
        screen.blit(musicSelect, (WIDTH//1.3,HEIGHT//5))
        musicOnText = clickFONT.render("ON",1,BLACK)
        screen.blit(musicOnText, (WIDTH//1.65,HEIGHT//4.4))
        musicOffText = clickFONT.render("OFF",1,BLACK)
        screen.blit(musicOffText, (WIDTH//1.25,HEIGHT//4.4))
        screen.blit(woodPlank, (WIDTH//1.38,HEIGHT//5.7))
        textBackgrounds = regularFont.render("BACKGROUNDS",1,WHITE)
        screen.blit(textBackgrounds, (WIDTH//1.8,HEIGHT//2))
        backgroundSelect = pygame.transform.scale(selectBox,(defaultBackgroundW,defaultBackgroundH))
        screen.blit(backgroundSelect,defaultBackground)

        for option in settingsOptions: 
            if option.rect.collidepoint(pygame.mouse.get_pos()): 
                option.hovered = True 
            else:
                option.hovered = False
            option.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inSettings = False
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if settingsOptions[0].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultSpeedWidth = settingsOptions[0].rend.get_rect()[2]
                    defaultSpeedHeight = settingsOptions[0].rend.get_rect()[3]
                    defaultSpeed = speedSelectPos[0]
                elif settingsOptions[1].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultSpeedWidth = settingsOptions[1].rend.get_rect()[2]
                    defaultSpeedHeight = settingsOptions[1].rend.get_rect()[3]
                    defaultSpeed = speedSelectPos[1]
                elif settingsOptions[2].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultSpeedWidth = settingsOptions[2].rend.get_rect()[2]
                    defaultSpeedHeight = settingsOptions[2].rend.get_rect()[3]
                    defaultSpeed = speedSelectPos[2]
                elif settingsOptions[3].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultBackground = backgroundSelectPos[0]
                    defaultBackgroundW = settingsOptions[3].rend.get_rect()[2]
                    defaultBackgroundH = settingsOptions[3].rend.get_rect()[3]
                    chosenBackground = sunny
                elif settingsOptions[4].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultBackground = backgroundSelectPos[1]
                    defaultBackgroundW = settingsOptions[4].rend.get_rect()[2]
                    defaultBackgroundH = settingsOptions[4].rend.get_rect()[3]
                    chosenBackground = beach
                elif settingsOptions[5].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultBackground = backgroundSelectPos[2]
                    defaultBackgroundW = settingsOptions[5].rend.get_rect()[2]
                    defaultBackgroundH = settingsOptions[5].rend.get_rect()[3]
                    chosenBackground = volcano
                elif settingsOptions[6].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultBackground = backgroundSelectPos[3]
                    defaultBackgroundW = settingsOptions[6].rend.get_rect()[2]
                    defaultBackgroundH = settingsOptions[6].rend.get_rect()[3]
                    chosenBackground = sky
                elif settingsOptions[7].rect.collidepoint(pygame.mouse.get_pos()):
                    defaultBackground = backgroundSelectPos[4]
                    defaultBackgroundW = settingsOptions[7].rend.get_rect()[2]
                    defaultBackgroundH = settingsOptions[7].rend.get_rect()[3]
                    chosenBackground = foot
                elif settingsOptions[8].rect.collidepoint(pygame.mouse.get_pos()):
                    inSettings = False
                    inStart = True
                    
    score1 = 0
    score2 = 0
    while inPlay:
        name1 = regularFont.render(player1Text,1,(RED))
        name1Rect = name1.get_rect()
        name1Rect.topleft = (WIDTH//10,HEIGHT//4)
        cursor = pygame.Rect(name1Rect.topright,(3,name1Rect.height))
        while inPlayer1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        player1Text = player1Text[:-1]
                    else:
                        player1Text = player1Text + event.unicode
                    name1 = regularFont.render(player1Text,1,(RED))
                    name1Rect.size = name1.get_size()
                    cursor.topleft = name1Rect.topright
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if doneButton[0].rect.collidepoint(pygame.mouse.get_pos()):
                        inPlayer1 = False
                        inPlayer2 = True
                    
            screen.fill(BLACK)
            nameintro1 = regularFont.render("Player 1, enter your name:",1,WHITE)
            screen.blit(nameintro1,(WIDTH//10,HEIGHT//10))
            screen.blit(name1,(WIDTH//10,HEIGHT//4))

            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen,(RED),cursor)
                
            for option in doneButton:
                if option.rect.collidepoint(pygame.mouse.get_pos()): 
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()
            pygame.display.update()

        name2 = regularFont.render(player2Text,1,(BLUE))
        name2Rect = name2.get_rect()
        name2Rect.topleft = (WIDTH//10,HEIGHT//4)
        cursor = pygame.Rect(name2Rect.topright,(3,name2Rect.height))
        while inPlayer2:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        player2Text = player2Text[:-1]
                    else:
                        player2Text = player2Text + event.unicode
                    name2 = regularFont.render(player2Text,1,(BLUE))
                    name2Rect.size = name2.get_size()
                    cursor.topleft = rect.topright
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if doneButton[0].rect.collidepoint(pygame.mouse.get_pos()):
                        inPlayer2 = False
                        inGame = True
                    
            screen.fill(BLACK)
            nameintro2 = regularFont.render("Player 2, enter your name:",1,WHITE)
            screen.blit(nameintro2,(WIDTH//10,HEIGHT//10))
            screen.blit(name2,(WIDTH//10,HEIGHT//4))
            
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen,(BLUE),cursor)
                
            for option in doneButton:
                if option.rect.collidepoint(pygame.mouse.get_pos()): 
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()
            pygame.display.update()
        
        players = [Option(player1Text,(WIDTH//4,HEIGHT//1.2)),Option(player2Text,(WIDTH//1.5,HEIGHT//1.2))]
        while inGame:
            screen.blit(chosenBackground,(0,0))
            
            textName1 = regularFont.render(player1Text,1,RED)
            textName2 = regularFont.render(player2Text,1,BLUE)
            textScore1 = regularFont.render(str(score1),1,RED)
            textScore2 = regularFont.render(str(score2),1,BLUE)

            screen.blit(textName1,(WIDTH//4,HEIGHT//1.2))
            screen.blit(textName2,(WIDTH//1.8,HEIGHT//1.2))
            screen.blit(textScore1,(WIDTH//50,HEIGHT//1.2))
            screen.blit(textScore2,(WIDTH//1.07,HEIGHT//1.2))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        inGame = False
                        inPlay = False
                        running = False
# ---------------------------------------------  modify so score must be increased after ball goes out
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score1 = score1 + 1
# ------------------------------------------------------------------                
            if score1 == winningScore or score2 == winningScore:
                inGame = False
                inPlay = False
                postGame = True

    winner = ""
    while postGame:
        pygame.event.pump()
        screen.blit(chosenBackground,(0,0))
        gameOverText = titleFont.render("GAME OVER",1,PURPLE)
        screen.blit(gameOverText,(WIDTH//4.8,HEIGHT//20))

        if score1 == winningScore:
            winner = player1Text
            winnerText = regularFont.render(player1Text + " is the winner!",1,RED)
            screen.blit(winnerText,(WIDTH//4.8,HEIGHT//4))
        if score2 == winningScore:
            winner = player2Text
            winnerText = regularFont.render(player2Text + " is the winner!",1,BLUE)
            screen.blit(winnerText,(WIDTH//4.8,HEIGHT//4))

        for option in postGameOptions:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    postGame = False
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if postGameOptions[0].rect.collidepoint(pygame.mouse.get_pos()):
                    postGame = False
                    inPlay = True
                    inPlayer1 = False
                    inPlayer2 = False
                    inGame = True
                    score1 = 0
                    score2 = 0
                if postGameOptions[1].rect.collidepoint(pygame.mouse.get_pos()):
                    postGame = False
                    inStart = True


pygame.quit() #SHTAWP
