
# Create two lists:
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# a) Using extend() to add list2 to list1.
list1.extend(list2)
print("Using extend() :",list1)

# b) Using append() to add list2 to a copy of list1
append_list = list1.copy()
append_list.append(list2)

print("Using append():", append_list)

# Difference:
# extend() adds each element of list2 individually to the end of list1.
# append() adds list2 as a single element (nested list) to list1.