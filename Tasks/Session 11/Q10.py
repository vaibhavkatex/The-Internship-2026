
while True:
    print("\n===== Simple Calculator ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you! Calculator Closed.")
        break

    try:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            print("Result:", num1 / num2)

        else:
            print("Invalid Choice! Please enter 1 to 5.")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    finally:
        print("Operation attempted.")