def calculate_sum(a, b):
 return a + b  

result = calculate_sum(10, 20) 
print("Sum =", result)  

def add_print(a, b):    
    print("Sum inside function =", a + b)

    
    def add_return(a, b): 
        return a + b 
    add_print(5, 3)    
    ans = add_return(5, 3)  
    print("Returned Sum =", ans) 