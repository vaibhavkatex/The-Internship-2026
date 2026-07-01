# Create a class Person
class Person:

    # Fixed: Added self parameter
    def __init__(self, name, age):

        # Fixed: Store values in object attributes
        self.name = name
        self.age = age

    # Fixed: Added self parameter
    def introduce(self):

        # Fixed: Correct print syntax and use object attributes
        print("My name is", self.name, "and I am", self.age, "years old.")


# Create object
p1 = Person("Rahul", 25)

# Call method
p1.introduce()