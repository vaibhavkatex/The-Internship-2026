
person= {"name": "Priya", "age": 21, "profession": "Engineer"}

# a) Using get() to access "age" and a non-existing key "salary"
print(person.get("age"))
print(person.get("salary", "Not Found"))

# b) Print all keys
print(person.keys())

# c) Print all values
print(person.values())

# d) Print all key-value pairs
print(person.items())