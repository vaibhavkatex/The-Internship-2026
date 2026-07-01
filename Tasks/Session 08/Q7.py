

# Creating Sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# UNION
# Union combines all unique elements from both sets.
union1 = A.union(B)
union2 = A | B

print("Union using union():", union1)
print("Union using | operator:", union2)

# INTERSECTION
# Intersection returns only the common elements present in both sets.
intersection1 = A.intersection(B)
intersection2 = A & B

print("Intersection using intersection():", intersection1)
print("Intersection using & operator:", intersection2)