# RSA Decryption

## 1. Introduction

**RSA Decryption** is the process of converting ciphertext back into plaintext using the recipient's private key. This is how the recipient recovers the original message sent by the sender.

The RSA decryption operation mirrors encryption:

$$
M = C^d \bmod n
$$

where:
- $C$ is the ciphertext
- $d$ is the private exponent
- $n$ is the modulus
- $M$ is the recovered plaintext

The mathematical correctness of decryption is guaranteed by Euler's Theorem, which ensures that $M^{ed} \equiv M \pmod{n}$.

---

# 2. RSA Decryption Process

### Input
- Ciphertext: $C$
- Private key: $(d, n)$

### Operation

$$
M \equiv C^d \pmod{n}
$$

### Output
- Plaintext: $M$

### Security Requirement

Only the holder of the private key can decrypt, since knowledge of $d$ is required.

---

# 3. Mathematical Foundation

The correctness of RSA decryption is proven using Euler's Theorem:

**Theorem**: For any message $M$ where $\gcd(M, n) = 1$:

$$
M^{ed} \equiv M \pmod{n}
$$

**Proof**:

Since $ed \equiv 1 \pmod{\phi(n)}$:

$$
ed = k \cdot \phi(n) + 1
$$

for some integer $k$.

Therefore:

$$
C^d \equiv (M^e)^d \equiv M^{ed} \equiv M^{k \cdot \phi(n) + 1} \pmod{n}
$$

$$
\equiv M \cdot (M^{\phi(n)})^k \pmod{n}
$$

By Euler's Theorem:

$$
M^{\phi(n)} \equiv 1 \pmod{n}
$$

Thus:

$$
M \cdot 1^k \equiv M \pmod{n}
$$

This proves that decryption correctly recovers the plaintext.

---

# 4. Decryption Algorithm

```python
def rsa_decrypt(ciphertext, d, n):
    """
    Decrypt a ciphertext using RSA.
    
    Args:
        ciphertext: Encrypted message (integer)
        d: Private exponent
        n: Modulus
    
    Returns:
        Plaintext (integer)
    """
    plaintext = pow(ciphertext, d, n)
    return plaintext


# Example usage
d = 2753
n = 3233
ciphertext = 2790

plaintext = rsa_decrypt(ciphertext, d, n)
print(f"Ciphertext: {ciphertext}")
print(f"Plaintext: {plaintext}")
```

---

# 5. Practical Example

### Scenario
- Private key: $(d, n) = (2753, 3233)$
- Ciphertext: $C = 2790$

### Decryption

$$
M \equiv 2790^{2753} \pmod{3233}
$$

Using modular exponentiation with binary representation of 2753:

1. $2753 = 101010111001_2$ in binary

2. Compute required powers of 2790 modulo 3233

3. Combine using square-and-multiply algorithm

**Result**: $M = 65$ (ASCII code for 'A')

---

# 6. Verification of Encryption-Decryption

### Complete Example

Given the key pair $(e=17, d=2753, n=3233)$:

**Original plaintext**: $M = 65$

**Encryption**:
$$
C = 65^{17} \bmod 3233 = 2790
$$

**Decryption**:
$$
M' = 2790^{2753} \bmod 3233 = 65
$$

**Verification**: $M = M' = 65$ ✓

---

# 7. Multi-Block Decryption

For messages larger than the modulus, the plaintext is divided into blocks, each encrypted separately.

```python
def rsa_decrypt_blocks(ciphertext_blocks, d, n):
    """Decrypt multiple blocks."""
    plaintext_blocks = [
        rsa_decrypt(block, d, n) 
        for block in ciphertext_blocks
    ]
    return plaintext_blocks
```

The blocks must be reconstructed to form the original message.

---

# 8. Computational Efficiency

### Time Complexity

Decryption requires:
- Modular exponentiation: $O(\log d)$ multiplications
- Each multiplication: $O(\log n)^2$ bit operations
- Total: $O(\log d \cdot \log n)^2$

For 2048-bit RSA:
- $\log n \approx 2048$ bits
- $\log d \approx 2048$ bits
- Approximately $2048^2 \approx 4 \times 10^6$ bit operations

Modern computers can decrypt in milliseconds.

---

# 9. Key Takeaways

- **RSA Decryption**: $M = C^d \bmod n$
- **Mathematical Basis**: Euler's Theorem guarantees $M^{ed} \equiv M \pmod{n}$
- **Private Key**: Only holder of $d$ can decrypt
- **Efficiency**: $O(\log d \cdot \log n)^2$ bit operations
- **Correctness**: Always recovers original plaintext (except rare edge cases)
- **Security**: Cannot decrypt without knowing $d$ or factoring $n$

---

# 10. Next Steps

Understanding decryption prepares you for:

- **[Modular Exponentiation](11_modular_exponentiation.md)** - Efficient computation
- **[RSA Full Algorithm](13_rsa_full_algorithm.md)** - Complete encryption-decryption flow
- **[RSA Security Analysis](14_rsa_security_analysis.md)** - Why it's secure
- **[Real-World RSA](16_real_world_rsa_usage.md)** - Practical implementations

---

# 11. References

1. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
3. Stallings, W. (2017). *Cryptography and Network Security* (6th ed.). Pearson.
