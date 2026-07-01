

# Taking 6 numbers as input and storing them in a set
s = set()

for i in range(6):
    num = int(input("Enter number :"))
    s.add(num)   # Duplicates will be removed automatically

# Adding two more numbers
s.add(int(input("Enter first extra number: ")))
s.add(int(input("Enter second extra number: ")))

# Removing one number safely using discard()
remove_num = int(input("Enter a number to remove: "))
s.discard(remove_num)

# Printing final set and its length
print("Final Set:", s)
print("Length of Set:", len(s))