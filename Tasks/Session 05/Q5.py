
# a) To print numbers from 0 to 10, we can use range() with a single argument which specifies the end of the range (exclusive). The start is by default 0 and the step is by default 1.
print("Numbers from 0 to 10:")
for i in range(11):  # This will generate numbers from 0 to 10 (11 is exclusive)
    print(i)

# b) To print numbers from 5 to 15, we can use range() with two arguments: the start and the end. The start is inclusive and the end is exclusive.
print("Numbers from 5 to 15:")
for i in range(5, 16):  # This will generate numbers from 5 to 15 (16 is exclusive)
    print(i)

# c) To print odd numbers from 1 to 21, we can use range() with three arguments: the start, the end, and the step. The step is set to 2 to get only odd numbers.
print("Odd numbers from 1 to 21:")
for i in range(1, 22, 2):  # This will generate odd numbers from 1 to 21 (22 is exclusive)
    print(i)