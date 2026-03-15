# Cryptography Introduction

## 1. Overview

Cryptography is the scientific discipline concerned with securing information through mathematical techniques. It enables communication between parties in a manner that prevents unauthorized access, modification, or forgery of the transmitted data. In modern computing systems, cryptography forms the foundation of secure communication protocols, digital authentication systems, and data protection mechanisms.

At its core, cryptography transforms readable information, known as **plaintext**, into an unintelligible form called **ciphertext** using mathematical algorithms and secret parameters known as **keys**. Only entities possessing the correct key can reverse this transformation and recover the original information.

Cryptography has evolved from simple substitution techniques used in ancient military communication into a highly sophisticated field that integrates mathematics, computer science, and information theory.

Modern cryptographic systems rely heavily on concepts from number theory, algebra, probability theory, and computational complexity.

---

## 2. Purpose of Cryptography

The primary purpose of cryptography is to ensure secure communication over potentially insecure channels such as the internet. A cryptographic system is typically designed to satisfy four fundamental security objectives.

### 2.1 Confidentiality

Confidentiality ensures that information remains accessible only to authorized parties. Encryption mechanisms prevent unauthorized entities from reading sensitive data.

For example, when encrypted data travels across a network, any interceptor observing the data cannot interpret its contents without the appropriate key.

---

### 2.2 Integrity

Integrity guarantees that information has not been altered during transmission or storage.

Cryptographic techniques such as **hash functions** and **message authentication codes (MACs)** allow systems to verify that a message remains unchanged from its original state.

---

### 2.3 Authentication

Authentication verifies the identity of the communicating parties. It ensures that the sender of a message is who they claim to be.

Authentication mechanisms are commonly implemented using digital signatures, certificates, or cryptographic challenge–response protocols.

---

### 2.4 Non-Repudiation

Non-repudiation ensures that a sender cannot deny having transmitted a message. Once a message is digitally signed using cryptographic techniques, the origin of the message can be verified.

This property is particularly important in digital contracts, financial systems, and secure communications.

---

## 3. Historical Development of Cryptography

Cryptography has a long historical evolution that reflects the increasing complexity of communication systems and security requirements.

### 3.1 Classical Cryptography

Early cryptographic techniques were primarily designed for military communication. These methods relied on simple transformations of letters or symbols.

Examples include:

- substitution ciphers
- transposition ciphers
- mechanical encryption devices

These classical systems were typically based on secrecy of the algorithm rather than secrecy of the key.

---

### 3.2 Mechanical and Electromechanical Cryptography

During the twentieth century, cryptography became more advanced through the use of mechanical and electromechanical encryption devices. These systems implemented complex transformations that were difficult to analyze without specialized knowledge or equipment.

Such systems represented a transition between manual cryptographic techniques and modern computational cryptography.

---

### 3.3 Modern Cryptography

Modern cryptography began to emerge with the development of computers and digital communication systems. Unlike classical cryptography, modern systems rely on rigorous mathematical principles and computational hardness assumptions.

Modern cryptography is characterized by:

- mathematically defined security models
- formally analyzed algorithms
- computational complexity considerations
- publicly known encryption algorithms with secret keys

This shift marked the transition from **security through obscurity** to **security through mathematics**.

---

## 4. Fundamental Terminology

Understanding cryptography requires familiarity with several core terms.

| Term | Definition |
|-----|------------|
| Plaintext | The original readable message or data |
| Ciphertext | The encrypted form of the message |
| Encryption | The process of converting plaintext into ciphertext |
| Decryption | The process of recovering plaintext from ciphertext |
| Key | A parameter controlling the encryption or decryption process |
| Cryptographic Algorithm | A mathematical procedure used to transform data |
| Cryptanalysis | The study of methods used to break cryptographic systems |

These components form the fundamental structure of any cryptographic system.

---

## 5. Encryption Process

A cryptographic system can be described using a mathematical model consisting of algorithms and keys.

The encryption process can be represented conceptually as:

Plaintext → Encryption Algorithm + Key → Ciphertext

The decryption process reverses this transformation:

Ciphertext → Decryption Algorithm + Key → Plaintext

The security of the system depends on the secrecy of the key rather than the secrecy of the algorithm itself. This principle is known as **Kerckhoffs's Principle**, which states that a cryptographic system should remain secure even if the algorithm is publicly known.

---

## 6. Types of Cryptographic Systems

Cryptographic systems can generally be classified into two major categories based on how encryption and decryption keys are used.

### 6.1 Symmetric Cryptography

Symmetric cryptography uses a single shared key for both encryption and decryption.

Encryption Key = Decryption Key


Both communicating parties must possess the same secret key in advance.

Advantages of symmetric cryptography include high computational efficiency and suitability for encrypting large amounts of data. However, the primary challenge lies in securely distributing the secret key between parties.

---

### 6.2 Asymmetric Cryptography

Asymmetric cryptography, also known as **public-key cryptography**, uses two different but mathematically related keys.
Public Key → used for encryption
Private Key → used for decryption


The public key can be freely distributed, while the private key must remain secret.

This approach eliminates the need for secure key distribution prior to communication and enables new cryptographic applications such as digital signatures and secure key exchange.

One of the most influential public-key cryptosystems is the **RSA algorithm**, which relies on properties of number theory and the difficulty of factoring large integers.

