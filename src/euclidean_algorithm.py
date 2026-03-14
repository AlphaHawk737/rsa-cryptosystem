def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, m):
    gcd, x, _ = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} mod {m} since gcd is {gcd}")
    return x % m