
# Create a list: items = [10, 20, 30, 20, 40, 50]
items = [10, 20, 30, 20, 40, 50]

# a) Remove the first occurrence of 20 using remove().
items.remove(20)

# b) Remove the item at index 3 using pop() and print the removed value.
Removed_Value=items.pop(3)
print("Removed Value :",Removed_Value)

# c) Remove the last item using pop().
items.pop()

# d) Clear the entire list using clear().
items.clear()

# Dif remove() & pop()
# remove() removes an element by its VALUE.
# pop() removes an element by its INDEX (position).