

students= {
    "s1": {"name": "Rahul", "age": 20, "marks": 88},
    "s2": {"name": "Sneha", "age": 21, "marks": 95}
}

# Print the details of the first student
print("First Student Details:")
print(students["s1"])

# Print the marks of the second student
print("Second Student Marks:")
print(students["s2"]["marks"])

# Add a new subject "math" with marks 90 for the first student
students["s1"]["math"] = 90

# Print updated first student details
print("Updated First Student Details:")
print(students["s1"])
