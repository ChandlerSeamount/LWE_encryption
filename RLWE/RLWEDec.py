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

from typing import Tuple
from Polynomial_functions import polynomial_mod_add, polynomial_mod_mult


def decrypt2(ciphertext: Tuple[np.array, np.array],         # Ciphertext
              s: np.ndarray,                                # secret key
              ciphertext_modulus: int,                      # The ciphertext modulus
              plaintext_modulus: int) -> str:               # The plaintext modulus
    
    c0, c1 = ciphertext
    #msg = c1 * s + c1
    decrypted = polynomial_mod_add(c0, polynomial_mod_mult(c1, s, ciphertext_modulus), ciphertext_modulus)
    #undo scaling
    descaled = (decrypted * plaintext_modulus + ciphertext_modulus // 2) // ciphertext_modulus
    #take the modulus
    result = descaled % plaintext_modulus
    ans = ""
    for num in result:
        ans += str(int(num))
    return ans