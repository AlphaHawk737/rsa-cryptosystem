# Modular Inverse

## 1. Introduction

The **modular multiplicative inverse** is a fundamental concept in number theory and is essential to RSA cryptography. It represents a number that, when multiplied by a given number in modular arithmetic, produces the multiplicative identity.

In RSA key generation, the modular inverse is used to compute the decryption exponent $d$ from the encryption exponent $e$. Without the modular inverse, RSA would not function correctly.

---

# 2. Definition

For a given integer $a$ and modulus $n$, the **modular multiplicative inverse** of $a$ modulo $n$ is an integer $x$ such that:

$$
ax \equiv 1 \pmod{n}
$$

We denote this inverse as $a^{-1} \pmod{n}$.

### Example

Find the modular inverse of 3 modulo 11:

Testing values:
- $3 \times 4 = 12 \equiv 1 \pmod{11}$ ✓

Therefore, $3^{-1} \equiv 4 \pmod{11}$.

---

# 3. Existence Conditions

The modular inverse of $a$ modulo $n$ exists if and only if:

$$
\gcd(a, n) = 1
$$

In other words, $a$ and $n$ must be **coprime** (mutually prime).

---

# 4. Computing Modular Inverse

The **Extended Euclidean Algorithm** is the most efficient method.

```python
def mod_inverse(a, n):
    """
    Compute the modular multiplicative inverse of a modulo n.
    """
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd_val, x, y)
    
    gcd_val, x, _ = extended_gcd(a % n, n)
    
    if gcd_val != 1:
        raise ValueError("Modular inverse does not exist")
    
    return (x % n + n) % n


print(mod_inverse(3, 11))  # Output: 4
print(mod_inverse(7, 26))  # Output: 15
```

---

# 5. Alternative: Fermat's Little Theorem

If $n$ is a prime, then by Fermat's Little Theorem:

$$
a^{-1} \equiv a^{n-2} \pmod{n}
$$

```python
def mod_inverse_fermat(a, n):
    return pow(a, n - 2, n)
```

---

# 6. Properties

### Uniqueness
If the inverse exists, it is unique modulo $n$.

### Inverse of Inverse
$$
(a^{-1})^{-1} \equiv a \pmod{n}
$$

### Multiplicative Property
$$
(ab)^{-1} \equiv a^{-1} \times b^{-1} \pmod{n}
$$

---

# 7. RSA Application

In RSA key generation, we compute the decryption exponent $d$ as:

$$
d \equiv e^{-1} \pmod{\phi(n)}
$$

where $e$ is the encryption exponent and $\phi(n)$ is Euler's totient function.

**Requirement**: $\gcd(e, \phi(n)) = 1$

### Example

Given $\phi(n) = 3120$ and $e = 17$:

$$
d = 17^{-1} \pmod{3120} = 2753
$$

Verification: $17 \times 2753 = 46801 \equiv 1 \pmod{3120}$ ✓

---

# 8. Key Takeaways

- **Modular inverse** of $a$ modulo $n$ is a number $x$ such that $ax \equiv 1 \pmod{n}$
- **Existence condition**: $\gcd(a, n) = 1$
- **Computation**: Extended Euclidean Algorithm is efficient
- **RSA Critical**: Computing the decryption exponent $d$ requires $e^{-1} \pmod{\phi(n)}$
- **Coprimality Requirement**: RSA requires $\gcd(e, \phi(n)) = 1$

---

# 9. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.
3. Burton, D. M. (2010). *Elementary Number Theory* (7th ed.). McGraw-Hill.