---

## 7. Mathematical Foundations of Cryptography

Modern cryptographic systems rely heavily on mathematics. Several mathematical areas are particularly important.

### 7.1 Number Theory

Number theory studies properties of integers and plays a central role in many cryptographic algorithms. Concepts such as prime numbers, modular arithmetic, and greatest common divisors form the foundation of many encryption methods.

---

### 7.2 Modular Arithmetic

Modular arithmetic describes arithmetic operations performed with respect to a fixed modulus. Instead of working with infinitely growing numbers, calculations wrap around after reaching a specified value.

This concept is fundamental to many cryptographic algorithms, particularly public-key systems such as RSA.

---

### 7.3 Computational Complexity

Cryptographic security often depends on the assumption that certain mathematical problems are computationally difficult to solve.

Examples include:

- integer factorization
- discrete logarithms
- elliptic curve discrete logarithms

While it is easy to compute certain mathematical operations in one direction, reversing them without additional information can be computationally infeasible.

This property is known as a **one-way function**, and it forms the basis of many cryptographic protocols.

---

## 8. Components of a Modern Cryptographic System

A modern cryptographic system typically consists of several interconnected components.

### 8.1 Encryption Algorithms

Encryption algorithms transform plaintext into ciphertext using mathematical operations controlled by cryptographic keys.

---

### 8.2 Key Management

Key management involves the generation, distribution, storage, and revocation of cryptographic keys. Poor key management can compromise the security of even the strongest encryption algorithms.

---

### 8.3 Cryptographic Protocols

Cryptographic protocols define how cryptographic algorithms are used within larger communication systems. These protocols specify procedures for authentication, key exchange, and secure communication.

---

### 8.4 Cryptographic Hash Functions

Hash functions transform input data into fixed-length outputs. They are designed to be deterministic and resistant to collisions.

Hash functions are widely used in data integrity verification and digital signatures.

---

## 9. Applications of Cryptography

Cryptography is an essential component of modern digital infrastructure.

Major applications include:

- secure internet communication
- authentication systems
- digital signatures
- encrypted messaging
- electronic commerce
- secure cloud storage

Protocols used across global networks rely heavily on cryptographic primitives to protect data and verify identities.

---

## 10. Cryptography in Cybersecurity

Within cybersecurity, cryptography serves as a foundational defensive mechanism.

It protects sensitive information against:

- unauthorized access
- interception
- tampering
- identity impersonation

Without cryptography, secure online banking, confidential communications, and electronic identity systems would not be possible.

As digital communication continues to expand, the role of cryptography in protecting information systems becomes increasingly critical.

---

## 11. Limitations and Challenges

Despite its effectiveness, cryptography alone cannot guarantee complete security. Several factors can undermine cryptographic protection.

Common issues include:

- weak key generation
- poor implementation practices
- insecure protocols
- side-channel attacks
- human error in key management

Therefore, cryptography must be implemented as part of a broader security framework that includes secure system design, access control mechanisms, and continuous monitoring.

---

## 12. Conclusion

Cryptography is a fundamental discipline that enables secure communication in modern digital systems. Through the use of mathematical transformations and carefully designed algorithms, it protects sensitive information against unauthorized access and manipulation.

Modern cryptographic systems rely on well-studied mathematical principles and computational hardness assumptions. As technology evolves and computational capabilities increase, cryptographic methods must continually adapt to maintain security.

Understanding the basic concepts of cryptography provides the foundation necessary to study more advanced systems such as public-key cryptography, digital signatures, and secure communication protocols.

---

# 13. Next Steps

This introduction to cryptography provides context for understanding:

- **[RSA History](02_rsa_history.md)** - Development of the RSA cryptosystem
- **[Modular Arithmetic](03_modular_arithmetic.md)** - Mathematical foundation of RSA
- **[RSA Full Algorithm](13_rsa_full_algorithm.md)** - Complete RSA system

---

# 14. References

1. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.

2. Diffie, W., & Hellman, M. E. (1976). "New Directions in Cryptography." *IEEE Transactions on Information Theory*, 22(6), 644-654.

3. Kerckhoffs, A. (1883). "La Cryptographie Militaire." *Journal des Sciences Militaires*, IX, 5-38.

4. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

5. Stallings, W. (2017). *Cryptography and Network Security* (6th ed.). Pearson Education.

6. Schneier, B. (1996). *Applied Cryptography: Protocols, Algorithms, and Source Code in C* (2nd ed.). John Wiley & Sons.

7. Shannon, C. E. (1949). "Communication Theory of Secrecy Systems." *Bell System Technical Journal*, 28(4), 656-715.

8. Kahn, D. (1967). *The Codebreakers: The Comprehensive History of Secret Communication from Ancient Times to the Internet*. Scribner.

9. Durfee, G., & Hellman, M. E. (1996). "Hiding Signatures in Linear Redundancy Check Codes." Technical Report.

10. NIST. (2019). "Recommendation for Key Management: Part 1 – General." National Institute of Standards and Technology, Special Publication 800-57.

11. ISO/IEC. (2012). "Information technology – Security techniques – Cryptographic techniques." ISO/IEC 27032:2012.

12. Burton, D. M. (2010). *Elementary Number Theory* (7th ed.). McGraw-Hill.
