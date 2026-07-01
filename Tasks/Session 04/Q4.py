# Initialize sum variable
total = 0

# Loop until user enters non-positive number
while True:
    # Get number from user
    value = float(input("Enter a positive number (0 or negative to stop): "))
    
    # Exit loop if number is not positive
    if value <= 0:
        break
    
    # Add to running total
    total += value

# Display final sum
print("Total Sum =", total)