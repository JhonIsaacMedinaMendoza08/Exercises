#Write a program that calculates the cost of parking based on the number of hours, with progressive rates.

print(""" 
---------------------------------------------------------
-----------------Exercise 21 ----------------------------
---------------------------------------------------------""")

hours = int(input("Enter the number of parking hours: "))

cost = 0
if hours <= 0:
    print("The number of hours cannot be negative.")
elif hours <= 1:
    cost = 5
elif hours >= 2 and hours <=4:
    cost = 5 + (hours - 1) * 4
else:
    cost = 5 + 3 * 3 + (hours - 4) * 3 

print(f"The total cost of parking is: ${cost}")