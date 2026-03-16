# RSA Key Generation

## 1. Introduction

**RSA Key Generation** is the process of creating a pair of public and private keys for the RSA cryptosystem. The security of the entire RSA system depends critically on the quality and correctness of key generation.

The process involves:
- Selecting two large prime numbers
- Computing their product (the modulus)
- Computing Euler's totient function
- Selecting the public exponent
- Computing the private exponent

This document covers the complete key generation process with mathematical foundations and practical implementation.

---

# 2. RSA Key Generation Steps

### Step 1: Select Two Large Prime Numbers

Choose two distinct, large prime numbers $p$ and $q$.

**Requirements**:
- Both should be large (typically 1024-2048 bits each)
- Should be distinct: $p \neq q$
- Should be randomly generated
- Should pass primality tests

**Why primes?** RSA security depends on the difficulty of factoring $n = pq$.

### Step 2: Compute the Modulus

$$
n = p \times q
$$

This is the modulus used in both encryption and decryption. The size of $n$ determines RSA key length (e.g., 2048-bit RSA uses a 2048-bit $n$).

### Step 3: Compute Euler's Totient

$$
\phi(n) = (p-1) \times (q-1)
$$

This value is essential for computing the private exponent and must be kept secret.

### Step 4: Select Public Exponent

Choose an integer $e$ such that:
- $1 < e < \phi(n)$
- $\gcd(e, \phi(n)) = 1$ (must be coprime to $\phi(n)$)

**Common choices**:
- $e = 65537 = 2^{16} + 1$ (most common due to efficiency)
- $e = 3$ (less common but faster)
- $e = 17$

### Step 5: Compute Private Exponent

Find $d$ such that:

$$
ed \equiv 1 \pmod{\phi(n)}
$$

This is computed using the **Extended Euclidean Algorithm**:

$$
d = e^{-1} \pmod{\phi(n)}
$$

### Step 6: Form Key Pairs

**Public Key**: $(e, n)$

**Private Key**: $(d, n)$

---

# 3. Key Generation Algorithm

```python
import random
from math import gcd

def is_prime(n, k=40):
    """Miller-Rabin primality test."""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def extended_gcd(a, b):
    """Extended Euclidean Algorithm."""
    if b == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y


def mod_inverse(a, m):
    """Compute modular inverse."""
    gcd_val, x, _ = extended_gcd(a, m)
    if gcd_val != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % m + m) % m


def generate_rsa_keys(key_size=2048):
    """
    Generate RSA public and private keys.
    
    Args:
        key_size: Size in bits of the modulus n
    
    Returns:
        ((e, n), (d, n)): Public and private keys
    """
    # Step 1: Generate two large primes
    p = random.getrandbits(key_size // 2)
    while not is_prime(p):
        p = random.getrandbits(key_size // 2)
    
    q = random.getrandbits(key_size // 2)
    while not is_prime(q) or q == p:
        q = random.getrandbits(key_size // 2)
    
    # Step 2: Compute modulus
    n = p * q
    
    # Step 3: Compute Euler's totient
    phi_n = (p - 1) * (q - 1)
    
    # Step 4: Select public exponent
    e = 65537
    while gcd(e, phi_n) != 1:
        e += 2
    
    # Step 5: Compute private exponent
    d = mod_inverse(e, phi_n)
    
    # Step 6: Return key pairs
    return (e, n), (d, n)


# Example usage
public_key, private_key = generate_rsa_keys(2048)
print(f"Public key (e): {public_key[0]}")
print(f"Modulus (n): {public_key[1]}")
print(f"Private key (d): {private_key[0]}")
```

---

# 4. Practical Example

### Key Generation with Small Primes

Let $p = 61$, $q = 53$:

**Step 1**: $p = 61$, $q = 53$ (both prime ✓)

**Step 2**: $n = 61 \times 53 = 3233$

**Step 3**: $\phi(n) = 60 \times 52 = 3120$

**Step 4**: Choose $e = 17$
- Check: $\gcd(17, 3120) = 1$ ✓

**Step 5**: Compute $d = 17^{-1} \pmod{3120}$
- Using Extended Euclidean Algorithm: $d = 2753$
- Verify: $17 \times 2753 = 46801 = 15 \times 3120 + 1 \equiv 1 \pmod{3120}$ ✓

**Result**:
- Public Key: $(e, n) = (17, 3233)$
- Private Key: $(d, n) = (2753, 3233)$

---

# 5. Key Properties

### Non-Uniqueness
Different values of $e$ and $d$ can work for the same $n$.

### Symmetry
RSA encryption and decryption are symmetric:
- Encrypt with public key, decrypt with private key
- Or vice versa (for digital signatures)

### Key Size Growth
Modern RSA uses 2048-bit or 4096-bit keys for adequate security.

---

# 6. Security Considerations

### Prime Quality
- Primes must be truly random and large
- Should avoid weak primes
- Must pass robust primality tests

### Exponent Selection
- $e = 65537$ is standard (fast and avoids vulnerabilities)
- Must ensure $\gcd(e, \phi(n)) = 1$

### Key Storage
- Private key must be protected
- Public key can be distributed freely
- Use secure key storage mechanisms

---

# 7. Key Takeaways

- **RSA Key Generation** involves six steps: prime selection, modulus computation, totient calculation, exponent selection, private exponent computation, and key formation
- **Security Depends On**: Quality of prime selection and randomness
- **Requirement**: $\gcd(e, \phi(n)) = 1$ must hold
- **Standard Choice**: $e = 65537 = 2^{16} + 1$
- **Modern Key Sizes**: 2048-bit or 4096-bit RSA
- **Private Key**: Must be kept secret; never transmitted

---

# 8. Next Steps

Understanding key generation prepares you for:

- **[RSA Encryption](09_rsa_encryption.md)** - Using the public key
- **[RSA Decryption](10_rsa_decryption.md)** - Using the private key
- **[Prime Generation](12_prime_generation.md)** - Detailed prime selection
- **[RSA Full Algorithm](13_rsa_full_algorithm.md)** - Complete system

---

# 9. References

1. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
3. FIPS 186-4. (2013). "Digital Signature Standard (DSS)." National Institute of Standards and Technology.
