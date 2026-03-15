def extended_euclidean_algorithm(a, b):
    if a == 0:  # return gcd and coefficients x,y for ax + by = gcd
        return b, 0, 1  # base case: gcd(b,0)=b and coefficients are (0,1)
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1  # back-substitute to compute current x
    y = x1  # y holds previous x1
    return gcd, x, y

def modular_inverse(a, m):
    gcd, x, _ = extended_euclidean_algorithm(a, m)  # compute inverse using extended Euclid
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} mod {m} since gcd is {gcd}")  # inverse only if gcd=1
    return x % m  # normalize to positive representative