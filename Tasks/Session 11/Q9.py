
try:
    # Take input from the user and convert it to an integer
    num = int(input("Enter a number: "))

    # Divide 100 by the entered number
    result = 100 / num

    # Display the result
    print("Result:", result)

# Fix 1: Added a colon(:) after except ValueError
except ValueError:
    # This block runs if the user enters a non-numeric value
    print("Please enter a valid number.")

# Fix 2: Used a general except block with a colon (:)
except:
    # This block handles any other unexpected errors
    print("Some error occurred.")