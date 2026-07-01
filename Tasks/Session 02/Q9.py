# Q9.py - Menu driven calculator

while True:
    print("\nCalculator Menu")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        print("Exiting Calculator...")
        break
        
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == 1:
        print("Result =", num1 + num2)
    elif choice == 2:
        print("Result =", num1 - num2)
    elif choice == 3:
        print("Result =", num1 * num2)
    elif choice == 4:
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result =", num1 / num2)
    else:
        print("Invalid Choice")
