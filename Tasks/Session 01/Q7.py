# S1Q7.py - Rectangle Area & Perimeter

"""
Calculates area and perimeter of a rectangle
based on user length and width.
"""

# Dimensions can have decimals, so we use float
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Area = length * width
area = length * width

# Perimeter = 2 * (length + width)
perimeter = 2 * (length + width)

print(f"\nArea: {area} sq units")
print(f"Perimeter: {perimeter} units")
