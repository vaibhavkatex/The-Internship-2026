# (Membership Testing)
# Write a program that:
# Takes a set of 5 colors as input from the user.
# Asks the user to enter a color name.
# Checks whether the color is present in the set using in and not in.
# Prints appropriate messages.


# Takes a set of 5 colors as input from the user.
colors = set()
for i in range(5):
    color = input("Enter a color: ")
    colors.add(color)

# Asks the user to enter a color name.
search_color = input("Enter a color to search: ")

# Checks whether the color is present in the set using in and not in.
if search_color in colors:
    print(f"'{search_color}' is present in the set.")
else:
    print(f"'{search_color}' is not present in the set.")