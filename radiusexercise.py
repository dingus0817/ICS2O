##PI = 3.14
##radius = int(input("Enter a radius: "))
##while(radius>0):
##    area = PI*(radius**2)
##    print("Area:", area)
##    radius = int(input("Enter a radius: "))
##print("uhhhhh idk how to do that lmao")

##import pygame
##import time
##pygame.init()
##
##BEGIN = pygame.time.get_ticks()         # record the time when the main loop begins
##while True:
##    
##    elapsed = pygame.time.get_ticks() + BEGIN
##    print(elapsed)
##    
##    print(round(elapsed/1000), "seconds have passed since the beginning of the main loop")
##    time.sleep(1)


##from random import randint
##UNLUCKY_NUMBER = 4
##COUNT = 10
##
##randomNumbers = []
##for i in range(COUNT):
##    randomNumber = randint(1,5)
##    randomNumbers.append(randomNumber)
##print("All numbers : ", randomNumbers)
##
##for i in range(COUNT-1,-1,-1):          # traversing in reverse order, from last index to zero
##    if randomNumbers[i] == UNLUCKY_NUMBER:
##        randomNumbers.pop(i)
##print("Good numbers: ", randomNumbers, "\n")


##import time
##
##PERIOD = 1
##BEGIN = time.time()
##referenceTime = BEGIN
##elapsed = 0
##
##while True:
##    elapsed = round(time.time() - referenceTime, 1)
##    if elapsed > PERIOD:
##        print ("Tic-Toc")
##        referenceTime = time.time()     # set new reference time


##import threading as th  
#### Defining of a method  
##def sctn():  
##    print("SECTION FOR LIFE \n")
##S = th.Timer(5.0, sctn)
##S.start()



##
##from __future__ import print_function
##
##
##from threading import Timer
##
##
##def hello():
##    print("Hello World!")
##
##
##class RepeatingTimer(object):
##
##    def __init__(self, interval, f, *args, **kwargs):
##        self.interval = interval
##        self.f = f
##        self.args = args
##        self.kwargs = kwargs
##
##        self.timer = None
##
##    def callback(self):
##        self.f(*self.args, **self.kwargs)
##        self.start()
##
##    def cancel(self):
##        self.timer.cancel()
##
##    def start(self):
##        self.timer = Timer(self.interval, self.callback)
##        self.timer.start()
##
##
##t = RepeatingTimer(3, hello)
##t.start()

##import time
##
##BEGIN = time.time()                     # record the time when the main loop begins
##while True:
##    #enterSomethingToWasteTime = raw_input("enter something: ")
##    elapsed = time.time() - BEGIN
##    print (elapsed,"seconds have passed since the beginning of the main loop")


##
##def printRow(columns):
##    print("* " * columns)
##
##def printAsterisks(rows,columns):
##    for row in range(rows):
##        printRow(columns)
##
##printAsterisks(2,3)




