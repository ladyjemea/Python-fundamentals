def display_menu():
    print("Welcome to the Python Calculator!")
    print("Please select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    
def get_operation():
    while True:
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate(choice, num1, num2):
    if choice == '1':
        return num1 + num2
    elif choice == '2':
        return num1 - num2
    elif choice == '3':
        return num1 * num2
    elif choice == '4':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    elif choice == '5':
        return num1 % num2
    elif choice == '6':
        return num1 ** num2

def main():
    display_menu()
    choice = get_operation()
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    result = calculate(choice, num1, num2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()