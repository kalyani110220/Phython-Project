# src/calculator.py

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers, handle division by zero"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def calculator():
    """Main function to perform calculator operations"""
    print("Welcome to Simple Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    while True:
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please choose 1–5.")
            continue

        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Perform calculation
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of addition: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of subtraction: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of multiplication: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of division: {result}")

        print("-" * 40)

if __name__ == "__main__":
    calculator()
