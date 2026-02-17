def factorial(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a


def pow_five(n):
    while n%5==0:
        n//=5
    return n==1
