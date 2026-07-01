
# Contact Management System

contacts = {}

# Take input from user
name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

# Store contact information
contacts[name] = {
    "phone": phone,
    "email": email
}

# Search contact using get()
search_name = input("\nEnter name to search: ")

contact = contacts.get(search_name)

if contact:
    print("\nContact Found:")
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
else:
    print("Contact not found.")

# Print all contacts using items()
print("\nAll Contacts:")

for name, details in contacts.items():
    print("Name:", name)
    print("Phone:", details["phone"])
    print("Email:", details["email"])
    print()