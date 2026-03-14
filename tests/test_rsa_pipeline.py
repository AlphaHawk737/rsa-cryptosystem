from src.key_generation import generate_rsa_keys
from src.encryption import rsa_encrypt
from src.decryption import rsa_decrypt

def test_rsa_encrypt_decrypt():
    keys = generate_rsa_keys()

    message = 42

    cipher = rsa_encrypt(message, keys["e"], keys["n"])
    decrypted = rsa_decrypt(cipher, keys["d"], keys["n"])

    assert decrypted == message

def test_rsa_multiple_messages():
    keys = generate_rsa_keys()

    messages = [5, 12, 42, 99]

    for m in messages:
        cipher = rsa_encrypt(m, keys["e"], keys["n"])
        decrypted = rsa_decrypt(cipher, keys["d"], keys["n"])

        assert decrypted == m