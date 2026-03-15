# RSA Full Algorithm

## 1. Introduction

The **RSA Full Algorithm** is the complete cryptosystem combining all previously discussed concepts:

- Prime generation
- Key generation
- Encryption
- Decryption
- Signing and verification (digital signatures)

This document provides a comprehensive overview of the entire RSA system with complete working examples and code implementations.

---

# 2. RSA Algorithm Overview

### Three Main Phases

1. **Key Generation**: Create public and private keys
2. **Encryption/Decryption**: Secure message transmission
3. **Digital Signatures**: Authentication and non-repudiation

---

# 3. Complete Key Generation

### Step-by-Step Process

```python
import random

def generate_rsa_keypair(key_size=2048):
    """
    Generate complete RSA key pair.
    
    Args:
        key_size: Size of RSA modulus in bits
    
    Returns:
        ((e, n), (d, n)): Public key, Private key
    """
    
    # Step 1: Generate two large random primes
    p = generate_prime(key_size // 2)
    q = generate_prime(key_size // 2)
    
    # Ensure they are distinct
    while p == q:
        q = generate_prime(key_size // 2)
    
    # Step 2: Compute modulus
    n = p * q
    
    # Step 3: Compute Euler's totient
    phi_n = (p - 1) * (q - 1)
    
    # Step 4: Choose public exponent
    e = 65537
    while gcd(e, phi_n) != 1:
        e += 2
    
    # Step 5: Compute private exponent
    d = mod_inverse(e, phi_n)
    
    # Step 6: Return key pair
    return (e, n), (d, n)
```

---

# 4. Complete Encryption and Decryption

### Combined Process

```python
def rsa_encrypt(plaintext, public_key):
    """Encrypt using public key."""
    e, n = public_key
    return pow(plaintext, e, n)


def rsa_decrypt(ciphertext, private_key):
    """Decrypt using private key."""
    d, n = private_key
    return pow(ciphertext, d, n)


# Demonstration
public_key, private_key = generate_rsa_keypair(2048)

message = 12345
ciphertext = rsa_encrypt(message, public_key)
recovered = rsa_decrypt(ciphertext, private_key)

assert message == recovered, "Decryption failed!"
print(f"Original:  {message}")
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {recovered}")
```

---

# 5. Message Padding (PKCS#1 v1.5)

Real-world RSA requires padding to:
1. Handle messages larger than modulus
2. Provide semantic security (randomization)
3. Prevent certain attacks

```python
def rsa_encrypt_padded(message_bytes, public_key):
    """RSA encryption with PKCS#1 v1.5 padding."""
    e, n = public_key
    
    # Add padding
    padded = pkcs1_v1_5_pad(message_bytes, n.bit_length() // 8)
    
    # Convert bytes to integer
    message_int = int.from_bytes(padded, 'big')
    
    # Encrypt
    ciphertext = pow(message_int, e, n)
    
    return ciphertext


def rsa_decrypt_padded(ciphertext, private_key):
    """RSA decryption with PKCS#1 v1.5 unpadding."""
    d, n = private_key
    
    # Decrypt
    message_int = pow(ciphertext, d, n)
    
    # Convert integer to bytes
    padded = message_int.to_bytes(n.bit_length() // 8, 'big')
    
    # Remove padding
    message_bytes = pkcs1_v1_5_unpad(padded)
    
    return message_bytes
```

---

# 6. Digital Signatures

### Signing

```python
def rsa_sign(message_hash, private_key):
    """
    Sign a message hash using private key.
    
    This is essentially decryption with the private key.
    """
    d, n = private_key
    signature = pow(message_hash, d, n)
    return signature
```

### Verification

```python
def rsa_verify(signature, public_key, original_hash):
    """
    Verify a signature using public key.
    
    This is essentially encryption with the public key.
    """
    e, n = public_key
    recovered_hash = pow(signature, e, n)
    return recovered_hash == original_hash
```

