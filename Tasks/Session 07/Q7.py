
# Creating a Tuple
grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

# Count and print how many times 'A' appears.
print("A Appears :",grades.count('A'),"Times")

# Count and print how many times 'B' appears.
print("B is Appears :",grades.count('B'),"Times")

# Take a grade as input from the user and print how many times it appears.

grade = input("Enter the grade to search: ")

count = grades.count(grade)

print(f"{grade} appears {count} time(s) in the tuple.")
