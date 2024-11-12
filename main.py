#Write a program that determines the type of triangle based on its sides using if
print (""" 
---------------------------------------------
--------Exercise 4 type of triangles---------
---------------------------------------------""")

lado1 = float(input("\tPlease enter the side distance: "))
lado2 = float(input("\tPlease enter the side distance: "))
lado3 = float(input("\tPlease enter the side distance: "))


if lado1==lado2 ==lado3:
    print ("\tIt is an equilateral triangle")
elif lado1==lado2 or lado1==lado3 or  lado2==lado3:
    print ("\tIt is an isosceles triangle")
elif lado1!=lado2 and lado1!=lado3 and lado2!=lado3 and lado1>0 and lado2>0 and lado3>0:
    print ("\tIt is a scalene triangle")
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print ("\tInvalid! Enter positive values greater than zero")