#Write a program that implements a number guessing game.

import random
print (""" 
---------------------------------------------------------
--------------Exercise 6 guess the number----------------
---------------------------------------------------------""")

def guess_the_number():  
    number_to_guess = random.randint(1,10)
    print ("\tWelcome to guess the number")
    print ("\tthink of a number between 1 and 10")
    while True:
        guess = int(input("Enter the number you thought of: "))
        #print ({number_to_guess})
        if guess > number_to_guess:
            print ("The number entered is higher, please try again (numbers between 1-10)")
        elif guess < number_to_guess:
            print ("The number entered is less, please try again (numbers between 1-10)")
        else:
            print ("the number entered is the same, congratulations!!")
            break
guess_the_number()