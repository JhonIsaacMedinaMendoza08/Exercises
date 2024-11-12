#Write a program that determines the largest of three numbers using if 
print (""" 
---------------------------------------------------------
--------------------Exercise 13 -------------------------
---------------------------------------------------------""")

num1 = int(input("Please enter the number 1: "))
num2 = int(input("Please enter the number 2: "))
num3 = int(input("Please enter the number 3: "))

if num1 >= num2 and num1 >= num3:
    print (f"the largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print (f"the largest number is: {num2}")
else:
    print (f"the largest number is: {num3}")