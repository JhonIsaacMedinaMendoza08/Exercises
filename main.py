#Write a program that classifies a triangle as acute, obtuse or right triangle according to its internal angles using if .

print(""" 
---------------------------------------------------------
-----------------Exercise 22 ----------------------------
---------------------------------------------------------""")

def triangles():
    a1 = float(input("Enter the first angle (in degrees): "))
    a2 = float(input("Enter the second angle (in degrees): "))
    a3 = float(input("Enter the third angle (in degrees): "))
    if a1 + a2 + a3 != 180:
        print("The angles do not add up to 180 degrees. It is not a valid triangle.")
        return
    if a1 == 90 or a2 == 90 or a3 == 90:
        type = "Rectangle"
    elif a1 > 90 or a2 > 90 or a3 > 90:
        type = "Obtuss"
    else:
        type = "Acute"
    print(f"The type of triangle is: {type}")
triangles()
