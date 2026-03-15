from src.modular_arithmetic import modular_exponentiation

def rsa_encrypt(message, e, n):
    # RSA encryption: ciphertext = message^e mod n
    return modular_exponentiation(message, e, n)