### Complete Example

```python
import hashlib

# Message to sign
message = b"I agree to this contract"

# Compute hash
message_hash = int.from_bytes(
    hashlib.sha256(message).digest(), 'big'
)

# Sign with private key
signature = rsa_sign(message_hash, private_key)

# Verify with public key
valid = rsa_verify(signature, public_key, message_hash)
print(f"Signature valid: {valid}")
```

---

# 7. Complete RSA Class Implementation

```python
class RSA:
    """Complete RSA cryptosystem implementation."""
    
    def __init__(self, key_size=2048):
        self.public_key, self.private_key = generate_rsa_keypair(key_size)
        self.n = self.public_key[1]
    
    def encrypt(self, plaintext):
        """Encrypt plaintext."""
        return rsa_encrypt(plaintext, self.public_key)
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext."""
        return rsa_decrypt(ciphertext, self.private_key)
    
    def sign(self, message_hash):
        """Sign a message hash."""
        return rsa_sign(message_hash, self.private_key)
    
    def verify(self, signature, message_hash):
        """Verify a signature."""
        return rsa_verify(signature, self.public_key, message_hash)
    
    def get_public_key(self):
        """Return public key for distribution."""
        return self.public_key
    
    def export_private_key(self):
        """Export private key (for storage)."""
        return self.private_key


# Usage
rsa = RSA(2048)
plaintext = 42
ciphertext = rsa.encrypt(plaintext)
recovered = rsa.decrypt(ciphertext)
assert plaintext == recovered
```

---

# 8. Practical Example: Secure Communication

### Alice and Bob Scenario

```python
# Key generation phase (done once)
alice_rsa = RSA(2048)
bob_rsa = RSA(2048)

# Exchange public keys
alice_public = alice_rsa.get_public_key()
bob_public = bob_rsa.get_public_key()

# Message from Bob to Alice
message = 12345

# Bob encrypts with Alice's public key
ciphertext = rsa_encrypt(message, alice_public)

# Alice decrypts with her private key
recovered = alice_rsa.decrypt(ciphertext)

assert message == recovered
print(f"Secure communication successful: {recovered}")
```

---

# 9. Security Properties

### Confidentiality
- Only private key holder can decrypt
- Computational infeasibility of factoring \(n\)

### Authenticity
- Sender can prove they sent a message (digital signature)
- Receiver can verify sender's identity

### Non-Repudiation
- Sender cannot deny sending a message
- Signature is tied to sender's private key

---

# 10. Computational Complexity Summary

| Operation | Complexity | Time (2048-bit) |
|-----------|-----------|-----------------|
| Key Generation | \(O(\log^2 n)\) for primality test | ~1 minute |
| Encryption | \(O(\log e \cdot \log n)^2\) | ~1 ms |
| Decryption | \(O(\log d \cdot \log n)^2\) | ~1 ms |
| Signing | \(O(\log d \cdot \log n)^2\) | ~1 ms |
| Verification | \(O(\log e \cdot \log n)^2\) | ~1 ms |

---

# 11. Key Takeaways

- **RSA Full Algorithm**: Combines key generation, encryption, decryption, and signing
- **Security**: Based on difficulty of factoring large integers
- **Asymmetric**: Public key for encryption, private key for decryption
- **Versatility**: Supports both confidentiality and authentication
- **Efficiency**: Practical performance with 2048-bit keys
- **Padding**: Essential for real-world implementation (PKCS#1, OAEP)

---

# 12. Next Steps

Understanding the complete RSA algorithm prepares you for:

- **[RSA Security Analysis](14_rsa_security_analysis.md)** - Why it's secure
- **[RSA Attacks](15_rsa_attacks.md)** - Potential vulnerabilities
- **[Real-World RSA](16_real_world_rsa_usage.md)** - Practical implementations

---

# 13. References

1. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.
2. PKCS#1. (2003). RSA Encryption Standard. RSA Security Inc.
3. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
