
# Create a class Rectangle with attributes length and width.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

# area() — return the area.
    def area(self):
        return self.length * self.width

# perimeter() — return the perimeter.
    def perimeter(self):
        return 2 * (self.length + self.width)
# display() — print length, width, area, and perimeter.
    def display(self):
        print("\nLength:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


# Take input from user
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

# Create object
rect = Rectangle(length, width)

# Display results
rect.display()