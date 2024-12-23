def calculator():
    # Function to get a valid number from the user
    def get_number(prompt):
        while True:
            try:
                return float(input(prompt))  # Attempt to convert input to float
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
        # Display the calculator menu
        print("Welcome to the Simple Calculator!")
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        # Get the user's operation choice
        operation = input("Enter the number of the operation (1/2/3/4): ")

        # Validate the operation choice
        if operation not in ('1', '2', '3', '4'):
            print("Invalid operation choice. Please try again.")
            continue

        # Get the two numbers from the user
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        # Perform the chosen operation
        if operation == '1':
            result = num1 + num2
            operator = '+'
        elif operation == '2':
            result = num1 - num2
            operator = '-'
        elif operation == '3':
            result = num1 * num2
            operator = '*'
        elif operation == '4':
            # Handle division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
            operator = '/'

        # Display the result
        print(f"{num1} {operator} {num2} = {result}")

        # Ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            print("Thank you for using the Simple Calculator. Goodbye!")
            break

# Entry point of the program
if __name__ == "__main__":
    calculator()
