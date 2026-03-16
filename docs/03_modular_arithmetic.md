# Modular Arithmetic

## 1. Introduction

Modular arithmetic is a fundamental concept in number theory and forms the mathematical foundation of many cryptographic systems. In particular, the RSA cryptosystem relies heavily on modular arithmetic for performing secure encryption and decryption operations.

In conventional arithmetic, numbers can grow arbitrarily large as operations are performed. In contrast, modular arithmetic restricts results to a fixed range by introducing a modulus. All calculations are performed relative to this modulus.

This property makes modular arithmetic especially suitable for computer-based cryptographic algorithms, where extremely large numbers must be manipulated efficiently while remaining bounded within a predictable range.

---

# 2. Concept of Modulus

A **modulus** is a positive integer that defines the range within which arithmetic operations are performed.

If an integer $a$ is divided by a positive integer $n$, the result can be written as:

$$
a = nq + r
$$

where:

| Symbol | Meaning |
|------|------|
| $a$ | integer being divided |
| $n$ | modulus |
| $q$ | quotient |
| $r$ | remainder |

The remainder satisfies the constraint:

$$
0 \le r < n
$$

The remainder $r$ represents the value of $a$ **modulo $n$**.

---

# 3. Modular Congruence

Two integers are said to be **congruent modulo $n$** if they leave the same remainder when divided by $n$.

This relationship is written as:

$$
a \equiv b \pmod{n}
$$

This statement means:

$$
n \mid (a-b)
$$

which indicates that the difference between $a$ and $b$ is divisible by $n$.

### Interpretation

The congruence relation partitions integers into equivalence classes where all numbers in the same class share the same remainder when divided by $n$.

For a modulus $n$, there exist exactly $n$ distinct equivalence classes:

$$
0, 1, 2, \dots, n-1
$$

Every integer belongs to one of these classes.

---

# 4. Modular Arithmetic Operations

Modular arithmetic supports operations analogous to standard arithmetic. These operations preserve congruence relationships.

## 4.1 Modular Addition

If

$$
a \equiv b \pmod{n}
$$

and

$$
c \equiv d \pmod{n}
$$

then

$$
a + c \equiv b + d \pmod{n}
$$

In practice, addition is performed normally and the result is reduced modulo $n$.

---

## 4.2 Modular Subtraction

Subtraction also preserves congruence:

$$
a - c \equiv b - d \pmod{n}
$$

After performing subtraction, the result is again reduced modulo $n$.

---

## 4.3 Modular Multiplication

Multiplication follows the same principle:

$$
ac \equiv bd \pmod{n}
$$

Multiplication is followed by modular reduction to keep results within the modular range.

---

## 4.4 Modular Exponentiation

Exponentiation is particularly important in cryptographic algorithms.

$$
a^k \pmod{n}
$$

This operation raises a number to a power and then reduces the result modulo $n$.

Directly computing large exponents is inefficient. Therefore, cryptographic implementations use optimized algorithms such as **square-and-multiply modular exponentiation**.

---

# 5. Properties of Modular Arithmetic

Modular arithmetic exhibits several important algebraic properties.

## Closure

Operations within modular arithmetic remain within the modular set:

$$
\{0,1,2,\dots,n-1\}
$$

---

## Associativity

Addition and multiplication are associative:

$$
(a+b)+c = a+(b+c)
$$

$$
(ab)c = a(bc)
$$

---

## Commutativity

Both addition and multiplication are commutative:

$$
a+b = b+a
$$

$$
ab = ba
$$

---

## Distributive Property

Multiplication distributes over addition:

$$
a(b+c) = ab + ac
$$

This property holds under modular arithmetic as well.

---

# 6. Modular Reduction

A key feature of modular arithmetic is **modular reduction**, which keeps numbers within the modular range.

For any integer $a$:

$$
a \bmod n
$$

represents the remainder when $a$ is divided by $n$.

Large intermediate values in calculations can be reduced at each step without affecting the final result.

For example:

$$
(a \cdot b) \bmod n
$$

can be computed as

$$
((a \bmod n) \cdot (b \bmod n)) \bmod n
$$

This property significantly reduces computational complexity in cryptographic systems.

---

# 7. Importance in Cryptography

