#Write a program that prompts the user for a positive integer n and calculates the sum of the 
# first n integers. Use a for loop to perform the sum.

print(""" 
---------------------------------------------------------
---------Exercise 1 Iterative Structures-----------------
---------------------------------------------------------""")

def sum_of_numbers():
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        print("Please enter a positive integer.")
        return
    sum = 0

    for i in range(1, number + 1):
        sum = i + sum
    print(f"The sum of the first {number} integers is: {sum}")
sum_of_numbers()