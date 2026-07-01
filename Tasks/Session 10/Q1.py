

# Create a class named Car with:
class Car:
    # Attributes: brand and model (set using __init__).
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

# A method display_info() that prints the brand and model.
    def display_info(self):
        print(f"Brand: {self.Brand}, Model: {self.Model}")


# Initialize two Car objects and call the method for both
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display_info()
car2.display_info()
 
        