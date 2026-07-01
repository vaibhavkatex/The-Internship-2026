# Q7. (Combined: Strings + range())
#  Write a program that takes a string from the user.
# Using a for loop and range() with len(), print:
# •	Each character of the string one by one (with its index).
# •	The string in reverse order using negative step in range().

# Take a string input from the user
user_string = input("Enter a string: ")

# Print each character with its index
print("Characters with indices:")
for i in range(len(user_string)):
    print(f"Index {i}: {user_string[i]}")

# Print the string in reverse order
print("String in reverse order:")
for i in range(len(user_string) - 1, -1, -1):
    print(user_string[i], end="")
print()  # Print a newline at the end
