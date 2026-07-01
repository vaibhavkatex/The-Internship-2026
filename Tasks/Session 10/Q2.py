
# Write a class Book that takes title, author, and price as parameters in __init__.
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

# Create a method show_details() to print all the book information.
    def show_details(self):
        print("\nTitle:",self.title)
        print("Author:",self.author)
        print("price:",self.price)

# Create at least two book objects and display their details.
b1=Book("Atomic Habits","James Clear","590")
b2=Book("The Psychology of Money","Morgan Housel","290")

b1.show_details()
b2.show_details()