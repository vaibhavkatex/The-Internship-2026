import math

# Get numeric input from user
value = float(input("Enter a number: "))

# Calculate square root (only for non-negative values)
if value < 0:
	print("Square Root = Not defined for negative numbers")
else:
	print("Square Root =", math.sqrt(value))

# Calculate and display ceiling and floor values
print("Ceiling Value =", math.ceil(value))
print("Floor Value =", math.floor(value))

# Calculate factorial (only for non-negative integers)
if value >= 0 and value.is_integer():
	print("Factorial =", math.factorial(int(value)))
else:
	print("Factorial can only be calculated for non-negative integers.")