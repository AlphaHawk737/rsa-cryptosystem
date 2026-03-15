import math
from src.prime_generation import check_identical_primes
from src.euclidean_algorithm import modular_inverse

def generate_rsa_keys():
    p, q = check_identical_primes()  # choose two primes p and q
    n = p * q  # modulus n
    phi = (p - 1) * (q - 1)  # Euler totient phi(n)
    e = 65537  # standard public exponent
    if math.gcd(e, phi) != 1:
        e = 3  # fallback small exponent if not coprime
        while math.gcd(e, phi) != 1:
            e += 2  # find odd e coprime with phi(n)
    d = modular_inverse(e, phi)  # private exponent d
    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "e": e,
        "d": d,
        "public_key": (e, n),
        "private_key": (d, n),
    }

def display_key_generation(keys):
    print("\nRSA Key Generation\n")
    print(f"p = {keys['p']}")
    print(f"q = {keys['q']}")
    print("\nComputed values\n")
    print(f"n = {keys['n']}")
    print(f"phi(n) = {keys['phi']}")
    print("\nKey parameters\n")
    print(f"e = {keys['e']}")
    print(f"d = {keys['d']}")
    print("\nKeys\n")
    print(f"Public Key (e, n) = {keys['public_key']}")
    print(f"Private Key (d, n) = {keys['private_key']}")

if __name__ == "__main__":
    keys = generate_rsa_keys()  # generate RSA keys when run directly
    display_key_generation(keys)  # print keys for demonstration