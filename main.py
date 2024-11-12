#Write a program that generates a random number between 1 and 100 and allows the user to guess it. 
# The program should give clues as to whether the entered number is greater or less than the secret number.

import random
print(""" 
---------------------------------------------------------
---------Exercise 6 Iterative Structures-----------------
---------------------------------------------------------""")

def guess_the_number():  
    number_to_guess = random.randint(1,100)
    print ("\tWelcome to guess the number")
    print ("\tthink of a number between 1 and 100")
    while True:
        guess = int(input("Enter the number you thought of: "))
        #print ({number_to_guess})
        if guess > number_to_guess:
            print ("The number entered is higher, please try again (numbers between 1-100)")
        elif guess < number_to_guess:
            print ("The number entered is less, please try again (numbers between 1-100)")
        else:
            print ("the number entered is the same, congratulations!!")
            break
guess_the_number()