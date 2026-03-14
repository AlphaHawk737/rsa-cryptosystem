from src.modular_arithmetic import modular_exponentiation

def rsa_encrypt(message, e, n):
    return modular_exponentiation(message, e, n)