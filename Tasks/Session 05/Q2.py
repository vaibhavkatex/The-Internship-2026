
# Take a string input from the user
name = input("Enter a String:")

# a) The first 5 characters can be accessed using slicing with start index 0 and end index 5 (exclusive)
print("The first 5 characters are:", name[0:5])

# b) The last 4 characters can be accessed using slicing with start index -4 and end index as the length of the string (exclusive)
print("last 4 characters are:", name[-4:])

# c) The string in reverse order can be accessed using slicing with start index as the length of the string, end index as -1 (exclusive), and step as -1 (to reverse the string)
print("The string in reverse order is:", name[::-1])

# d) Every 2nd character of the string can be accessed using slicing with start index 0, end index as the length of the string (exclusive), and step as 2 (to skip every 2nd character)
print("Every 2nd character of the string is:", name[0::2])