# Q4.py - For loop using range functions

# range(1, 31) generates values from 1 to 30
print("Numbers from 1 to 30:")
for i in range(1, 31):
    print(i)
print("------------------")

# range(1, 51, 2) starts at 1, goes up to 50, increments by 2
print("Odd numbers from 1 to 50:")
for i in range(1, 51, 2):
    print(i)
print("------------------")

# Calculating sum of numbers from 1 to 15
total = 0
for i in range(1, 16):
    total += i
print("Sum =", total)
