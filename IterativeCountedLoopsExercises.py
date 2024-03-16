#File name: IterativeCountedLoopsExercises.py
#Description: This program is for practicing iterative/counted loops
#Author: Jamie Zhang

##for number in [0,-1,-2,-3,-4,-5]:
##    print(number)
##print()
##
##
##for number in [-1,-2,-3,-4,-5]:
##    print(number)
##print() 
##    
##
##for number in [-3,-2,-1,0,1,2]:
##    print(number)
##print()
##
##
##for number in [10,8,6,4,2,0]:
##    print(number)
##print()
##
##
##for number in [1,3]:
##    print(number)
##print()
##
##
##
##for number in range(5,17):
##    print(number)
##print()
##
##
##
##for number in range(20):
##    print("jamy")
##print()
##
##
##
##for number in range(10,0,-1):
##    print(number)
##print("Blast Off!\n")
##    
##
##
##for number in range(1,100):
##    if number%3 == 0:
##        print(number)
##print()
##
##
##
##
##
##
##
##number = 0
##notValid = True
##while (notValid):
##    number = int(input("Enter an integer number in the range 0 - 255: "))
##    if (number > 255 or number < 0):
##        print("Please enter 0 - 255, idiot")
##    else:
##        notValid = False
##
##bit128 = 0
##bit64 = 0
##bit32 = 0
##bit16 = 0
##bit8 = 0
##bit4 = 0
##bit2 = 0
##bit1 = 0
##
##for orange in [128,64,32,16,8,4,2,1]:
##    bit = number - orange 
## 
##    if (number >= 128):
##        bit128 = 1
##    elif (128 > number >= 64):
##        bit64 = 1
##    elif (64 > number >= 32):
##        bit32 = 1
##    elif (32 > number >= 16):
##        bit16 = 1
##    elif (16 > number >= 8):
##        bit8 = 1
##    elif (8 > number >= 4):
##        bit4 = 1
##    elif (4 > number >= 2):
##        bit2 = 1
##    elif (2 > number > 0):
##        bit1 = 1
##    if (bit >= 0):
##        number = bit
##        
##binary = str(bit128) + str(bit64) + str(bit32) + str(bit16) + str(bit8) + str(bit4) + str(bit2) + str(bit1)
##
##print("The binary representation of this number is:", binary)




##decimal = int(input("Please enter an integer number in the range 0-255: "))
##binary = ""                             
##
##for bit in range(8):                    
##    digit = decimal%2                 
##    binary = str(digit) + binary         
##    decimal = decimal / 2               
##
##print ("The binary representation of this number is:",binary)




number = int(input("Enter an integer in the range 0 - 255: "))
binary = ""
for count in range(7,-1,-1):
    result = number//(2**count)
    bit = result%2
    binary = binary + str(bit)
    print(binary)
print(binary)
    
