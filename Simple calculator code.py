def calculator():
    print("Simple Calculator")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = int(input("Enter choice (1-4): "))
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed")
    else:
        print("Invalid choice")

calculator()
