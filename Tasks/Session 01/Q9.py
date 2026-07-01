# S1Q9.py - Student Profile Generator

print("=== Student Profile Generator ===")

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

# Marks for three subjects
sub1 = float(input("Enter Subject 1 marks: "))
sub2 = float(input("Enter Subject 2 marks: "))
sub3 = float(input("Enter Subject 3 marks: "))

# Total and Percentage calculation
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

print("\n" + "="*30)
print("       STUDENT PROFILE       ")
print("="*30)
print(f"Name      : {name}")
print(f"Age       : {age} years")
print(f"City      : {city}")
print(f"Marks     : {sub1}, {sub2}, {sub3}")
print(f"Total     : {total}/300")
print(f"Percentage: {percentage:.2f}%")
print("="*30)
