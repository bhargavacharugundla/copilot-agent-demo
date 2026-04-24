"""Simple Calculator Module"""


def validate_numeric_input(value):
    """
    Validate if input is numeric (integer or float).
    
    Args:
        value: String input to validate
        
    Returns:
        tuple: (is_valid, converted_value) where is_valid is bool and converted_value is float or None
    """
    try:
        numeric_value = float(value)
        return True, numeric_value
    except ValueError:
        return False, None


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers with zero check"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_numeric_input(prompt):
    """
    Repeatedly prompt user until valid numeric input is received.
    
    Args:
        prompt: String to display as input prompt
        
    Returns:
        float: Valid numeric input from user
    """
    while True:
        user_input = input(prompt)
        is_valid, value = validate_numeric_input(user_input)
        
        if is_valid:
            return value
        else:
            print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")


def main():
    """Main calculator interface"""
    print("Simple Calculator")
    print("================")
    
    while True:
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = get_numeric_input("Enter first number: ")
                num2 = get_numeric_input("Enter second number: ")
                
                if choice == "1":
                    print(f"Result: {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {divide(num1, num2)}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
