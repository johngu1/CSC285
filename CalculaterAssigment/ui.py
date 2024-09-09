from CalculaterAssigment.calculator import Calculator

def main_menu():
    print("\nWelcome to the calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")

def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def get_choice():
    return input("Enter your choice (1-5): ")

def run_calculator():
    calc = Calculator()

    while True:
        main_menu()
        choice = get_choice()

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            a, b = get_numbers()

            if choice == '1':
                result = calc.add(a, b)
                operation = '+'
            elif choice == '2':
                result = calc.subtract(a, b)
                operation = '-'
            elif choice == '3':
                result = calc.divide(a, b)
                operation = '/'
            elif choice == '4':
                result = calc.multiply(a, b)
                operation = '*'

            print(f"Result: {a} {operation} {b} = {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")