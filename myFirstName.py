print("Let's play a game :DD")
word = "panda"
print("First guess the letters of the mystery word.")
print("Then after five guesses, guess the word. (hint: no capitals)")
print("It is an animal.")
attempt1 = input("Guess a letter: ")
print(attempt1 in word)
attempt2 = input("Guess again: ")
print(attempt2 in word)
attempt3 = input("Guess again: ")
print(attempt3 in word)
attempt4 = input("Guess again: ")
print(attempt4 in word)
attempt5 = input("Guess again: ")
print(attempt5 in word)
answer = input("Now guess the word: ")
if answer==word:
    print("Wowww congrats!")
else:
    print("lmao L bozo u suc") 



