from src.modular_arithmetic import modular_exponentiation

def rsa_decrypt(ciphertext, d, n):
    return modular_exponentiation(ciphertext, d, n)