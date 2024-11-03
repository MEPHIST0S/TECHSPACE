def Total(num1, num2, z):
    return "{:.{}f}".format(num1 + num2, z)

def Multiplication(num1, num2, z):
    return "{:.{}f}".format(num1 * num2, z)

def Division(num1, num2, z):
    return "{:.{}f}".format(num1 / num2, z)

def Subtraction(num1, num2, z):
    return "{:.{}f}".format(num1 - num2, z)

while True:
    num1, num2 = map(float, input("Enter Numbers: ").split())
    operation = input("Enter Operation: ")

    if operation == "+":
        z = int(input("Enter Amount of Digits after Comma: "))
        print(Total(num1, num2, z))
    elif operation == "*":
        z = int(input("Enter Amount of Digits after Comma: "))
        print(Multiplication(num1, num2, z))
    elif operation == "/":
        z = int(input("Enter Amount of Digits after Comma: "))
        print(Division(num1, num2, z))
    elif operation == "-":
        z = int(input("Enter Amount of Digits after Comma: "))
        print(Subtraction(num1, num2, z))
    else:
        print("Invalid operation")

    resume = input("Do you want to continue? (yes/no): ").strip().lower()
    if resume != 'yes':
        break

print("Session ended.")