
try:
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))

    c = a / b
    print("Division:", c)

except ValueError:
    print("Please enter only numbers.")
