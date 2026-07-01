

# Creating a Tuple
fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

# Find and print the first index of 'banana'.
print(" Frist Index Of a banana :",fruits.index('banana'))

# Find and print the first index of 'banana' starting the search from index 2.
print(" Frist Index Of a banana :",fruits.index('banana',2))

# Use try-except to safely find the index of 'kiwi' and print "Not found" if it
fruits = ('apple', 'banana', 'mango', 'orange')

try:
    index = fruits.index('kiwi')
    print("Index ofkiwi:", index)
except ValueError:
    print("Not found")