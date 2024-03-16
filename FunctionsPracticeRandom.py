import string
import random

def randomNumber():
    number = random.randint(8,16)
    return number

def randomLetter():
    print(random.choice(string.ascii_letters), end = "")
    
print("your random password: ", end = "")

for letter in range(randomNumber()):
    randomLetter()
