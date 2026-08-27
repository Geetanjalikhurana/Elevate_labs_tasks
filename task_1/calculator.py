"""
Calculator CLI App
-------------------
A command-line calculator supporting basic arithmetic operations (+, -, *, /)
with robust error handling and interactive user input loops.
"""

import sys

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the division of a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def power(a: float, b: float) -> float:
    """Returns a raised to the power of b."""
    return a ** b

def modulus(a: float, b: float) -> float:
    """Returns the remainder of division of a by b."""
    if b == 0:
        raise ValueError("Modulus by zero is not allowed.")
    return a % b


def get_number(prompt: str) -> float:
    """Prompts user for a numeric input until a valid number is provided."""
    while True:
        try:
            val = input(prompt).strip()
            return float(val)
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 5, 3.14, -10).")


def display_menu():
    """Prints the main interactive menu options."""
    print("\n" + "=" * 40)
    print("        CLI CALCULATOR APP")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    print("=" * 40)


def main():
    """Main CLI execution loop."""
    print("Welcome to the Command-Line Calculator!")
    
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        
        if choice in ('7', 'exit', 'quit', 'q'):
            print("\nThank you for using Calculator CLI. Goodbye!")
            sys.exit(0)
            
        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid choice! Please select a valid option from 1 to 7.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
                op_symbol = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op_symbol = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op_symbol = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op_symbol = '/'
            elif choice == '5':
                result = power(num1, num2)
                op_symbol = '^'
            elif choice == '6':
                result = modulus(num1, num2)
                op_symbol = '%'

            # Format integer outputs without trailing zeros (e.g., 5.0 -> 5)
            if isinstance(result, float) and result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result

            if isinstance(num1, float) and num1.is_integer():
                num1_str = str(int(num1))
            else:
                num1_str = str(num1)

            if isinstance(num2, float) and num2.is_integer():
                num2_str = str(int(num2))
            else:
                num2_str = str(num2)

            print(f"\n---> Result: {num1_str} {op_symbol} {num2_str} = {formatted_result}")

        except ValueError as err:
            print(f"\n---> Error: {err}")

        input("\nPress Enter to continue...")


if __name__ == '__main__':
    main()
