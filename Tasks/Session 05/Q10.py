

# Take a string input from the user
input_string = input("Enter a string: ")


# 1. Print length of the string
string_length = len(input_string)
print("Length of the string:", string_length)


# 2. Print first half and second half using slicing
half_index = string_length // 2
first_half = input_string[:half_index]
second_half = input_string[half_index:]
print("First half of the string:", first_half)
print("Second half of the string:", second_half)


# 3. Check if the word "python" (case insensitive) is present
if "python" in input_string.lower():
    print("The word 'python' is present in the string.")
else:
    print("The word 'python' is not present in the string.")


# 4. Use range() to print all characters with their positive and negative indices
print("Characters with positive and negative indices:")
for i in range(string_length):
    print(f"Index {i}: {input_string[i]} (Negative Index: {i - string_length})")



# 5. Print the string in reverse
reversed_string = input_string[::-1]    
print("String in reverse:", reversed_string)


