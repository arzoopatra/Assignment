def calculator(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return "Error: Division by zero!" if num2 == 0 else num1 / num2
    else:
        return "Error: Invalid operator!"

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = calculator(num1, num2, operator)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
