# Q10.py - Debugged python code with fixes

# Convert input to integer because input() returns a string
num = int(input("Enter a number: "))

# Added missing colons (:) to if-elif-else statements
if num > 100:
    print("Large number")
elif num > 50:
    print("Medium number")
else:
    print("Small number")

count = 1

# Added missing colon (:) to while statement
while count < 10:
    print(count)
    # Corrected count increment syntax
    count += 1
