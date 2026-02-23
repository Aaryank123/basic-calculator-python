def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero is not allowed."
    return a / b


def show_menu():
    print("\n🧮 Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("👉 Choose an operation (1-5): ")

        if choice == "5":
            print("👋 Exiting calculator. Bye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("❌ Invalid choice. Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print(f"✅ Result: {result}")


if __name__ == "__main__":
    main()