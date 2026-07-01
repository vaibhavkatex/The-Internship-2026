

# Create a dictionary with 5 key-value pairs
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 88,
    "grade": "A",
    "city": "Mumbai"
}

# Remove and print the last inserted item
removed_item1 = student.popitem()
print("First removed item:", removed_item1)

# Remove and print the next last inserted item
removed_item2 = student.popitem()
print("Second removed item:", removed_item2)

# Print dictionary after popitem()
print("Dictionary after popitem():", student)

# Clear the entire dictionary
student.clear()

# Print final result
print("Final Dictionary:", student)

# Difference between pop() and popitem():
# pop(key) -> Removes a specific key and returns its value.

# popitem() -> Removes the last inserted key-value pair
