def welcome(name):
    print("=" * 40)
    print(f"Welcome {name}!")
    print("MISSION 2030 CALCULATOR")
    print("=" * 40)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Cannot divide by zero." 
    return a / b

welcome("Soorya")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit") 

    choice = int(input("\nEnter your choice (1-5): "))

    if choice == 5:
        print("Thank you for using Mission 2030 Calculator!")
        break

    if 1 <= choice <= 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Answer =", add(num1, num2))

        elif choice == 2:
            print("Answer =", subtract(num1, num2))

        elif choice == 3:
            print("Answer =", multiply(num1, num2))

        elif choice == 4:
            print("Answer =", divide(num1, num2))

    else:
        print("Invalid choice!")