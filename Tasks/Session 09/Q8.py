# Q8. (fromkeys() and Membership)

# Create a dictionary with default value None
keys = ["name", "age", "city"]
person = dict.fromkeys(keys, None)

# Take user input
person["name"] = input("Enter your name: ")
person["age"] = input("Enter your age: ")
person["city"] = input("Enter your city: ")

# Print dictionary
print("\nDictionary:", person)

# Check if a key exists
key = input("\nEnter a key to check: ")

if key in person:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the Dictionary.")