
# Creating a set
s = {100, 200, 300, 400, 500}

# Use pop() to remove and print one element.
removed_element = s.pop()
print("Removed element:", removed_element)


# Print the set after popping.
print("Set after pop :",s)

# Clear the entire set using clear().
s.clear()

# Print the final empty set.
print("Final set :",s)


# remove(x):
# Removes the specified element.
# Raises KeyError if the element is not found.

# discard(x):
# Removes the specified element.
# Does not raise an error if the element is not found.

# pop():
# removes an arbitrary element (sets have no indexing, so there is no "last" element).