def factorial(n):
    prod = 1

    for i in range(2, n+1):
        prod*=i
    
    return prod

def is_prime(n):
    
    for i in range(2, n**(1/2)+1):
        if n%i == 0:
            return False
    
    return True