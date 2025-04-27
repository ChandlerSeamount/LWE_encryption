from keyGen import generate_keys
from RLWEDec import decrypt2
from RLWEEnc import encrypt2

if __name__ == "__main__":
    ciphertext_modulus = 2048
    plaintext_modulus = 7
    message = "0123456"


    public_key, secret_key = generate_keys(len(message), ciphertext_modulus)
    ciphertext = encrypt2(message, public_key, ciphertext_modulus, plaintext_modulus)
    decrypted_message = decrypt2(ciphertext, secret_key, ciphertext_modulus, plaintext_modulus)

    message2 = "1111111"
    ciphertext2 = encrypt2(message2, public_key, ciphertext_modulus, plaintext_modulus)
    for i in range(len(ciphertext2[0])):
        ciphertext2[0][i] = ciphertext2[0][i] + ciphertext[0][i]
        ciphertext2[1][i] = ciphertext2[1][i] + ciphertext[1][i]
    decrypted_message2 = decrypt2(ciphertext2, secret_key, ciphertext_modulus, plaintext_modulus)

    print("Original Message  :", message)
    print("Decrypted Message :", decrypted_message)
    print("Adding Encrypted  : 1111111")
    print("Decrypted Message2:", decrypted_message2)