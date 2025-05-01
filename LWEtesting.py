# from RLWE.keyGen import generate_keys
# from RLWE.RLWEDec import decrypt2
# from RLWE.RLWEEnc import encrypt2
from LWE2 import LWE
import matplotlib.pyplot as plt
import random
import time


if __name__ == "__main__":

    size = []
    runTimeLWE = []

    for i in range(1, 10):
        n = i * 50
        size.append(n)

        b = []
        for _ in range(n):
            b.append(random.randint(0, 1))

        binary_str = ''.join(map(str, b))
        start_time = time.time()

        # np.random.seed()
        # Make two people to exchange keys. 
        alice = LWE(len(binary_str))
        bob = LWE(len(binary_str))

        # Generate their keys
        alice_pk = alice.gen()
        bob_pk = bob.gen()

        # Encrypt then decrypt the message
        ct = alice.encrypt(binary_str, bob_pk)
        m = bob.decrpyt(ct)

        end_time = time.time()
        elapsed_time = end_time - start_time
        runTimeLWE.append(elapsed_time)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(size, runTimeLWE, label='LWE', marker='o')
    plt.title('Runtime of LWE')
    plt.xlabel('message size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    # Save the plot
    plt.savefig('runtime_LWE.png')
    plt.close()