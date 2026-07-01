class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def show_info(self):
        print("\nTitle :", self.title)
        print("Author:", self.author)
        print("Status:", self.status)


# List to store book objects
library = []

while True:

    print("\n===== Library Management System =====")
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(title, author)
        library.append(book)

        print("Book added successfully.")

    # Issue Book
    elif choice == "2":
        title = input("Enter Book Title to Issue: ")

        found = False

        for book in library:
            if book.title.lower() == title.lower():
                book.issue_book()
                found = True
                break

        if not found:
            print("Book not found.")

    # Return Book
    elif choice == "3":
        title = input("Enter Book Title to Return: ")

        found = False

        for book in library:
            if book.title.lower() == title.lower():
                book.return_book()
                found = True
                break

        if not found:
            print("Book not found.")

    # Show All Books
    elif choice == "4":

        if len(library) == 0:
            print("No books available.")

        else:
            for book in library:
                book.show_info()

    # Exit
    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")