#Write a program that asks the user to input integers indefinitely. The program should 
# add up the numbers as long as they are even, but should stop if the user inputs an odd number. 
# Use a while loop to accomplish this.

print(""" 
---------------------------------------------------------
---------Exercise 7 Iterative Structures-----------------
---------------------------------------------------------""")

sum = 0
    
while True: 
    number = int(input("Enter an integer: ")) 
        
    if number % 2 != 0: 
        print("Odd number entered.")
        break 
    else:
        sum = number + sum
print(f"The sum of the even numbers given is: {sum}")