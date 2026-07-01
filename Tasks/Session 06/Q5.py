

# Start with an empty list
l1 = []

# Use append() to add 5 city names
l1.append("Washim")
l1.append("Akola")
l1.append("Goa")
l1.append("Amravati")
l1.append("Thane")

# Use insert() to add one more city at position 2
l1.insert(2, "Mumbai")

# Take user input for at least 2 cities
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

l1.append(city1)
l1.append(city2)

# Print final list
print("Final List:", l1)