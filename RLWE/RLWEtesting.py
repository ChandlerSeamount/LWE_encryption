from keyGen import generate_keys
from RLWEDec import decrypt2
from RLWEEnc import encrypt2
import matplotlib.pyplot as plt
import random
import time

if __name__ == "__main__":

    size = []
    runTimeRLWE = []

    for i in range(1, 15):
        n = i * 10000
        size.append(n)

        b = []
        for _ in range(n):
            b.append(random.randint(0, 1))

        message = ''.join(map(str, b))
        start_time = time.time()

        ciphertext_modulus = 2048
        plaintext_modulus = 7



        public_key, secret_key = generate_keys(len(message), ciphertext_modulus)
        ciphertext = encrypt2(message, public_key, ciphertext_modulus, plaintext_modulus)
        decrypted_message = decrypt2(ciphertext, secret_key, ciphertext_modulus, plaintext_modulus)


        end_time = time.time()
        elapsed_time = end_time - start_time
        runTimeRLWE.append(elapsed_time)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(size, runTimeRLWE, label='RLWE', marker='o')
    plt.title('Runtime of RLWE')
    plt.xlabel('message size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    # Save the plot
    plt.savefig('runtime_RLWE.png')
    plt.close()