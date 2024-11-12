#Write a program that calculates BMI and determines weight status.
import math

print (""" 
---------------------------------------------------------
--------------------Exercise 12 BMI ---------------------
---------------------------------------------------------""")

weight = float(input("PLease enter your weight (KG): "))
height = float(input("Please enter your height (M): "))

imc = weight / math.pow (height, 2)


if imc < 18.5:
    print (f"you are underweight with BMI {imc:.2f}")
elif imc > 18.5 and imc < 24.9:
    print (f"You are a normal weight with BMI {imc:.2f}")
elif imc > 25 and imc < 29.9:
    print (f"you are overweight with BMI {imc:.2f}")
else:
    print (f"you are in obesity with BMI {imc:.2f}")