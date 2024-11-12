#Write a program that determines whether a number is positive, negative, or zero using if .
print (""" 
---------------------------------------------------------
-----Exercise 7 Positive, negative or zero number--------
---------------------------------------------------------""")
number = int(input("Enter the number to validate: "))

if number == 0:
    print ("The number provided is zero")
elif number < 0:
    print ("The number provided is negative")
else:
    print ("The number provided is positive")