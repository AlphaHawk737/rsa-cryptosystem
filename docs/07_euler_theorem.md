# Euler's Theorem

## 1. Introduction

**Euler's Theorem** is one of the most important results in number theory and forms the mathematical foundation of the RSA cryptosystem. It establishes that for any integer \(a\) coprime to \(n\):

\[
a^{\phi(n)} \equiv 1 \pmod{n}
\]

This elegant relationship is what makes RSA mathematically sound. Without Euler's Theorem, there would be no guarantee that encrypted messages can be correctly decrypted.

---

# 2. Statement of Euler's Theorem

**Theorem**: Let \(n\) be a positive integer and \(a\) be an integer such that \(\gcd(a, n) = 1\). Then:

\[
a^{\phi(n)} \equiv 1 \pmod{n}
\]

---

# 3. Fermat's Little Theorem

**Fermat's Little Theorem** is a special case when \(n\) is prime:

If \(p\) is prime and \(\gcd(a, p) = 1\), then:

\[
a^{p-1} \equiv 1 \pmod{p}
\]

### Example

For \(p = 7\) and \(a = 3\):

\[
3^{6} = 729 = 104 \times 7 + 1 \equiv 1 \pmod{7}
\]

---

# 4. Application to RSA

Euler's Theorem is the foundation that makes RSA work.

### RSA Key Relationship

In RSA:
- Public exponent: \(e\)
- Private exponent: \(d\)
- Relation: \(ed \equiv 1 \pmod{\phi(n)}\)

This means: \(ed = k \cdot \phi(n) + 1\) for some integer \(k\).

### Why Decryption Works

**Encryption**: \(C \equiv M^e \pmod{n}\)

**Decryption**: \(C^d \equiv (M^e)^d \equiv M^{ed} \pmod{n}\)

Since \(ed = k \cdot \phi(n) + 1\):

\[
M^{ed} \equiv M^{k \cdot \phi(n) + 1} \equiv M \cdot (M^{\phi(n)})^k \equiv M \pmod{n}
\]

By Euler's Theorem: \(M^{\phi(n)} \equiv 1 \pmod{n}\)

Therefore: \(M \cdot (1)^k \equiv M \pmod{n}\)

**This proves that decryption correctly recovers the original message!**

---

# 5. Practical Example

### Verify Euler's Theorem: \(n = 15\), \(a = 2\)

- \(\phi(15) = \phi(3 \times 5) = 2 \times 4 = 8\)
- \(2^8 = 256 = 17 \times 15 + 1 \equiv 1 \pmod{15}\) ✓

---

# 6. RSA Example

### Key Generation
- \(p = 7\), \(q = 11\)
- \(n = 77\)
- \(\phi(n) = 6 \times 10 = 60\)
- \(e = 13\)
- \(d = 37\) (since \(13 \times 37 = 481 \equiv 1 \pmod{60}\))

### Encryption and Decryption

Let \(M = 5\):

**Encrypt**: \(C \equiv 5^{13} \equiv 26 \pmod{77}\)

**Decrypt**: \(26^{37} \equiv 5 \pmod{77}\) ✓

---

# 7. Key Takeaways

- **Euler's Theorem**: \(a^{\phi(n)} \equiv 1 \pmod{n}\) when \(\gcd(a,n)=1\)
- **Foundation of RSA**: Makes the link between encryption and decryption
- **Exponent Relation**: \(ed \equiv 1 \pmod{\phi(n)}\) ensures \(M^{ed} \equiv M \pmod{n}\)
- **Correctness Proof**: Decryption works because of the relation \(ed = k\phi(n) + 1\)
- **Security Basis**: Breaking RSA requires factoring \(n\) or computing \(\phi(n)\)

---

# 8. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Rivest, R. L., Shamir, A., & Adleman, L. (1978). "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*, 21(2), 120-126.
3. Burton, D. M. (2010). *Elementary Number Theory* (7th ed.). McGraw-Hill.
