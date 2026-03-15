from src.modular_arithmetic import modular_exponentiation

def rsa_decrypt(ciphertext, d, n):
    # RSA decryption: message = ciphertext^d mod n
    return modular_exponentiation(ciphertext, d, n)