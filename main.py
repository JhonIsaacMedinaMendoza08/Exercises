#Write a program that, given a number from 1 to 7, prints the corresponding day of the week using match .
print (""" 
---------------------------------------------------------
--------------Exercise 5 Day of the week-----------------
---------------------------------------------------------""")

def day_of_the_week(day_number):
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid number. Must be between 1 and 7."

day_number = int(input("Enter a number from 1 to 7 to get the day of the week:"))

print (f"The day of the week according to the number is: {day_of_the_week(day_number)}")