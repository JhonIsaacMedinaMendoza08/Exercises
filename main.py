print (""" 
---------------------------------------------------------
--------------------Exercise 14 -------------------------
---------------------------------------------------------""")

def guess_the_letter():
    secretletter = "j"
    while True:
        letter = input("Guess the secret letter: ").lower()
        match letter:
            case "j":
                print ("Congratulations! You found the secret letter")
                break
            case _:
                print ("Sorry, that's not the secret letter. Please try again.")
guess_the_letter()