
#Creating a List
fruits = ["apple", "banana", "mango", "orange", "grape"]

# Access frist items 
print("frist item :",fruits[0])

# Access Third items
print("Third item :",fruits[2])


# Access Last item (using negative index)
print("Last item (using negative index) :",fruits[-1])

# Access Second last item (using negative index)
print("Second Last item (using negative index) :",fruits[-2])

# Take a number as input from the user and print the item at that index (handle basiccases only).
num = int(input("Enter The Number: "))
    
print("Item at index", num, ":", fruits[num-1])



