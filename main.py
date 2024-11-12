#Write a program that determines whether a year is a leap year or not.
print (""" 
---------------------------------------------------------
------------------Exercise 8 leap year-------------------
---------------------------------------------------------""")
year = int(input("Enter the year to validate: "))

if year % 400 == 0:#or year %400 ==0 :
    print ("The year is leap year")
elif year %4 ==0:
    print ("The year is leap year")
else:
    print ("The year isn't leap year")