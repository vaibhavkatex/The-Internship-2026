# S1Q10.py - Debugging Python Code

# Fixes made:
# 1. Added '=' to 'age = 20'
# 2. Wrapped "Amsterdam" in double quotes
# 3. Added space in "My name is "
# 4. Added commas in print statements to avoid syntax errors

# Corrected code
Name = "Alice"
age = 20
city = "Amsterdam"

print("My name is " + Name)
print("I am", age, "years old")
print("I live in", city)

# Check if adult (fixed: added comma)
print("Adult:", age > 18)
