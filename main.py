#Request a numerical grade and classify it as A (90-100), B (80-89), C (70-79), D (60-69), or F (<60).
print (""" 
---------------------------------------------------------
-------------Exercise 10 numerical grade-----------------
---------------------------------------------------------""")

grade = int (input("Enter your numerical grade to be evaluated: "))

if grade >=90 and grade <=100:
    print ("Your rating is: A")
elif grade >= 80 and grade <= 89 :
    print ("Your rating is: B")
elif grade >= 70 and grade <= 79 :
    print ("Your rating is: C")
elif grade >= 60 and grade <= 69 :
    print ("Your rating is: D")
elif grade <= 59 and grade <= 0:
    print ("Your rating is: F")
else:
    print ("Enter a grade between 0-100")
