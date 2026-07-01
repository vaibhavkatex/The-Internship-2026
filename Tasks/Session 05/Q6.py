# Q6. (range() with Negative Step)
# Use range() to print:
# Numbers from 20 down to 10 (decreasing).
# Numbers from 15 down to 1 in steps of 2.
# Print each sequence on a new line with proper messages.

# a) To print numbers from 20 down to 10, we can use range() with three arguments: the start, the end, and the step. The start is 20, the end is 9 (since it's exclusive), and the step is -1 to decrease the numbers.
print("Numbers from 20 down to 10:")
for i in range(20, 9, -1):
    print(i)

# b) To print numbers from 15 down to 1 in steps of 2, we can use range() with three arguments: the start, the end, and the step. The start is 15, the end is 0 (since it's exclusive), and the step is -2 to decrease the numbers.
print("Numbers from 15 down to 1 in steps of 2:")
for i in range(15, 0, -2):
    print(i)