Modular arithmetic is essential in public-key cryptography because it enables operations on extremely large integers while keeping values computationally manageable.

The RSA cryptosystem uses modular arithmetic in the following ways:

| RSA Component | Role of Modular Arithmetic |
|------|------|
| Key generation | Computation of modular inverses |
| Encryption | Modular exponentiation |
| Decryption | Modular exponentiation |
| Security | Mathematical properties of modular congruence |

Encryption in RSA is defined as:

$$
C = M^e \bmod n
$$

Decryption is defined as:

$$
M = C^d \bmod n
$$

Both operations rely entirely on modular arithmetic.

---

# 8. Efficient Modular Exponentiation

In cryptographic applications, exponents can be extremely large. Direct exponentiation would be computationally infeasible.

To address this problem, algorithms such as **square-and-multiply** are used.

This algorithm repeatedly performs two operations:

1. squaring the current value
2. multiplying when required by the exponent's binary representation

An example implementation from the project source code is shown below.

```python
def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus

        exponent = exponent >> 1
        base = (base * base) % modulus

    return result
```

This algorithm reduces computational complexity from $O(e)$ to $O(\log e)$, which makes modern cryptographic systems practical.

---

# 9. Practical Examples

## Example 1: Simple Modular Addition

Let's compute $17 + 28 \pmod{13}$:

1. Perform addition: $17 + 28 = 45$
2. Reduce modulo 13: $45 \div 13 = 3$ remainder $6$
3. Result: $17 + 28 \equiv 6 \pmod{13}$

Alternatively, reduce each operand first:
- $17 \equiv 4 \pmod{13}$
- $28 \equiv 2 \pmod{13}$
- $(4 + 2) \bmod 13 = 6 \pmod{13}$

---

## Example 2: Modular Multiplication

Let's compute $7 \times 11 \pmod{15}$:

1. Perform multiplication: $7 \times 11 = 77$
2. Reduce modulo 15: $77 \div 15 = 5$ remainder $2$
3. Result: $7 \times 11 \equiv 2 \pmod{15}$

---

## Example 3: Modular Exponentiation

Let's compute $3^{10} \pmod{7}$ using the square-and-multiply algorithm:

| Step | Exponent (binary) | Operation | Result |
|------|------|------|------|
| 0 | 1010 | Initialize | base=3, result=1 |
| 1 | 1010 | Exponent is even, square | base=9≡2, result=1 |
| 2 | 0101 | Exponent is odd, multiply | base=4, result=2 |
| 3 | 0010 | Exponent is even, square | base=16≡2, result=2 |
| 4 | 0001 | Exponent is odd, multiply | base=4, result=4 |
| 5 | 0000 | Done | Final: 4 |

Therefore, $3^{10} \equiv 4 \pmod{7}$.

---

# 10. Key Takeaways

- **Modular arithmetic** restricts operations to a fixed range $\{0, 1, 2, \ldots, n-1\}$
- **Congruence** defines equivalence classes of integers that leave the same remainder modulo $n$
- **Operations** (addition, subtraction, multiplication, exponentiation) preserve congruence relationships
- **Modular reduction** keeps intermediate values bounded, enabling efficient computation on large numbers
- **RSA encryption and decryption** rely entirely on modular exponentiation: $C = M^e \bmod n$ and $M = C^d \bmod n$
- **Efficient algorithms** like square-and-multiply reduce exponentiation from exponential to logarithmic time complexity

---

# 11. Next Steps

This foundational knowledge of modular arithmetic prepares you for understanding:

- **[Euclidean Algorithm](04_euclidean_algorithm.md)** - Finding the greatest common divisor
- **[Modular Inverse](05_modular_inverse.md)** - Computing multiplicative inverses in modular arithmetic
- **[Euler's Totient Function](06_euler_totient_function.md)** - Computing $\phi(n)$ for RSA key generation
- **[Euler's Theorem](07_euler_theorem.md)** - The mathematical foundation of RSA

---

# References

1. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A method for obtaining digital signatures and public-key cryptosystems." *Communications of the ACM*, 21(2), 120-126.
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
3. Stallings, W. (2017). *Cryptography and Network Security* (6th ed.). Pearson.
4. Burton, D. M. (2010). *Elementary Number Theory* (7th ed.). McGraw-Hill.
