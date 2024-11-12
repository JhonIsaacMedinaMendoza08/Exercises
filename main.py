#Write a program that calculates a student's final grade based on his/her grade.

print(""" 
---------------------------------------------------------
-----------------Exercise 18 ----------------------------
---------------------------------------------------------""")

def credits_calculate():
    num_subjects = int(input("Enter the number of subjects taken: "))
    total_credits = 0

    for i in range(num_subjects):
        score = float(input(f"Enter the score obtained in subject {i+1}: "))
        if score >= 60:
            total_credits += 3  
    print(f"The total number of credits approved is: {total_credits}")
credits_calculate()
