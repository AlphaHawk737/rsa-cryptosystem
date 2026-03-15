# Prime Generation

## 1. Introduction

**Prime Generation** is the process of finding large random prime numbers suitable for RSA key generation. The quality and randomness of the primes directly impact the security of the entire RSA system.

RSA requires two distinct prime numbers \(p\) and \(q\), each typically 1024-2048 bits long. Finding such large primes requires:

- Efficient primality testing
- Random number generation
- Computational efficiency

This document covers the mathematical concepts and practical implementation of prime generation for cryptography.

---

# 2. Prime Number Properties

### Definition

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

### Density of Primes

The **Prime Number Theorem** estimates the number of primes less than \(n\):

\[
\pi(n) \approx \frac{n}{\ln n}
\]

For cryptographic purposes:
- Among random 2048-bit numbers, approximately 1 in 1400 is prime
- This means finding a prime requires testing \(\approx 700\) candidates on average

---

# 3. Primality Testing

### Trial Division

The simplest method but impractical for large numbers:

```python
def is_prime_trial(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

**Time Complexity**: \(O(\sqrt{n})\) - infeasible for 2048-bit numbers

### Miller-Rabin Primality Test

A probabilistic algorithm that is efficient and suitable for cryptography.

**Algorithm**:

For odd number \(n\), write \(n - 1 = 2^r \cdot d\) where \(d\) is odd.

For a witness \(a\):
1. Compute \(x = a^d \bmod n\)
2. If \(x = 1\) or \(x = n-1\), return "probably prime"
3. For \(i\) from 0 to \(r-2\):
   - \(x = x^2 \bmod n\)
   - If \(x = n-1\), return "probably prime"
4. Return "composite"

Repeat with multiple random witnesses for high confidence.

```python
def is_prime_miller_rabin(n, k=40):
    """
    Miller-Rabin primality test.
    
    Args:
        n: Number to test
        k: Number of iterations (higher = more confident)
    
    Returns:
        True if probably prime, False if composite
    """
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
```

**Time Complexity**: \(O(k \log^3 n)\) - suitable for cryptography

**Error Probability**: After \(k\) iterations, probability of false prime is at most \(4^{-k}\)

---

# 4. Prime Generation for RSA

### Algorithm

```python
import random

def generate_prime(bit_length, certainty=40):
    """
    Generate a random prime of specified bit length.
    
    Args:
        bit_length: Desired number of bits
        certainty: Number of Miller-Rabin iterations
    
    Returns:
        A random prime number
    """
    while True:
        # Generate random odd number with desired bit length
        candidate = random.getrandbits(bit_length)
        candidate |= (1 << (bit_length - 1))  # Ensure top bit is 1
        candidate |= 1  # Make it odd
        
        # Test for primality
        if is_prime_miller_rabin(candidate, certainty):
            return candidate
```

---

# 5. Practical Example

### Generate 512-bit Prime

```python
import random

def generate_prime_512():
    while True:
        # Random 512-bit number
        n = random.getrandbits(512)
        n |= (1 << 511)  # Set most significant bit
        n |= 1  # Make it odd
        
        if is_prime_miller_rabin(n, 40):
            return n

p = generate_prime_512()
print(f"Prime p: {p}")
print(f"Bit length: {p.bit_length()}")
```

---

# 6. Weak Primes to Avoid

### Strong Primes

For RSA, **strong primes** are preferred:
- \(p\) is prime
- \(p-1\) has a large prime factor
- \(p+1\) has a large prime factor

These provide additional security against some factorization attacks.

### Carmichael Numbers

**Carmichael numbers** pass Fermat's test but are composite. Use Miller-Rabin instead of Fermat's test.

---

# 7. Key Generation Process

### Complete RSA Prime Generation

```python
def generate_rsa_primes(bit_length=1024):
    """
    Generate two distinct primes for RSA.
    """
    p = generate_prime(bit_length)
    
    # Ensure q is different from p
    q = generate_prime(bit_length)
    while q == p:
        q = generate_prime(bit_length)
    
    # Optionally, ensure p and q are properly ordered
    if p > q:
        p, q = q, p
    
    return p, q
```

---

# 8. Performance Analysis

### Statistics

| Prime Size | Expected Candidates | Expected Iterations |
|------------|-------------------|-------------------|
| 512-bit | ~355 | ~708 |
| 1024-bit | ~710 | ~1420 |
| 2048-bit | ~1420 | ~2840 |

Using Miller-Rabin with 40 iterations:
- 512-bit prime: ~1-2 seconds
- 1024-bit prime: ~5-10 seconds
- 2048-bit prime: ~30-60 seconds

---

# 9. Key Takeaways

- **Prime Generation**: Finding large random primes for RSA
- **Miller-Rabin Test**: Efficient probabilistic primality test
- **Prime Density**: \(\approx n/\ln n\) primes less than \(n\)
- **Algorithm**: Generate random candidates and test until prime found
- **Security**: Use cryptographically secure random number generators
- **Strong Primes**: Preferred for additional security properties

---

# 10. Next Steps

Understanding prime generation prepares you for:

- **[RSA Key Generation](08_rsa_key_generation.md)** - Complete key generation
- **[RSA Full Algorithm](13_rsa_full_algorithm.md)** - Complete RSA system
- **[Real-World RSA](16_real_world_rsa_usage.md)** - Practical implementations

---

# 11. References

1. Miller, G. L. (1976). "Riemann's Hypothesis and Tests for Primality." *Journal of Computer and System Sciences*, 13(3), 300-317.
2. Rabin, M. O. (1980). "Probabilistic algorithm for testing primality." *Journal of Number Theory*, 12(1), 128-138.
3. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
