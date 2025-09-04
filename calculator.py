
def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Operations: +, -, *, /")
    op = input("Choose operation: ")
    result = None
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b != 0:
            result = a / b
        else:
            result = "Division by zero error"
    else:
        result = "Invalid operation"
    print(f"Result: {result}")

calculator()
