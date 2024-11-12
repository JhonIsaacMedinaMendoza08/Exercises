#Write a program that classifies a person based on their age.
print (""" 
---------------------------------------------------------
-------------Exercise 9 years classification-------------
---------------------------------------------------------""")

Age = int (input("Enter your age to determine if you are a child, teenager, adult or senior: "))

if Age >=0 and Age<= 12:
    print ("The person is a child")
elif Age >=13 and Age <=17:
    print ("The person is a teenager")
elif Age >= 18 and Age <= 64 :
    print ("The person is an adult")
else:
    print ("The person is an old man")