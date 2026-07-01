# S1Q5.py - Input/Output & Typecasting

# Getting user inputs
name = input("Enter your name: ")
birth_year_str = input("Enter your birth year: ")

# input() returns string, so we convert birth_year to int for calculation
birth_year = int(birth_year_str)
age = 2026 - birth_year

print(f"\nHello {name}!")
print(f"Your age in 2026 will be {age} years.")
