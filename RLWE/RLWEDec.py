import numpy as np

def decrypt(secret_key : np.poly1d,     # secret key polynomial
            encoded : tuple,            # encoded message (c0, c1)
            Q : int,                    # bit modulus
            n : int) -> np.array:       # polynomial length 

    ring = np.array([1] + [0] * (n-1) + [1])

    # multiply c1 and the secret key and normalize with the ring
    product = np.floor(np.polymul(encoded[1], secret_key) % Q)
    product = np.floor(np.polydiv(product, ring)[1]) % Q

    #add c0 and normalize
    total = np.polyadd(encoded[0], product) % Q
    message = np.floor(np.polydiv(total, ring)[1]) % Q

    return message