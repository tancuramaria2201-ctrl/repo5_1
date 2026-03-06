def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def is_power_of_5(n):
    while n % 5 == 0 and n > 1:
        n = n / 5
    return n == 1