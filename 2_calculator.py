import math

print("🔬 Scientific Calculator 🔢")
print("Available operations: +, -, *, /, %, ^, sqrt, sin, cos, tan, log")

operator = input("Enter the operator: ")

if operator in ['+', '-', '*', '/', '%', '^']:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if operator == '+':
        print(f"Answer = {num1 + num2}")
    elif operator == '-':
        print(f"Answer = {num1 - num2}")
    elif operator == '*':
        print(f"Answer = {num1 * num2}")
    elif operator == '/':
        if num2 == 0:
            print("❌ Cannot divide by zero.")
        else:
            print(f"Answer = {num1 / num2}")
    elif operator == '%':
        print(f"Answer = {num1 % num2}")
    elif operator == '^':
        print(f"Answer = {math.pow(num1, num2)}")

elif operator in ['sqrt', 'sin', 'cos', 'tan', 'log']:
    num = float(input("Enter the number: "))

    if operator == 'sqrt':
        print(f"Answer = {math.sqrt(num)}")
    elif operator == 'sin':
        print(f"Answer = {math.sin(math.radians(num))}")
    elif operator == 'cos':
        print(f"Answer = {math.cos(math.radians(num))}")
    elif operator == 'tan':
        print(f"Answer = {math.tan(math.radians(num))}")
    elif operator == 'log':
        if num <= 0:
            print("❌ Logarithm undefined for zero or negative numbers.")
        else:
            print(f"Answer = {math.log10(num)}")

else:
    print("❌ Invalid operator! Please choose a valid one.")
