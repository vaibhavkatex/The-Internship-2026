# a) Empty dictionary using two different ways

# Method 1: Using {}
d1 = {}
print("d1 =", d1)
print("Type:", type(d1))

# Method 2: Using dict()
d2 = dict()
print("d2 =", d2)
print("Type:", type(d2))


# b) Dictionary with string keys
d3 = {
    "name": "Vaibhav",
    "city": "Washim",
    "course": "AI-ML"
}
print("\nd3 =", d3)
print("Type:", type(d3))


# c) Dictionary with integer keys
d4 = {
    1: "India",
    2: "China",
    3: "America",
    4: "Japan"
}
print("\nd4 =", d4)
print("Type:", type(d4))


# d) Mixed data type dictionary
d5 = {
    "Brand": "TATA",   # String
    "Wheels": 6,       # Integer
    "Distance": 129.0  # Float
}
print("\nd5 =", d5)
print("Type:", type(d5))