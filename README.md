# 🧮 Simple Calculator (Python)

Author : M.S.MEYSINTHA

A beginner-friendly Python program that works as a menu-driven calculator.
It allows the user to perform basic arithmetic operations:

➕ Addition

➖ Subtraction

✖️ Multiplication

➗ Division

# 📂 Features

Easy-to-use menu interface

Handles division by zero

Supports both integer and decimal numbers

Beginner-friendly code structure

# 📜 Code Example
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

# ▶️ Example Run
Simple Calculator
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1-4): 1
Enter first number: 12
Enter second number: 8
Result: 20.0

# ⚡ How to Run

Clone this repository:

git clone https://github.com/your-username/simple-calculator.git
cd simple-calculator


# Run the program:

python calculator.py

# output



# 📌 Future Improvements

Add power, modulus, and square root functions

Implement a GUI (Tkinter/Flask/Streamlit) version

Add error handling for invalid inputs
