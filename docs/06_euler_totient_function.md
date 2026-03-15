# Euler's Totient Function

## 1. Introduction

**Euler's totient function**, denoted \(\phi(n)\), counts the number of integers from 1 to \(n\) that are coprime to \(n\).

The totient function is essential to RSA for:

- Computing the range of valid encryption and decryption exponents
- Establishing the mathematical relationship between public and private keys
- Proving the correctness of RSA encryption and decryption

Understanding \(\phi(n)\) is critical to understanding how RSA works.

---

# 2. Definition

For a positive integer \(n\), **Euler's totient function** \(\phi(n)\) is the count of positive integers up to \(n\) that are relatively prime to \(n\):

\[
\phi(n) = \#\{1 \leq k \leq n : \gcd(k, n) = 1\}
\]

### Example: Computing \(\phi(12)\)

For \(n = 12\), the integers coprime to 12 are: {1, 5, 7, 11}

Therefore, \(\phi(12) = 4\).

---

# 3. Computing Euler's Totient Function

### For Prime Numbers
\[
\phi(p) = p - 1
\]

### For Prime Powers
\[
\phi(p^k) = p^{k-1}(p - 1)
\]

### For Coprime Numbers
If \(\gcd(m, n) = 1\), then:

\[
\phi(mn) = \phi(m) \times \phi(n)
\]

### General Formula
\[
\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)
\]

---

# 4. Computing \(\phi(n)\) for RSA

In RSA, we use \(n = p \times q\) where \(p\) and \(q\) are distinct primes:

\[
\phi(n) = (p-1) \times (q-1)
\]

### Example

Given \(p = 61\) and \(q = 53\):

\[
\phi(3233) = 60 \times 52 = 3120
\]

---

# 5. Python Implementation

```python
def euler_totient(n):
    """Compute Euler's totient function φ(n)."""
    result = n
    p = 2
    
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    
    if n > 1:
        result -= result // n
    
    return result


def euler_totient_rsa(p, q):
    """Compute φ(pq) for RSA."""
    return (p - 1) * (q - 1)


print(euler_totient(12))        # Output: 4
print(euler_totient_rsa(61, 53)) # Output: 3120
```

---

# 6. Properties

### Multiplicativity
If \(\gcd(m, n) = 1\), then \(\phi(mn) = \phi(m) \times \phi(n)\)

### Gauss's Theorem
\[
\sum_{d \mid n} \phi(d) = n
\]

### For Prime Powers
\[
\phi(p^k) = p^{k-1}(p-1)
\]

---

# 7. Relationship to RSA Security

Euler's totient function is central to RSA:

1. **Key Generation**: Determines valid encryption exponents
2. **Decryption Exponent**: Found by computing \(e^{-1} \pmod{\phi(n)}\)
3. **Security**: Computing \(\phi(n)\) from \(n\) is as hard as factoring \(n\)

---

# 8. Key Takeaways

- **Euler's totient** \(\phi(n)\) counts integers from 1 to \(n\) that are coprime to \(n\)
- **For primes**: \(\phi(p) = p - 1\)
- **For RSA**: \(\phi(n) = (p-1)(q-1)\) where \(n = pq\)
- **Multiplicativity**: \(\phi(mn) = \phi(m)\phi(n)\) when \(\gcd(m,n) = 1\)
- **RSA Critical**: Decryption exponent is \(d \equiv e^{-1} \pmod{\phi(n)}\)

---

# 9. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Burton, D. M. (2010). *Elementary Number Theory* (7th ed.). McGraw-Hill.
3. Hardy, G. H., & Wright, E. M. (2008). *An Introduction to the Theory of Numbers* (6th ed.). Oxford University Press.
