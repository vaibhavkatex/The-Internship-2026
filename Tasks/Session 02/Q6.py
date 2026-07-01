# Q6.py - Keep adding positive numbers until zero or negative is entered

total = 0.0

# Repeatedly take input until non-positive number is entered
while True:
    num = float(input("Enter a positive number: "))
    if num <= 0:
        break
    total += num

print("Total Sum =", total)
