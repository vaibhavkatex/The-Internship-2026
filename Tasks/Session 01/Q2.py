# S1Q2.py - Core Data Types & Typecasting

# Creating variables of core types
my_string = "Hello AIML"
my_integer = 15
my_float = 9.81
my_boolean = False

# Printing variables and their types
print("String:", my_string, "| Type:", type(my_string))
print("Integer:", my_integer, "| Type:", type(my_integer))
print("Float:", my_float, "| Type:", type(my_float))
print("Boolean:", my_boolean, "| Type:", type(my_boolean))

print("\n--- Type Conversion ---")
# Converting types
converted_int_to_float = float(my_integer)
converted_float_to_int = int(my_float)

print("Int to Float:", converted_int_to_float)
print("Float to Int (Truncated):", converted_float_to_int)
