# RSA Security Analysis

## 1. Introduction

**RSA Security Analysis** examines why RSA remains secure despite being publicly known. The security of RSA is founded on well-established mathematical principles and the computational hardness of certain number-theoretic problems.

The security of RSA depends on:
- The difficulty of factoring large integers
- The design of the algorithm itself
- Proper implementation of padding schemes
- Correct key generation practices

---

# 2. Security Foundation: Integer Factorization

### The Factorization Problem

Given a large composite number \(n = p \times q\), finding the prime factors \(p\) and \(q\) is computationally infeasible.

**Theorem**: If an attacker can factor \(n\), they can:
1. Compute \(\phi(n) = (p-1)(q-1)\)
2. Compute \(d = e^{-1} \pmod{\phi(n)}\)
3. Decrypt any message

### Why Factoring is Hard

No polynomial-time algorithm for factoring is known.

**Best Known Algorithms**:

| Algorithm | Time Complexity |
|-----------|-----------------|
| Trial Division | \(O(\sqrt{n})\) |
| Pollard's rho | \(O(n^{1/4})\) |
| Quadratic Sieve | \(O(e^{\sqrt{\log n \log \log n}})\) |
| General Number Field Sieve (GNFS) | \(O(e^{(64/9)^{1/3}(\log n)^{1/3}(\log \log n)^{2/3}})\) |

**Practical Difficulty**:
- 768-bit RSA factored in 2009 (required thousands of CPU-years)
- 1024-bit RSA considered unsafe since ~2013
- 2048-bit RSA expected secure until ~2030
- 4096-bit RSA expected secure for decades

---

# 3. Mathematical Security Properties

### Theorem: RSA Correctness

For any message \(M\) where \(\gcd(M, n) = 1\):

\[
(M^e)^d \equiv M \pmod{n}
\]

**Proof**: By Euler's Theorem, since \(ed \equiv 1 \pmod{\phi(n)}\):

\[
M^{ed} \equiv M^{1 + k\phi(n)} \equiv M \cdot (M^{\phi(n)})^k \equiv M \pmod{n}
\]

This ensures decryption always recovers plaintext.

### One-Way Function

RSA encryption is a **one-way function**:
- Easy to compute: \(C = M^e \bmod n\) (milliseconds)
- Hard to invert: Finding \(M\) from \(C\) without \(d\) requires factoring

---

# 4. Attacks Against RSA

### Factorization Attacks

**General Number Field Sieve (GNFS)**:
- Current best algorithm for factoring
- Subexponential complexity
- Practical limit: ~200-digit (660-bit) numbers

**Mitigation**: Use 2048-bit or larger keys

### Brute Force Attacks

**Dictionary Attack**: Encrypt all possible messages and compare with observed ciphertext.

**Mitigation**: Use padding schemes (OAEP) to randomize encryption

### Homomorphic Property Attack

RSA has multiplicative homomorphism:
\[
E(M_1) \cdot E(M_2) \equiv E(M_1 \cdot M_2) \pmod{n}
\]

**Risk**: Can construct valid ciphertexts from known ones

**Mitigation**: Use deterministic padding (PKCS#1 v1.5) or randomized padding (OAEP)

---

# 5. Implementation Security

### Timing Attacks

Decryption time varies with the value of \(d\).

```python
# Vulnerable to timing attacks
def rsa_decrypt_vulnerable(ciphertext, d, n):
    result = 1
    for bit in d.bits():
        result = (result * result) % n
        if bit == 1:
            result = (result * ciphertext) % n
    return result
```

**Mitigation**: Use constant-time exponentiation

```python
# Constant-time version
def rsa_decrypt_secure(ciphertext, d, n):
    result = 1
    base = ciphertext
    for bit in d.bits():
        if bit:
            result = (result * base) % n
        base = (base * base) % n
    return result
```

### Side-Channel Attacks

- **Power Analysis**: Monitor power consumption during computation
- **Electromagnetic Leakage**: Measure electromagnetic emissions
- **Cache Timing**: Exploit CPU cache behavior

**Mitigation**: Use hardware security modules (HSMs) or constant-time implementations

---

# 6. Key Generation Security

### Weak Prime Selection

If \(p\) or \(q\) are weak primes, RSA becomes vulnerable.

**Weak Primes**:
- \(p - 1\) or \(q - 1\) with all small prime factors
- Primes close to powers of 2
- Primes from non-random generation

**Mitigation**: Generate random primes using Miller-Rabin with sufficient iterations

### Proper Randomness

Private key generation must use cryptographically secure random number generators.

**Bad**: `random.getrandbits()` (pseudorandom)

**Good**: `os.urandom()` or `secrets.randbits()` (cryptographically secure)

---

# 7. Padding Security

### PKCS#1 v1.5 Issues

```
00 02 [random bytes] 00 [data]
```

**Vulnerability**: Bleichenbacher's attack can decrypt without knowing private key

### OAEP (Optimal Asymmetric Encryption Padding)

```
00 [hash] [seed] [random] [data]
```

**Advantages**:
- Provably secure under random oracle model
- Prevents known plaintext attacks
- Randomizes each encryption

**Recommendation**: Always use OAEP for encryption

---

# 8. Parameters and Key Sizes

### Recommended Key Sizes

| Year | Legacy | Recommended | Strong |
|------|--------|------------|---------|
| 2018 | 1024 | 2048 | 4096 |
| 2022 | 1024 | 2048 | 4096 |
| 2030 | 2048 | 3072 | 4096 |
| 2050 | 2048 | 4096 | 8192 |

### Bit Security

- 1024-bit RSA ≈ 80-bit security (breakable)
- 2048-bit RSA ≈ 112-bit security (strong)
- 4096-bit RSA ≈ 128-bit security (very strong)

---

# 9. Proofs of Security

### Semantic Security

RSA with OAEP padding is semantically secure under the **RSA Assumption**:

> Computing \(e\)-th roots modulo \(n\) is computationally infeasible without knowledge of \(\phi(n)\).

### Theorem

Under the RSA Assumption and with OAEP padding, no polynomial-time adversary can win the semantic security game with non-negligible advantage.

---

# 10. Key Takeaways

- **RSA Security**: Based on difficulty of factoring large integers
- **Factorization**: No known polynomial-time algorithm
- **Current Status**: 2048-bit RSA secure; 1024-bit RSA breakable
- **Attacks**: Factorization, side-channels, padding attacks
- **Mitigation**: Proper implementation, OAEP padding, secure key generation
- **Future**: Quantum computers will break RSA (post-quantum alternatives needed)

---

# 11. Post-Quantum Cryptography

### Quantum Threat

Shor's algorithm (1994) can factor large integers in polynomial time on quantum computers.

**Risk Timeline**: Practical quantum computers likely 10-20+ years away

### Post-Quantum Alternatives

- **Lattice-based**: CRYSTALS-Kyber, CRYSTALS-Dilithium
- **Multivariate**: Rainbow, GOST R 34.10-94
- **Hash-based**: XMSS, SPHINCS
- **Code-based**: McEliece, Classic McEliece

---

# 12. References

1. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.
2. Bellare, M., & Rogaway, P. (1994). "Optimal Asymmetric Encryption Padding." *EUROCRYPT '94*.
3. Shor, P. W. (1994). "Algorithms for quantum computation." *FOCS*, ACM.
4. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
