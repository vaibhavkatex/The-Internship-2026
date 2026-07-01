# # Question 9
# (Immutability of Tuples)
# Create a tuple: coordinates = (10, 20)
# Demonstrate that tuples are immutable by trying to:
# Change the first element
# Add a new element using append()
# Explain what errors occur (in comments). Then show the correct way to modify
# data by converting the tuple to a list, making changes, and converting back to a
# tuple.


# Create a tuple
coordinates = (10, 20)

print("Original Tuple:", coordinates)

# -------------------------------------------------
# Attempt 1: Change the first element
# -------------------------------------------------

#coordinates[0] = 100

# Original Tuple: (10, 20)
# Traceback (most recent call last):
#   File "c:\Users\sdf\Desktop\ITR2026\Tasks\Session 07\Q9.py", line 21, in <module>
#     coordinates[0] = 100
# TypeError: 'tuple' object does not support item assignment
# Reason:
# Tuples are immutable, so their elements cannot be changed after creation.


# -------------------------------------------------
# Attempt 2: Add a new element using append()
# -------------------------------------------------

# coordinates.append(30)

# Error:
# AttributeError: 'tuple' object has no attribute 'append'
# Reason:
# Tuples do not have methods like append(), insert(), or remove().


# -------------------------------------------------
# Correct Way: Convert tuple to list, modify, then convert back
# -------------------------------------------------

# Convert tuple to list
coordinates_list = list(coordinates)

# Modify data
coordinates_list[0] = 100
coordinates_list.append(30)

# Convert back to tuple
coordinates = tuple(coordinates_list)

print("Modified Tuple:", coordinates)