#Write a program that prompts the user for a string of text and counts how many vowels (a, e, i, o, u) it contains. 
# Use a for loop to iterate through the string and perform the count.
print(""" 
---------------------------------------------------------
---------Exercise 2 Iterative Structures-----------------
---------------------------------------------------------""")

text = input("Enter a text string: ")
number_of_vowels = 0
vowels = "aeiouAEIOU"
for i in text:
    if i in vowels: 
        number_of_vowels += 1
print(f"The number of vowels in the chain is: {number_of_vowels}")