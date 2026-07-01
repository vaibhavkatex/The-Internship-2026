
try:
    a = int(input("Enter a 1st Number: "))
    b = int(input("Enter a 2st Number: "))
    c = a / b
    print("Division :", c)

 # Handle ValueError and ZeroDivisionError.   
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

else:
    print("Division performed successfully!")


finally:
    print("Program execution completed.")
