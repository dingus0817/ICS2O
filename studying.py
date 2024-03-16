##print("Python rocks")
##
##
##print("computer science\n@\nuhs")
##
##
##HST_TAX = 0.13
##COMPUTER = 867.53
##
##tax = COMPUTER*HST_TAX
##print("the tax for the computer is", tax)
##
##
##
##print(round(232/60, 1))
##
##
##
##PI = 3.14
##d = 6
##c = PI * d
##print(c)
##
##
##mean = (17 + 24 + 30)/3
##print(round(mean, 1))
##
##
##
##print("spy" + "x" + "family", "sucks", "2023")
##
##
##
##
##colour = input("what's your favourite colour: ")
##print(colour)
##
##
##
##
##firstName = input("enter ur first name: ")
##lastName = input("enter ur last name: ")
##print("hello", firstName, lastName + ". how r u?")
##
##
##
##IN_TO_CM = 2.54
##inch = float(input("enter a length: "))
##cm = inch * IN_TO_CM
##print("the length from inches to cm is", cm)
##
##
##print(chr(116) + chr(104) + chr(102))
##
##
##
##
##name = "Jamie"
##for letter in name:
##    asci = ord(letter)
##    print(asci, end = " ")



MISTAKE_LIMIT = 7
mistakes = 0
guesses = ""
wrongLetters = ""
missingLetters = 50
guesses = ""
numGuess = 0
reset = 0
guessed = False
postGame = "1"
previousGuess = 50

print("\nHello, player! Let's play Hangman today")
print("You get seven allowed mistakes")
print("The goal is to guess the word in the least amount of guesses")
print("The category is: animals")
name = input("What's your name? ")

while (postGame == "1" or postGame == "3"):
    HANGMAN_PICS = ['''
      +---+
          |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
    (;-;) |
          |
          |
          |
    =========''', '''
      +---+
      |   |
    (;-;) |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
    (;-;) |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
    (;-;) |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
    (;-;) |
     /|\  |
     /  
          |
    =========''', '''
      +---+
      |   |
    (;-;) |
     /|\  |
     / \  |
          |
    =========''']
    
    from random import randint
    
    words = []
    file = open("words.txt", "r")
    for line in file:
        word = line.strip("\n")
        words.append(word)
    file.close()

    for i in range(20):
        pick = randint(0, len(words)-1)
        secretWord = words[pick]

    if (postGame == "3"):
        name = input("\nHello, new player. What's your name? ")

    while (mistakes < MISTAKE_LIMIT and missingLetters > 0): 
        guess = input("\nGuess a letter, " + name + ": ")
        guesses = guesses + guess
        numGuess = numGuess + 1
        numLettersGuessed = reset
        
        for letter in secretWord:
            if letter in guesses:
                print(letter, end = " ") 
                numLettersGuessed = numLettersGuessed + 1
            else: 
                print("_", end = " ")
                
        missingLetters = len(secretWord) - numLettersGuessed

        if guess not in secretWord:
            print("\n" + guess, "is incorrect") 
            mistakes = mistakes + 1
            print(HANGMAN_PICS[0 + mistakes])
            wrongLetters = wrongLetters + guess + " "
        else:
            print("\n" + guess, "is correct!")
            print(HANGMAN_PICS[0 + mistakes])

        print("The wrong letters are: " + wrongLetters)
        print("You have", missingLetters, "missing letters") 
        print("You have", MISTAKE_LIMIT - mistakes, "allowed mistakes left")
                 
    if (missingLetters == 0):
        guessed = True
        print("\nCongratulations", name + "! You won!")    
    else:
        print("\nYou lost! The word was '" + secretWord + "'")

    print(name + "'s score:", numGuess, "guesses")  
        
    if (numGuess <= previousGuess):
        bestScore = numGuess
        bestUser = name
        
    print("Best player so far:", bestUser + ",", bestScore, "guesses")
    
    mistakes = reset
    missingLetters = 8
    guesses = ""
    previousGuess = numGuess
    numGuess = reset
    numLettersGuessed = reset
    wrongLetters = ""
    countGuess = reset
    
    print("\nPlay Again - press 1")
    print("Exit - press 2")
    print("Switch Players - press 3")
    postGame = input("Enter your choice: ")

print("Thank you for playing!")







secretWord = "tootsies"
MISTAKE_LIMIT = 7
mistakes = 0
guesses = ""
wrongLetters = ""
missingLetters = 8
guesses = ""
numGuess = 0
reset = 0
guessed = False
postGame = "1"
previousGuess = 50



print("\nHello, player! Let's play Hangman today")
print("You get seven allowed mistakes")
print("The goal is to guess the word in the least amount of guesses")
name = input("What's your name? ")

while (postGame == "1" or postGame == "3"): 

    if (postGame == "3"):
        name = input("\nHello, new player. What's your name? ")

    while (mistakes < MISTAKE_LIMIT and missingLetters > 0): 

        guess = input("\nGuess a letter, " + name + ": ")
        guesses = guesses + guess
        numGuess = numGuess + 1
        numLettersGuessed = reset
        missingLetters = 8 

        for letter in secretWord:
            if letter in guesses:
                print(letter, end = " ") 
                numLettersGuessed = numLettersGuessed + 1
            else: 
                print("_", end = " ")
                
        missingLetters = missingLetters - numLettersGuessed

        if guess not in secretWord:
            print("\n" + guess, "is incorrect") 
            mistakes = mistakes + 1
            wrongLetters = wrongLetters + guess + " "
        else:
            print("\n" + guess, "is correct!")
            

        print("The wrong letters are: " + wrongLetters)
        print("You have", missingLetters, "missing letters") 
        print("You have", MISTAKE_LIMIT - mistakes, "allowed mistakes left")
         
              
    if (missingLetters == 0):
        guessed = True
        print("\nCongratulations", name + "! You won!")
        
    else:
        print("\nYou lost! The word was '" + secretWord + "'")

    print(name + "'s score:", numGuess, "guesses")
    
        
    if (numGuess <= previousGuess):
        bestScore = numGuess
        bestUser = name
    print("Best player so far:", bestUser + ",", bestScore, "guesses")
    

    mistakes = reset
    missingLetters = 8
    guesses = ""
    previousGuess = numGuess
    numGuess = reset
    numLettersGuessed = reset
    wrongLetters = ""
    countGuess = reset
    

    print("\nPlay Again - press 1")
    print("Exit - press 2")
    print("Switch Players - press 3")
    postGame = input("Enter your choice: ")







           
