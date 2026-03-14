from src.key_generation import generate_rsa_keys, display_key_generation
from src.encryption import rsa_encrypt
from src.decryption import rsa_decrypt


def get_numeric_input(prompt="Enter numeric message: "):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Input cannot be empty. Please enter a number.")
            continue
        if text.lstrip("+-").isdigit():
            return int(text)
        print("Please enter numeric digits only (e.g. 42).")


def main():
    keys = generate_rsa_keys()
    display_key_generation(keys)
    message = get_numeric_input()
    print("\nEncryption\n")
    ciphertext = rsa_encrypt(message, keys["e"], keys["n"])
    print(f"Message = {message}")
    print(f"Ciphertext = {ciphertext}")
    print("\nDecryption\n")
    decrypted = rsa_decrypt(ciphertext, keys["d"], keys["n"])
    print(f"Decrypted message = {decrypted}")


if __name__ == "__main__":
    main()