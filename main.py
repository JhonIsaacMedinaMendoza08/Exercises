#Write a program that asks the user for a positive integer n and calculates the factorial. 
# Use a for loop to perform the calculation.
print(""" 
---------------------------------------------------------
---------Exercise 3 Iterative Structures-----------------
---------------------------------------------------------""")

n = int(input("Please enter the number: "))

if n < 0:
    print ("Please enter a positive number ")
else:
    factorial = 1
    for i in range (1 , n + 1):
        factorial = factorial*i

    print (f"The factorial of {n} is {factorial}")