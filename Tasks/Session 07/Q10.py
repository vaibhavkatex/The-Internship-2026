# Q10. (Mini Project - Combined Concepts)
# Student Record Program using Tuples

# Take input from the user

name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))

mark1 = int(input("Enter Subject 1 Marks: "))
mark2 = int(input("Enter Subject 2 Marks: "))
mark3 = int(input("Enter Subject 3 Marks: "))

# Store all information in a tuple (Packing)
student = (name, roll_no, mark1, mark2, mark3)

# Print complete record
print("\n===== Student Record =====")
print(student)

# Unpack the tuple
name, roll_no, mark1, mark2, mark3 = student

# Print values with labels

print("\n===== Student Details =====")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Subject 1  :", mark1)
print("Subject 2  :", mark2)
print("Subject 3  :", mark3)

# Count how many times a mark appears
search_mark = int(input("\nEnter a mark to count: "))

count_mark = student.count(search_mark)

print(f"{search_mark} appears {count_mark} time(s) in the record.")

# Create Nested Tuple (Multiple Students)
student1 = student

student2 = ("Rahul",102,85,90,88)

students = (student1, student2)

# Print Nested Tuple
print("\n===== All Student Records =====")
print(students)

# Access Specific Values
print("\n===== Accessing Specific Values =====")

# First student's name
print("First Student Name :", students[0][0])

# Second student's roll number
print("Second Student Roll No :", students[1][1])

# Second student's Subject 2 marks
print("Second Student Subject 2 Marks :", students[1][3])