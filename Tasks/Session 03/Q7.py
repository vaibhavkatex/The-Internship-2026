"""This program calculates the area and perimeter of a rectangle using user-provided dimensions."""

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of Rectangle =", area)
print("Perimeter of Rectangle =", perimeter)
 