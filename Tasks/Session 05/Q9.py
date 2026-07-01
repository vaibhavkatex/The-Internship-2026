# Q9. (Slicing + range())
#  Write a program that prints the following using range() and string slicing concepts
# where applicable:
# •	First 10 even numbers (2 to 20).
# •	Numbers from 1 to 30 in steps of 3.
# •	A string "PythonProgramming" sliced to show "Python", "Programming", and the reverse.

# a) To print the first 10 even numbers from 2 to 20, we can use range() with a step of 2 starting from 2.
print("First 10 even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i)
    
# b) To print numbers from 1 to 30 in steps of 3, we can use range() with a step of 3 starting from 1.
print("Numbers from 1 to 30 in steps of 3:")
for i in range(1, 31, 3):
    print(i)

# c) To slice the string "PythonProgramming", we can use string indexing.
user_string = "PythonProgramming"
print(f"Original string: {user_string}")
print(f"First 6 characters: {user_string[0:6]}")
print(f"Last 11 characters: {user_string[6:17]}")
print(f"Reversed string: {user_string[::-1]}")