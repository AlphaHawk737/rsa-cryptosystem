from src.key_generation import generate_rsa_keys
from src.encryption import rsa_encrypt
from src.decryption import rsa_decrypt


def encrypt_text(text, e, n):
    return [rsa_encrypt(ord(c), e, n) for c in text]


def decrypt_text(cipher_list, d, n):
    return "".join(chr(rsa_decrypt(c, d, n)) for c in cipher_list)


def get_alphanumeric_input(prompt="Enter message (alphanumeric only): "):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Input cannot be empty. Please try again.")
            continue
        if all(c.isalnum() for c in text):
            return text
        print("Only alphanumeric characters are allowed. Try again.")


def main():
    keys = generate_rsa_keys()
    message = get_alphanumeric_input()
    cipher = encrypt_text(message, keys["e"], keys["n"])
    decrypted = decrypt_text(cipher, keys["d"], keys["n"])
    print("Original:", message)
    print("Cipher:", cipher)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()