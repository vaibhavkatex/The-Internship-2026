# Q8.py - FizzBuzz from 1 to 40

# Loop through numbers 1 to 40
for num in range(1, 41):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

