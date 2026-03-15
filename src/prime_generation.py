import random

def is_prime(n):    
    if n < 2:
        return False  # numbers less than 2 are not prime

    if n == 2:
        return True  # 2 is prime

    if n % 2 == 0:
        return False  # even numbers >2 are not prime

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False  # divisible by an odd factor
        i += 2  # test only odd divisors

    return True  # no divisors found


def generate_prime(start=100, end=1000):
    while True:
        candidate = random.randint(start, end)  # random candidate in range

        if is_prime(candidate):
            return candidate  # return the first prime found


def check_identical_primes():
    p = generate_prime()  # generate first prime
    q = generate_prime()  # generate second prime

    while p == q:
        q = generate_prime()  # avoid identical primes

    return p, q  # return distinct primes