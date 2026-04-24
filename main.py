"""Simple Calculator Module"""


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
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
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
            except ValueError as e:
                print("Invalid input. Please enter valid numbers.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
