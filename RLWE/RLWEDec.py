import numpy as np
from typing import Tuple
from Polynomial_functions import polynomial_mod_add, polynomial_mod_mult


def decrypt2(ciphertext: Tuple[np.array, np.array],         # Ciphertext
              s: np.ndarray,                                # secret key
              ciphertext_modulus: int,                      # The ciphertext modulus
              plaintext_modulus: int) -> str:               # The plaintext modulus
    
    c0, c1 = ciphertext
    #msg = c1 * s + c0
    decrypted = polynomial_mod_add(c0, polynomial_mod_mult(c1, s, ciphertext_modulus), ciphertext_modulus)
    #undo scaling
    descaled = (decrypted * plaintext_modulus + ciphertext_modulus // 2) // ciphertext_modulus
    #take the modulus
    result = descaled % plaintext_modulus
    ans = ""
    for num in result:
        ans += str(int(num))
    return ans