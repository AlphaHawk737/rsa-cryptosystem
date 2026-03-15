# RSA Attacks

## 1. Introduction

Despite RSA's mathematical soundness, various attacks exist that exploit:
- Implementation flaws
- Padding weaknesses
- Side channels
- Algorithm properties
- Weak key generation

Understanding these attacks is essential for secure RSA deployment. This document covers practical attack methods and their countermeasures.

---

# 2. Factorization Attacks

### Pollard's Rho Algorithm

Finds prime factors in expected \(O(n^{1/4})\) time.

**Effectiveness**: Useful when factors are not too large

**Mitigation**: Use large, random primes

### Quadratic Sieve

Better than trial division for moderately large numbers (up to ~100 digits).

**Complexity**: \(O(e^{\sqrt{\log n \log \log n}})\)

**Mitigation**: Use 2048+ bit keys

---

# 3. Bleichenbacher's Padding Attack

### Vulnerability

Exploits PKCS#1 v1.5 padding to decrypt messages without knowing private key.

**Attack Process**:
1. Send variations of ciphertext to oracle
2. Oracle reveals if padding is valid
3. Iteratively narrow down plaintext space
4. Eventually recover plaintext

**Impact**: Can decrypt messages with adaptive chosen-ciphertext attacks

### Mitigation

Use OAEP padding instead of PKCS#1 v1.5:

```python
# Vulnerable: PKCS#1 v1.5
def encrypt_pkcs1_v1_5(message, public_key):
    # Padding: 00 02 [random bytes] 00 [message]
    pass

# Secure: OAEP
def encrypt_oaep(message, public_key):
    # Hash-based randomized padding
    pass
```

---

# 4. Timing Attacks

### Execution Time Variation

Decryption time depends on the value of \(d\).

**Attack**: Monitor decryption time to infer bits of private key.

```python
# Vulnerable: Non-constant time
def rsa_decrypt_slow(ciphertext, d, n):
    result = 1
    for bit in d.bits():
        result = pow(result, 2, n)
        if bit == 1:  # Time varies based on bit
            result = (result * ciphertext) % n
    return result
```

### Mitigation

Use constant-time exponentiation:

```python
# Secure: Constant time
def rsa_decrypt_constant(ciphertext, d, n):
    result = 1
    for bit in d.bits():
        temp = (result * ciphertext) % n
        result = result if not bit else temp
        # Both paths execute regardless of bit value
    return result
```

---

# 5. Power Analysis Attacks

### Differential Power Analysis (DPA)

Analyzes power consumption during cryptographic operations.

**Method**:
1. Collect power traces during decryption
2. Correlate traces with hypothetical key bits
3. Identify correct key values by highest correlation

**Practical Attack**: Successfully recovered private keys from smart cards

### Countermeasures

- **Randomization**: Add random computations
- **Masking**: Use multiplicative/additive blinding
- **Hardware**: Faraday cages, constant power circuits
- **HSM**: Hardware Security Modules

---

# 6. Small Exponent Attacks

### Common Exponent Attack (\(e = 3\))

If multiple parties use same public exponent \(e\) and same modulus size:

```
C₁ = M^3 mod n₁
C₂ = M^3 mod n₂  
C₃ = M^3 mod n₃
```

Using Chinese Remainder Theorem, recover \(M^3\), then compute cube root.

### Mitigation

- Use large exponent (\(e = 65537\))
- Pad messages before encryption
- Use OAEP padding

---

# 7. Low Exponent Decryption Attack

### When \(d\) is Small

If decryption exponent \(d\) is small (bad choice during key generation):

```
If d < n^(1/4), can find d using continuous fractions
```

### Mitigation

- Ensure \(\gcd(e, \phi(n)) = 1\) properly
- Standard: use \(e = 65537\)
- Verify \(d \geq 2^{(n-1)/2}\)

---

# 8. Chosen Ciphertext Attacks

### Adaptive Chosen-Ciphertext Attack

Attacker chooses ciphertexts adaptively and observes decryption results.

**Example**:
- Obtain ciphertext \(C\)
- Compute related ciphertext: \(C' = C \times 2^e \bmod n\)
- Decrypt to get: \(M' = M \times 2 \bmod n\)
- Recover \(M\)

### Mitigation

- Use randomized padding (OAEP)
- Use IND-CCA2 secure schemes
- Never decrypt untrusted ciphertexts without validation

---

# 9. Implementation Attacks

### Common Mistakes

**Mistake 1**: Using default `random` instead of cryptographic RNG
```python
# BAD
p = get_random_prime(random.getrandbits)

# GOOD
import secrets
p = get_random_prime(secrets.randbits)
```

**Mistake 2**: Not using padding
```python
# BAD: Deterministic RSA
ciphertext = pow(message, e, n)

# GOOD: With OAEP padding
ciphertext = rsa_oaep_encrypt(message, public_key)
```

**Mistake 3**: Reusing same message with different keys
```python
# BAD: Homomorphic property exploitable
C = (C1 * C2) mod n  # Decrypts to M1 * M2
```

---

# 10. Key Reuse Attacks

### Multiple Messages, Same Key

**Attack**: Use padding oracle to decrypt messages

**Mitigation**: Use randomized padding (OAEP) - each encryption is unique

---

# 11. Defense Summary

| Attack | Mitigation |
|--------|-----------|
| Factorization | Use 2048+ bit keys |
| Padding oracle | Use OAEP instead of PKCS#1 v1.5 |
| Timing | Constant-time exponentiation |
| Power analysis | Randomization, masking, HSM |
| Small exponent | Use \(e = 65537\), padding |
| Low \(d\) | Proper key generation |
| Chosen ciphertext | Randomized padding, validation |

---

# 12. Key Takeaways

- **RSA Attacks**: Exploit implementation flaws, weak padding, or weak keys
- **Factorization**: Still the primary threat (2048-bit safe for now)
- **Side Channels**: Power, timing, electromagnetic analysis possible
- **Padding Critical**: OAEP required for semantic security
- **Constant Time**: Essential for secure implementation
- **Randomness**: Cryptographically secure RNG required

---

# 13. References

1. Bleichenbacher, D. (1998). "Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1." *CRYPTO '98*.
2. Kocher, P. C., Jaffe, J., & Jun, B. (1999). "Differential Power Analysis." *CRYPTO '99*.
3. Weimer, F., et al. (2020). "Return of Bleichenbacher's Oracle Threat." *USENIX Security Symposium*.
4. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
