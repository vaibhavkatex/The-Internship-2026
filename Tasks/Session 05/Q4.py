
# Take a string input from the user
input_string = input("Enter a string: ")

# Print the length of the string using len()

print("The length of the string is:", len(input_string))

# Print the last character using len() (without using negative index)
print("The last character is:", input_string[len(input_string) - 1])

# Print the middle character if the length is odd
if len(input_string) % 2 == 1:
    middle_index = len(input_string) // 2
    print("The middle character is:", input_string[middle_index])
else:
    print("The string has an even length, so there is no single middle character.")