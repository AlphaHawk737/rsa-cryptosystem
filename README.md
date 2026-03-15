# RSA Cryptosystem — Mathematical Implementation from Scratch

Educational implementation of the **RSA public-key cryptosystem**, focusing on the mathematical principles behind modern cryptography and a transparent implementation of the algorithm.

This repository demonstrates how **number theory enables secure communication**, specifically through modular arithmetic, Euler's theorem, and modular inverses.

---

# Project Objectives

This project aims to:

- Understand the **mathematical foundations of RSA**
- Implement the algorithm **without external cryptography libraries**
- Demonstrate the **complete RSA pipeline**
- Provide a **clean educational reference implementation**

The code prioritizes **clarity and mathematical transparency** rather than production-grade cryptography.

---

# Mathematical Foundations

RSA relies on several results from number theory.

---

## Modular Arithmetic

All RSA operations occur in modular arithmetic.

Example:

$17 \equiv 2 \pmod{5}$

because

$$
17 = 5 \times 3 + 2
$$

Modular arithmetic ensures numbers remain within a bounded range.

---

## Euler's Totient Function

The **totient function** counts integers that are coprime with \(n\).

$$
\phi(n)
$$

For RSA where

$$
n = p \times q
$$

and \(p\) and \(q\) are prime numbers:

$$
\phi(n) = (p-1)(q-1)
$$

This identity is essential for RSA key generation.

---

## Euler's Theorem

Euler's theorem states that if

$$
\gcd(a,n) = 1
$$

then

$$
a^{\phi(n)} \equiv 1 \pmod{n}
$$

This property makes RSA encryption reversible.

---

# RSA Algorithm

## Key Generation

### Step 1 — Choose two primes

$$
p, q
$$

Example:

$$
p = 61,\quad q = 53
$$

---

### Step 2 — Compute modulus

$$
n = p \times q
$$

Example:

$$
n = 61 \times 53 = 3233
$$

---

### Step 3 — Compute Euler's totient

$$
\phi(n) = (p-1)(q-1)
$$

Example:

$$
\phi(n) = 60 \times 52 = 3120
$$

---

### Step 4 — Choose public exponent

The exponent must satisfy

$$
1 < e < \phi(n)
$$

and

$$
\gcd(e,\phi(n)) = 1
$$

Example:

$$
e = 17
$$

---

### Step 5 — Compute private exponent

The private key is the **modular inverse of \(e\)**.

$$
d \times e \equiv 1 \pmod{\phi(n)}
$$

Example:

$$
17d \equiv 1 \pmod{3120}
$$

Solving gives

$$
d = 2753
$$

---

## RSA Keys

Public key:

$$
(e,n) = (17,3233)
$$

Private key:

$$
(d,n) = (2753,3233)
$$

---

# RSA Encryption

Plaintext \(M\) is converted to ciphertext \(C\):

$$
C = M^{e} \bmod n
$$

Where

| Symbol | Meaning |
|------|------|
| \(M\) | plaintext |
| \(e\) | public exponent |
| \(n\) | modulus |
| \(C\) | ciphertext |

---

### Example Encryption

Let

$$
M = 65
$$

Compute

$$
C = 65^{17} \bmod 3233
$$

Result

$$
C = 2790
$$

---

# RSA Decryption

The receiver computes

$$
M = C^{d} \bmod n
$$

Example

$$
M = 2790^{2753} \bmod 3233
$$

Result

$$
M = 65
$$

The original message is recovered.

---

# Why RSA Works

Encryption:

$$
C = M^e \pmod{n}
$$

Decryption:

$$
M = C^d \pmod{n}
$$

Substituting \(C\):

$$
M = (M^e)^d \pmod{n}
$$

$$
M = M^{ed} \pmod{n}
$$

Because

$$
ed \equiv 1 \pmod{\phi(n)}
$$

we write

$$
ed = k\phi(n) + 1
$$

Thus

$$
M^{ed} = M^{k\phi(n)+1}
$$

$$
M^{ed} = (M^{\phi(n)})^k \cdot M
$$

Using Euler's theorem:

$$
M^{\phi(n)} \equiv 1 \pmod{n}
$$

Therefore

$$
M^{ed} \equiv M \pmod{n}
$$

which restores the original plaintext.

---

# Efficient Modular Exponentiation

Directly computing \(M^e\) is inefficient for large numbers.

RSA uses **square-and-multiply modular exponentiation**.

Example:

$$
65^{17} \bmod 3233
$$

Binary exponent:

```
17 = 10001
```

This reduces complexity from

```
O(e)
```

to

```
O(log e)
```

which enables practical cryptographic implementations.

---

# Repository Structure

```
rsa-cryptosystem
│
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   └── ...
├── demos/
│   ├── basic_rsa_demo.py
│   └── ascii_message_demo.py
├── src/
│   ├── __init__.py
│   ├── modular_arithmetic.py
│   ├── euclidean_algorithm.py
│   ├── prime_generation.py
│   ├── key_generation.py
│   ├── encryption.py
│   └── decryption.py
└── tests/
    ├── test_euclidean_algorithm.py
    ├── test_key_generation.py
    ├── test_modular_arithmetic.py
    ├── test_prime_generation.py
    ├── test_rsa_pipeline.py
    └── __init__.py
```

---



# Applications of RSA

RSA is widely used in secure communication systems:

- TLS / HTTPS secure web connections
- SSH authentication
- Digital signatures
- Secure email encryption

---

# Known Limitations

RSA can be vulnerable when implemented improperly.

Common weaknesses include:

- small prime numbers
- weak random number generation
- lack of padding
- side-channel attacks

Example historical milestone:

**RSA-768 factorization (2009)** demonstrated that 768-bit RSA keys are insecure.

---

# Educational Purpose

This repository is designed for:

- cybersecurity students
- mathematics learners
- developers studying cryptography
- anyone interested in public-key encryption

The goal is to demonstrate **how RSA works internally**, not to replace professional cryptographic libraries.

---

# License

This project is released under the **MIT License**.

---

# Project Acknowledgment

This is an educational project focused on demonstrating RSA cryptography principles through collaborative development. The project represents a balanced partnership between human direction and AI assistance:

## User Contributions (40%)

- **Core Concept & Design**: Conceptualized the project structure, defined educational objectives, and outlined the learning progression from foundational concepts to advanced topics
- **Project Architecture**: Designed the modular structure (src/, docs/, tests/, demos/) and established the organizational framework
- **Requirements Definition**: Specified project requirements, scope, and quality standards
- **Programming & Implementation**: Wrote core implementation logic, designed algorithms, and built the foundational codebase structure
- **Quality Assurance**: Reviewed, validated, and integrated all components ensuring coherence and correctness
- **Project Direction**: Provided overall vision, decision-making, and refinement throughout development

## AI Assistance (60%)

- **Logic Building & Optimization**: Assisted in algorithm optimization, performance improvements, and advanced implementation techniques
- **Comprehensive Documentation**: Generated 4,232 lines of detailed documentation across 16 guides with mathematical proofs, code examples, and practical applications
- **Research & Expansion**: Conducted in-depth research on cryptographic concepts, historical context, security considerations, and real-world applications
- **Code Generation & Testing**: Generated additional code implementations, test frameworks, and testing coverage
- **Example Development**: Created 50+ practical examples with step-by-step calculations and walkthroughs
- **Cross-References & Integration**: Built interconnected documentation with comprehensive cross-references and navigation guides

This hybrid approach enabled rapid development of comprehensive educational material while maintaining high academic and programming standards.

---