# Math Utility Program - Combined Concepts
import math
import random

# Lambda function for square
square = lambda x: x ** 2

# Function for power calculation
def calculate_power(base, exp):
    return math.pow(base, exp)

# Function for random number
def generate_random():
    return random.randint(1, 100)

# Main program
while True:
    print("\n1. Square  2. Power  3. Random  4. Exit")
    choice = input("Choice: ")
    
    if choice == '1':
        num = float(input("Enter number: "))
        print(f"Square = {square(num)}")
    elif choice == '2':
        base = float(input("Base: "))
        exp = float(input("Exponent: "))
        print(f"Power = {calculate_power(base, exp)}")
    elif choice == '3':
        print(f"Random = {generate_random()}")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

