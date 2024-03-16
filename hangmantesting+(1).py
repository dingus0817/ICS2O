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
name = input("What's your name? ")

while (postGame == "1" or postGame == "3"):
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

print("Thank you for playing!")

    



     
