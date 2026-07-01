

# Create a list: scores = [85, 92, 78, 92, 65, 92, 88]
scores = [85, 92, 78, 92, 65, 92, 88]

# Find and print the index of the first occurrence of 92.
indexof92=scores.index(92)
print("Index of first occurrence of 92:", indexof92)

# Count and print how many times 92 appears.
count_92 = scores.count(92)
print("92 appears", count_92, "times")

# Take a number as input from the user and check if it exists in the list. If yes, print its index and count.

# Take a number as input from the user
num = int(input("Enter a number: "))

# Check if the number exists in the list
if num in scores:
    print(num, "exists in the list.")
    print("Index:", scores.index(num))
    print("Count:", scores.count(num))
else:
    print(num, "does not exist in the list.")
