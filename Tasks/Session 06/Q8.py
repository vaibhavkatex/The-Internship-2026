# Create a list: marks = [45, 78, 65, 90, 34, 82, 71]
marks = [45, 78, 65, 90, 34, 82, 71]

# Sort the list in ascending order and print it.
marks = [85, 92, 78, 65, 88]
sorted_list = sorted(marks)
print(sorted_list)


# Sort the list in descending order and print it.
sorted_list = sorted(marks, reverse=True)
print(sorted_list)

# Reverse the original list (without sorting) and print it.
Reversed_list=marks[::-1]
print(Reversed_list)

# Add comments on the difference between sort() and reverse().
# reverse() reverses the order of elements in the original list.

# sort() method arranges the elements of a list in ascending order by default.
# It modifies the original list and does not return a new list.