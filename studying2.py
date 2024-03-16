##quantity = int(input("how much food u want?: "))
##UNIT_COST = 100
##cost = UNIT_COST * quantity
##
##if cost > 1000:
##    cost = cost - cost*0.1
##else:
##    cost = cost
##print("the total cost will be:", cost)


##totalClass = int(input("enter the total number of classes: "))
##attendedClass = int(input("enter the number of classes u attended: "))
##
##percentage = round(((attendedClass/totalClass)*100),1)
##print("you attended", percentage, "% of ur classes")
##
##if percentage < 75:
##    print("wow u r a bad student: u cannot go to the exam :O")
##else:
##    print("good luck on ur exam :D")


##total = 0
##loopNumber = 10
##for count in range(loopNumber):
##    number = int(input("enter a number: "))
##    total = total + number
##average = total/loopNumber
##print("the average of the 10 numbers is", average)


##import random
##number = random.randint(1,9)
##
##running = True
##
##while running:
##    guess = int(input("guess a number from 1-9: "))
##    if guess == number:
##        running = False
##        print("lucky guess lol")
##    else:
##        print("nope")


##for count in range(1,51):
##    if count%3 == 0 and count%5 == 0:
##        print("FizzBuzz")
##    elif count%3 == 0:
##        print("Fizz")
##    elif count%5 == 0:
##        print("Buzz")
##    else:
##        print(count)


##x,y = 0,1
##while x < 50:
##    x, y = y, x + y
##    print(x)


##x = 0
##y = 1
##while x < 50:
##    x1 = x
##    x = y
##    y = x1 + y
##    print(x)


##age = int(input("enter ur age: "))
##if age >= 18:
##    print("wow u can vote")
##else:
##    print("u cant vote")


##print("gib me 3 numbers")
##num1 = int(input("gib me a number: "))
##num2 = int(input("gib me a number: "))
##num3 = int(input("gib me a number: "))
##bigNum = 0
##
##if num1 > num2 and num1 > num3:
##    bigNum = num1
##elif num2 > num1 and num2 > num3:
##    bigNum = num2
##else:
##    bigNum = num3
##print("the biggest number out of the three is", bigNum)


##for count in range(1500,2701):
##    if count % 5 == 0 and count % 7 == 0:
##        print(count)



##salary = int(input("enter ur salary: "))
##years = int(input("enter the number of years u have worked: "))
##net = 0
##
##if years > 10:
##    net = salary * 0.1 + salary
##elif years >= 6 and years <= 10:
##    net = salary * 0.08 + salary
##else:
##    net = salary * 0.05 + salary
##print("ur net bonus amount will be:", round(net,2))


##oddSum = 0
##for count in range(12,38):
##    if count%2 == 1:
##        oddSum = oddSum + count
##print("the sum of the odd numbers from 12 - 37 is:", oddSum)


##for count in range(1,1001):
##    total = 0
##    x = count
##
##    while x != 0:
##        digit = x % 10
##        num = digit**3
##        total = total + num
##        x = x//10
##        
##    if count == total:
##        print("Armstrong:", count)



##number = int(input("enter a number: "))
##total = 0
##for count in range(number + 1):
##    total = total + count
##print("the sum of all the numbers from 1 to", number, "is:", total)



##def isPalindrome(word):
##    if(word == word[::-1]):
##       return "The string is a palindrome"
##    else:
##        return "The string is not a palindrome"
##
##
##word = input("enter a word: ")
##newWord = ""
##for letter in range(len(word) - 1, -1, -1):
##    print(word[letter], end = "")
##print()
##print(isPalindrome(word))


##word = input("enter a word: ")
##reverseWord = ""
##for letter in word:
##    reverseWord = letter + reverseWord
##print(reverseWord)
##if word + "" == reverseWord:
##    print("the word is a palindrome")
##else:
##    print("the word is not a palindrome")
##
##
##
##h = float(input("enter the height of triangle: "))
##b = float(input("enter the base of triangle: "))
##area = b*h/2
##print("the area of the triangle is:", area)
##


##decimal = int(input("Please enter an integer number in the range 0-255: "))
##binary = ""                             # start with an empty binary string
##
##for bit in range(8):                    # repeat 8 times 
##    digit = decimal % 2                 # take the last (least significant) bit
##    binary = str(digit) + binary        # concatenate it in front of the binary string so far
##    decimal = decimal / 2               # shift all bits to the right
##
##print ("The binary representation of this number is:",binary)


import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')

rect1 = pg.Rect(200, 100, 161, 100)
rect2 = pg.Rect(0, 0, 120, 74)
rect2.center = rect1.center

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill(BG_COLOR)
    pg.draw.rect(screen, (0, 100, 255), rect1, 2)
    pg.draw.rect(screen, (255, 128, 0), rect2, 2)
    pg.display.flip()
    clock.tick(60)
pygame.quit()


