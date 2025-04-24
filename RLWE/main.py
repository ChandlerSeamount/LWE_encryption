from keyGen import generate_keys
from RLWEDec import decrypt2
from RLWEEnc import encrypt2

if __name__ == "__main__":
    ciphertext_modulus = 1024
    plaintext_modulus = 7
    message = "110110101010"


    public_key, secret_key = generate_keys(len(message), ciphertext_modulus)
    ciphertext = encrypt2(message, public_key, ciphertext_modulus, plaintext_modulus)
    decrypted_message = decrypt2(ciphertext, secret_key, ciphertext_modulus, plaintext_modulus)

    print("Original Message: ", message)
    print("Decrypted Message:", decrypted_message)