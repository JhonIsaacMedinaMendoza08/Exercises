#Write a program that converts a numeric grade to a letter grade according to a
#specific grading system, using match .

print(""" 
---------------------------------------------------------
-----------------Exercise 20 ----------------------------
---------------------------------------------------------""")

def convert_grades():
    grades = float(input("Enter the numerical rating (0-100): "))
    if not (0 <= grades <= 100):
        print("The rating must be between 0 and 100.")
        return
    match grades:
        case grades if 90 <= grades <= 100:
            letter = 'A'
        case grades if 80 <= grades < 90:
            letter = 'B'
        case grades if 70 <= grades < 80:
            letter = 'C'
        case grades if 60 <= grades < 70:
            letter = 'D'
        case _:
            letter = 'F'
    print(f"The letter grade is: {letter}")
convert_grades()