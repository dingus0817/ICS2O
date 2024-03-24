code = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5, 
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
}


def solution():
    word1 = input("please enter word #1: ")
    letters1 = []
    for letter in word1:
        letters1.append(letter)
    word2 = input("please enter word #2: ")
    letters2 = []
    for letter in word2:
        letters2.append(letter)
    word3 = input("please enter word #3: ")
    letters3 = []
    for letter in word3:
        letters3.append(letter)

    print(word1 + " " + word2 + " " + word3)

    code1 = ''
    counter1 = 0
    for letter in word1:
        for key in code:
            if letter.casefold() == key.casefold():
                counter1 = counter1 + 1
                code1 = code1 + str(code[key])
                if counter1 < len(word1):
                    code1 = code1 + "-"
    

    code2 = ''
    counter2 = 0
    for letter in word2:
        for key in code:
            if letter.casefold() == key.casefold():
                counter2 = counter2 + 1
                code2 = code2 + str(code[key])
                if counter2 < len(word2):
                    code2 = code2 + "-"
    
    code3 = ''
    counter3 = 0
    for letter in word3:
        for key in code:
            if letter.casefold() == key.casefold():
                counter3 = counter3 + 1
                code3 = code3 + str(code[key])
                if counter3 < len(word3):
                    code3 = code3 + "-"

    return code1 + " + " + code2 + " + " + code3
    

    
print(solution())


    