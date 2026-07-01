

student = ('Rahul', 20, 'Computer Science', 'A')

# a) Iterating
print("Tuple Elements:")
for item in student:
    print(item)

# b) Unpacking
name, age, branch, grade = student

print("\nStudent Details:")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("Grade:", grade)