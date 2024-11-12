#Write a program that calculates a student's final grade based on his/her grade.

print (""" 
---------------------------------------------------------
-----------------Exercise 17 ----------------------------
---------------------------------------------------------""")

def final_qualification():
    qualification = float(input("Enter the student's grade (0-100): "))
    additionalPoints = input("Did the student do additional homework? (yes/no): ").lower()
    if additionalPoints == "yes":
        qualification += (qualification * 0.05)
        if qualification > 100:
            qualification = 100  
    print(f"The student's final grade is: {qualification:.2f}")

final_qualification()
