
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Error: Please enter a valid non-zero number.")