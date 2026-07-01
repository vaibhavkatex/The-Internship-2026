import random 

print("five random integers:") 

for i in range(5): 
    print(random.randint(1, 100)) 
print("Random Number between 50 and 150:", random.randint(50, 150)) 
print("Random Floating Number:", random.random()) 