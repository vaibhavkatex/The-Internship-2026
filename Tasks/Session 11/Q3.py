
try:
    # Division
    a = int(input("Enter the 1st Number: "))
    b = int(input("Enter the 2nd Number: "))
    print("Division:", a / b)

    # String to Integer Conversion
    s = input("Enter a number in string form: ")
    num = int(s)
    print("Converted Integer:", num)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")





