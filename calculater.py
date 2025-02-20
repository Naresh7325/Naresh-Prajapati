# Simple Calculator

def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        # Get user choice
        choice = int(input("Enter the number of your choice (1/2/3/4): "))

        # Check for valid choice
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            return

        # Get input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if choice == 1:
            result = num1 + num2
            operation = "Addition"
        elif choice == 2:
            result = num1 - num2
            operation = "Subtraction"
        elif choice == 3:
            result = num1 * num2
            operation = "Multiplication"
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "Division"

        # Display the result
        print(f"Result of {operation}: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

# Run the calculator
calculator()
