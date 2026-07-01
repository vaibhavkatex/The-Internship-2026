# Q7. (copy() and setdefault())

# Create a dictionary
d = {"a": 1, "b": 2}

# Make a copy of the dictionary
d_copy = d.copy()

# Add key "c" with value 3 if it doesn't exist
d.setdefault("c", 3)

# Use setdefault() on existing key "a"
d.setdefault("a", 100)

# Print original and copied dictionaries
print("Original Dictionary:", d)
print("Copied Dictionary:", d_copy)