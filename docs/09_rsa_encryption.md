# RSA Encryption

## 1. Introduction

**RSA Encryption** is the process of converting plaintext into ciphertext using the recipient's public key. This is the operational phase of the RSA cryptosystem where secure communication becomes possible.

The RSA encryption operation is elegant in its simplicity:

\[
C = M^e \bmod n
\]

where:
- \(M\) is the plaintext message
- \(e\) is the public exponent
- \(n\) is the modulus
- \(C\) is the ciphertext

Despite its simplicity, the security of this operation relies on the mathematical difficulty of factoring \(n\).

---

# 2. RSA Encryption Process

### Input
- Plaintext message: \(M\) where \(0 \leq M < n\)
- Public key: \((e, n)\)

### Operation

\[
C \equiv M^e \pmod{n}
\]

### Output
- Ciphertext: \(C\)

### Key Properties

1. **Deterministic**: Same plaintext always produces same ciphertext
2. **Efficient**: Fast to compute using modular exponentiation
3. **Public**: Anyone with the public key can encrypt
4. **Secure**: Difficult to reverse without the private key

---

# 3. Encryption Algorithm

```python
def rsa_encrypt(message, e, n):
    """
    Encrypt a message using RSA.
    
    Args:
        message: Integer plaintext (0 <= message < n)
        e: Public exponent
        n: Modulus
    
    Returns:
        Ciphertext (integer)
    """
    ciphertext = pow(message, e, n)
    return ciphertext


# Example usage
e = 17
n = 3233
plaintext = 42

ciphertext = rsa_encrypt(plaintext, e, n)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
```

---

# 4. Practical Example

### Scenario
- Public key: \((e, n) = (17, 3233)\)
- Plaintext: \(M = 65\) (ASCII code for 'A')

### Encryption

\[
C \equiv 65^{17} \pmod{3233}
\]

Using modular exponentiation:

1. Break down 17 in binary: \(17 = 16 + 1 = 2^4 + 2^0\)
2. Compute powers of 65:
   - \(65^1 \equiv 65 \pmod{3233}\)
   - \(65^2 \equiv 4225 \equiv 992 \pmod{3233}\)
   - \(65^4 \equiv 984064 \equiv 939 \pmod{3233}\)
   - \(65^8 \equiv 881721 \equiv 2679 \pmod{3233}\)
   - \(65^{16} \equiv 7177041 \equiv 1570 \pmod{3233}\)

3. Combine:
   \[
   65^{17} = 65^{16} \times 65^1 \equiv 1570 \times 65 \equiv 2790 \pmod{3233}
   \]

**Result**: Ciphertext = 2790

---

# 5. Efficient Modular Exponentiation

For large exponents, direct exponentiation is infeasible. The **square-and-multiply** algorithm reduces complexity from \(O(e)\) to \(O(\log e)\).

```python
def modular_exponentiation(base, exponent, modulus):
    """
    Efficient modular exponentiation using binary method.
    
    Computes: base^exponent mod modulus
    Time: O(log exponent)
    """
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        exponent = exponent >> 1
        base = (base * base) % modulus
    
    return result
```

---

# 6. Message Size Limitations

### Single Block Encryption

In basic RSA, the message must be smaller than the modulus:

\[
0 \leq M < n
\]

For a 2048-bit RSA key, the modulus is approximately \(2^{2048}\), so messages must be less than this.

### Padding Schemes

To support longer messages and improve security:
- **PKCS#1 v1.5**: Adds padding before encryption
- **OAEP**: Optimal Asymmetric Encryption Padding (more secure)

These schemes pad the message to match the modulus size.

---

# 7. Semantic Security

### Deterministic Nature Problem

Basic RSA is **deterministic**: same plaintext → same ciphertext.

**Issue**: Attacker can:
1. Encrypt known plaintexts
2. Compare with observed ciphertext
3. Identify the plaintext

### Solution: Randomized Padding

Padding schemes add randomness, making encryption **probabilistic**.

---

# 8. Key Takeaways

- **RSA Encryption**: \(C = M^e \bmod n\)
- **Efficient**: Uses modular exponentiation (\(O(\log e)\) time)
- **Public Operation**: Anyone with public key can encrypt
- **Deterministic**: Same plaintext produces same ciphertext (in basic RSA)
- **Message Size**: Must be smaller than modulus \(n\)
- **Practical Use**: Requires padding schemes (PKCS#1, OAEP) for security

---

# 9. Next Steps

Understanding RSA encryption prepares you for:

- **[RSA Decryption](10_rsa_decryption.md)** - Reversing the encryption
- **[Modular Exponentiation](11_modular_exponentiation.md)** - Efficient computation
- **[RSA Security Analysis](14_rsa_security_analysis.md)** - Security properties
- **[RSA Full Algorithm](13_rsa_full_algorithm.md)** - Complete system

---

# 10. References

1. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.
2. Bellare, M., & Rogaway, P. (1994). "Optimal Asymmetric Encryption Padding." *EUROCRYPT '94*, Springer-Verlag.
3. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
