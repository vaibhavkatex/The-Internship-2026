# Q8. (Membership with range())
#  Write a program that:
# •	Takes a number as input from the user.
# •	Checks if the number is present in range(1, 51) and in range(10, 100, 5).
# •	Prints clear messages for each check.

# Take a number as input from the user
number = int(input("Enter a number: "))

# Check if the number is in range(1, 51)
if number in range(1, 51):
    print(f"{number} is in the range(1, 51).")
else:
    print(f"{number} is not in the range(1, 51).")

# Check if the number is in range(10, 100, 5)
if number in range(10, 100, 5):
    print(f"{number} is in the range(10, 100, 5).")
else:
    print(f"{number} is not in the range(10, 100, 5).")