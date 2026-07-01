
# a) A set with 5 integers.
set1 = {1, 2, 3, 4, 5}
print(type(set1), set1)

# b) A set with mixed data types (integer, string, float).
set2 = {1, "Vaibhav", 1.2}
print(type(set2), set2)

# c) An empty set using the correct method.
empty_set = set()
print(type(empty_set), empty_set)

# d) A set from the string "hello" using the set() constructor.
set4 = set("hello")
print(type(set4), set4)

# Sets automatically remove duplicates because a set stores only unique values.
# Example:
duplicate_set = {1, 2, 2, 3, 3, 4}
print(duplicate_set)