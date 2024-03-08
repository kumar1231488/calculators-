def calculator():
    history = []

    while True:
        print("simple calculator:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting calculator...")
            break
        elif choice not in ('1', '2', '3', '4', '5'):
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print("Result: ", result)
            history.append((num1, '+', num2, result))
        elif choice == '2':
            result = num1 - num2
            print("Result: ", result)
            history.append((num1, '-', num2, result))
        elif choice == '3':
            result = num1 * num2
            print("Result: ", result)
            history.append((num1, '*', num2, result))
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                result = num1 / num2
                print("Result: ", result)
                history.append((num1, '/', num2, result))
        elif choice == '5':
            print("History:")
            for operation in history:
                print(f"{operation[0]} {operation[1]} {operation[2]} = {operation[3]}")

if __name__ == "__main__":
    calculator()