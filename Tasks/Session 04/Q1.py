# Lambda Function 

square = lambda x: x * x 
number = float(input("Enter a any number: "))

print("Square using lambda:", square(number)) 

# Normal Function

def square_def(x):
    return x * x

print("Square using normal function:", square_def(number)) 