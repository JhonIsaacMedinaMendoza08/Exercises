#Write a program that calculates an employee's net salary after applying taxes.

print (""" 
---------------------------------------------------------
-----------------Exercise 15 Salary----------------------
---------------------------------------------------------""")

def salarioNeto ():
    grossSalary = float(input("Enter your salary before taxes: "))
    country = input("Enter your country (Country A, Country B, Country C): ")
    match country.lower():
        case "a" | "country a" :
            taxes = 0.20
        case "b" | "country b":
            taxes = 0.15
        case "c" | "country c":
            taxes = 0.10
        case _:
            taxes = 0.25
        
    finalTaxes = grossSalary * taxes
    finalSalary = grossSalary - finalTaxes

    print (f"Your final salary is : {finalSalary}")

salarioNeto()