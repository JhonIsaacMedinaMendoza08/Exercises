#Use match to implement a simple calculator.

print (""" 
---------------------------------------------
--------Exercise 3 Simple calculator---------
---------------------------------------------""")
num1 = float(input("    Please enter the number: "))
symbol = str(input("    Enter the symbol (+, -, *, /): "))
num2 = float(input("    Please enter the number: "))
match symbol:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        resultado = num1 / num2
    case _:
        print("Invalid operation. Choose from ' + ', ' - ', ' * ' or ' / '.")            
print(f"""
---------------------------------------------
The result of the {symbol} is: {resultado}