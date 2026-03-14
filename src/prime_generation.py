import random

def is_prime(n):
    """Check if a number is prime using trial division."""
    
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True



def generate_prime(start=100, end=1000):
    """Generate a random prime number in a range."""
    
    while True:
        candidate = random.randint(start, end)

        if is_prime(candidate):
            return candidate
        
def check_identical_primes():
    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    return p, q