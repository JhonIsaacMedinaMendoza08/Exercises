#Write a program that prompts the user for two integers, a start value and an end value. The program should print all the 
# even numbers in that range, including the limits. Use a for loop to iterate through the range.
print(""" 
---------------------------------------------------------
---------Exercise 4 Iterative Structures-----------------
---------------------------------------------------------""")

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

if start > end:
    print("The start value must be less than or equal to the end value.")

for even in range(start, end + 1):
    if even % 2 == 0:
        print(even)