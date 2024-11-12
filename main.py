#Write a program that converts Celsius to Fahrenheit or Fahrenheit to Celsius using match .
print (""" 
---------------------------------------------------------
--------------------Exercise 11 -------------------------
---------------------------------------------------------""")


def convert_temperature(number, scale):
    match scale.lower():
        case "c":
            f = (1.8 * number) + 32
            return f
        case "f":
            c = (number - 32) / 1.8
            return c
        case _:
            return "Invalid scale! , try again with 'C' or 'F'"


Temperture = float(input("Please enter the temperture:  "))
scale = input("Celsious - 'C' or fahrenheir - 'F':  ")


new_temperture = convert_temperature(Temperture, scale)

print (f"The converted temperture is: {new_temperture} grades")