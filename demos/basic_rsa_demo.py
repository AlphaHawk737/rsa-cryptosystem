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
            return int(text)  # accept signed integer input
        print("Please enter numeric digits only (e.g. 42).")


def main():
    keys = generate_rsa_keys()  # generate RSA keys
    display_key_generation(keys)
    message = get_numeric_input()  # get numeric plaintext
    print("\nEncryption\n")
    ciphertext = rsa_encrypt(message, keys["e"], keys["n"])  # RSA encrypt
    print(f"Message = {message}")
    print(f"Ciphertext = {ciphertext}")
    print("\nDecryption\n")
    decrypted = rsa_decrypt(ciphertext, keys["d"], keys["n"])  # RSA decrypt
    print(f"Decrypted message = {decrypted}")


if __name__ == "__main__":
    main()