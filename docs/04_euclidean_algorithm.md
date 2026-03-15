# Euclidean Algorithm

## 1. Introduction

The Euclidean Algorithm is one of the oldest and most fundamental algorithms in number theory. It provides an efficient method to compute the **greatest common divisor (GCD)** of two integers—a crucial operation in cryptography and mathematics.

The RSA cryptosystem depends critically on the Euclidean Algorithm for:

- Computing the greatest common divisor of two large numbers
- Finding the multiplicative inverse in modular arithmetic
- Verifying the validity of RSA key parameters

The algorithm's elegant design and logarithmic time complexity make it ideal for cryptographic applications involving very large integers.

---

# 2. Greatest Common Divisor (GCD)

The **greatest common divisor** of two integers \(a\) and \(b\) is the largest positive integer that divides both \(a\) and \(b\) without remainder.

We denote this as:

\[
\gcd(a, b)
\]

### Definition

For integers \(a\) and \(b\) (where \(b \neq 0\)), \(\gcd(a, b)\) is the largest integer \(d\) such that:

- \(d \mid a\) (d divides a)
- \(d \mid b\) (d divides b)

### Example

For \(a = 48\) and \(b = 18\):

- Divisors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48
- Divisors of 18: 1, 2, 3, 6, 9, 18
- Common divisors: 1, 2, 3, 6
- Greatest common divisor: 6

Therefore, \(\gcd(48, 18) = 6\).

---

# 3. The Euclidean Algorithm

The Euclidean Algorithm computes the GCD using the following principle:

\[
\gcd(a, b) = \gcd(b, a \bmod b)
\]

The algorithm repeatedly applies this reduction until the remainder becomes zero, at which point the GCD is the last non-zero remainder.

## Algorithm Statement

**Input**: Two non-negative integers \(a\) and \(b\) where \(a \geq b\)

**Output**: \(\gcd(a, b)\)

```
1. While b ≠ 0:
   a ← b
   b ← a mod b
2. Return a
```

This process continues until \(b = 0\), at which point \(a\) contains the GCD.

---

## 4. Example: Computing GCD(48, 18)

Let's trace through the Euclidean Algorithm with \(a = 48\) and \(b = 18\):

| Step | a | b | a mod b | Operation |
|------|---|---|---------|-----------|
| 0 | 48 | 18 | 12 | \(48 = 2 \times 18 + 12\) |
| 1 | 18 | 12 | 6 | \(18 = 1 \times 12 + 6\) |
| 2 | 12 | 6 | 0 | \(12 = 2 \times 6 + 0\) |
| 3 | 6 | 0 | — | Algorithm terminates |

**Result**: \(\gcd(48, 18) = 6\)

---

## 5. Python Implementation

```python
def gcd(a, b):
    """
    Compute the greatest common divisor of a and b using the Euclidean Algorithm.
    
    Args:
        a: First non-negative integer
        b: Second non-negative integer
    
    Returns:
        The greatest common divisor of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a


# Example usage
print(gcd(48, 18))    # Output: 6
print(gcd(100, 35))   # Output: 5
print(gcd(1071, 462)) # Output: 21
```

---

# 6. Time Complexity

The Euclidean Algorithm is remarkably efficient. The number of steps required is bounded by:

\[
O(\log \min(a, b))
\]

This logarithmic complexity makes it suitable for cryptographic operations involving very large integers.

### Why is it Logarithmic?

At each step, at least one of the numbers is reduced by at least half. This is guaranteed by the property that when \(a \geq 2b\), we have \(a \bmod b < a/2\).

Therefore, the algorithm requires at most 5 times the number of digits in the smaller number of steps.

---

# 7. Extended Euclidean Algorithm

The **Extended Euclidean Algorithm** not only computes \(\gcd(a, b)\) but also finds integers \(x\) and \(y\) such that:

\[
ax + by = \gcd(a, b)
\]

This is known as **Bézout's identity**.

## Algorithm

```python
def extended_gcd(a, b):
    """
    Compute gcd(a, b) and find integers x, y such that ax + by = gcd(a, b).
    
    Returns:
        A tuple (gcd, x, y) where ax + by = gcd
    """
    if b == 0:
        return (a, 1, 0)
    
    gcd_value, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return (gcd_value, x, y)


# Example
gcd_val, x, y = extended_gcd(35, 15)
print(f"gcd(35, 15) = {gcd_val}")
print(f"35 × {x} + 15 × {y} = {gcd_val}")
```

### RSA Application

The Extended Euclidean Algorithm is essential for computing the modular inverse in RSA key generation.

---

# 8. Key Takeaways

- **The Euclidean Algorithm** efficiently computes the greatest common divisor in \(O(\log n)\) time
- **GCD Computation** is fundamental to number theory and cryptography
- **Extended Euclidean Algorithm** finds Bézout coefficients, enabling modular inverse computation
- **Coprimality** (when \(\gcd(a, b) = 1\)) is crucial for RSA key generation
- **RSA Dependence**: The algorithm is essential for verifying key validity and computing the decryption exponent

---

# 9. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Burton, D. M. (2010). *Elementary Number Theory* (7th ed.). McGraw-Hill.
3. Hardy, G. H., & Wright, E. M. (2008). *An Introduction to the Theory of Numbers* (6th ed.). Oxford University Press.
