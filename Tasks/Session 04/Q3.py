# For loop is used for repeating a tasks a specific number of times. It is used when the number of iterations is known beforehand. The syntax of a for loop in Python is as follows:

print("Numbers from 1 to 25:") 
for i in range(1, 26): 
    print(i) 
tot = 0 

for i in range(1, 21): 
    tot += i 

print("Sum of numbers from 1 to 20 =", tot) 
print("Table of 5:") 

for i in range(1, 11): 
    print(f"5 x {i} = {5 * i}") 
