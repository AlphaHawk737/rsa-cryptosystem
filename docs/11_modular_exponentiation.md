# Modular Exponentiation

## 1. Introduction

**Modular Exponentiation** is the computation of $a^b \bmod n$, where $a$, $b$, and $n$ can be extremely large numbers (thousands of bits).

This operation is essential to both RSA encryption and decryption:
- Encryption: $C = M^e \bmod n$
- Decryption: $M = C^d \bmod n$

Without efficient modular exponentiation algorithms, RSA would be computationally infeasible. The naive approach of computing $a^b$ and then reducing modulo $n$ would require intermediate values with billions of bits, impossible to handle.

---

# 2. The Challenge

### Naive Approach Problem

Computing $a^b$ directly and then taking modulo $n$ fails because:

- $a^b$ becomes astronomically large
- For $a = 2^{2048}$ and $b = 2^{2048}$, the result would have $2^{2048} \times 2048$ bits
- This is completely impractical to compute

### Solution: Reduce at Each Step

Instead of computing the full exponent, reduce modulo $n$ at each step:

$$
(a \times b) \bmod n = ((a \bmod n) \times (b \bmod n)) \bmod n
$$

This keeps intermediate values bounded by $n$.

---

# 3. Square-and-Multiply Algorithm

The **square-and-multiply** algorithm (also called binary exponentiation) reduces time complexity from $O(b)$ to $O(\log b)$.

### Algorithm Principle

Express the exponent in binary and process each bit:

$$
b = \sum_{i=0}^{k} b_i \times 2^i
$$

where each $b_i$ is 0 or 1.

Then:

$$
a^b = a^{\sum b_i \times 2^i} = \prod_{i: b_i=1} a^{2^i}
$$

### Algorithm Steps

```
1. result ← 1
2. base ← a
3. exponent ← b
4. While exponent > 0:
     If exponent is odd:
       result ← (result × base) mod n
     base ← (base × base) mod n
     exponent ← exponent >> 1
5. Return result
```

---

# 4. Python Implementation

```python
def modular_exponentiation(base, exponent, modulus):
    """
    Compute (base^exponent) mod modulus efficiently.
    
    Uses square-and-multiply algorithm.
    Time complexity: O(log exponent)
    
    Args:
        base: Base value
        exponent: Exponent value
        modulus: Modulus for reduction
    
    Returns:
        (base^exponent) mod modulus
    """
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply result by base
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # Square the base and halve the exponent
        exponent = exponent >> 1
        base = (base * base) % modulus
    
    return result


# Example usage
print(modular_exponentiation(2, 10, 1000))     # 2^10 mod 1000 = 24
print(modular_exponentiation(3, 13, 1000))     # 3^13 mod 1000 = 327
print(pow(2, 1000000, 1000000007))  # Using Python's built-in
```

---

# 5. Step-by-Step Example

### Compute $3^{13} \bmod 17$

**Binary representation**: $13 = 1101_2 = 8 + 4 + 1$

| Step | Exponent | Exponent (binary) | Base | Result | Operation |
|------|----------|-------------------|------|--------|-----------|
| 0 | 13 | 1101 | 3 | 1 | exponent odd: result = 1×3 mod 17 = 3 |
| 1 | 6 | 110 | 3²=9 | 3 | square: 9, exponent even |
| 2 | 3 | 11 | 9²=81≡13 | 3×13≡39≡5 | square: 13, exponent odd: 3×13 mod 17 = 5 |
| 3 | 1 | 1 | 13²≡16 | 5×16≡80≡12 | square: 16, exponent odd: 5×16 mod 17 = 12 |
| 4 | 0 | — | — | 12 | exponent = 0, done |

**Result**: $3^{13} \bmod 17 = 12$

---

# 6. Time Complexity Analysis

### Comparison

| Method | Time Complexity | Practical |
|--------|-----------------|-----------|
| Naive (repeated multiplication) | $O(b)$ | Infeasible for large $b$ |
| Square-and-Multiply | $O(\log b)$ | Practical for 2048-bit exponents |

### Example: 2048-bit Exponentiation

- **Naive approach**: 2^2048 ≈ 10^616 multiplications (impossible)
- **Square-and-Multiply**: log₂(2^2048) = 2048 ≈ 2000 multiplications (feasible in milliseconds)

---

# 7. Hardware Acceleration

### RSA Hardware Support

Modern CPUs include instructions for efficient modular multiplication:
- Intel: MULX, ADCX, ADOX
- AMD: Similar support

### Performance

- Software: ~1-10 milliseconds per encryption/decryption
- Hardware-accelerated: ~0.1-1 millisecond

---

# 8. Variations

### Right-to-Left Binary Method

Process binary digits from least significant to most significant:

```python
def modular_exponentiation_rtl(base, exponent, modulus):
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    
    return result
```

### Windowed Exponentiation

For very large exponents, process multiple bits at once (faster but more memory).

---

# 9. Key Takeaways

- **Modular Exponentiation**: Computing $a^b \bmod n$ efficiently
- **Square-and-Multiply**: Reduces complexity from $O(b)$ to $O(\log b)$
- **Essential to RSA**: Makes encryption and decryption computationally feasible
- **Binary Method**: Process exponent bit by bit
- **Practical**: 2048-bit exponentiation in milliseconds
- **Hardware Support**: Modern CPUs have optimized instructions

---

# 10. Next Steps

Understanding modular exponentiation prepares you for:

- **[RSA Full Algorithm](13_rsa_full_algorithm.md)** - Complete RSA system
- **[RSA Security Analysis](14_rsa_security_analysis.md)** - Security properties
- **[Prime Generation](12_prime_generation.md)** - Other computational algorithms

---

# 11. References

1. Knuth, D. E. (1998). *The Art of Computer Programming, Vol. 2: Seminumerical Algorithms* (3rd ed.). Addison-Wesley.
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
3. Hankerson, D., Menezes, A. J., & Vanstone, S. A. (2004). *Guide to Elliptic Curve Cryptography*. Springer-Verlag.
