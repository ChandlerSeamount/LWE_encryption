import numpy as np
from typing import Tuple
from Polynomial_functions import generate_random_poly_coef1, generate_gausian_poly, polynomial_mod_add, polynomial_mod_mult

def encrypt2(m : str,                      # The message to be encrypted
            pk : Tuple[np.array, np.array],     # The public key
            ciphertext_modulus : int,           # The ciphertext modulus
            plaintext_modulus : int             # The plaintext modulus
            ) -> Tuple[np.array, np.array]:     # THe ciphertext
    pk0, pk1 = pk
    polynomial_degree = len(pk0)
    u = generate_random_poly_coef1(polynomial_degree) 
    e0 = generate_gausian_poly(polynomial_degree)
    e1 = generate_gausian_poly(polynomial_degree)

    #scale m up so that it isn't lost in the noise
    m_scaled = np.array([((int(bit))*(ciphertext_modulus // plaintext_modulus)) % ciphertext_modulus for bit in m])

    #c0 = pk0 * u + msg + e0
    c0 = polynomial_mod_add(polynomial_mod_add(polynomial_mod_mult(u, pk1, ciphertext_modulus), m_scaled, ciphertext_modulus),e0, ciphertext_modulus)
    #c1 = pk1 * u + e1
    c1 = polynomial_mod_add(polynomial_mod_mult(u, pk0, ciphertext_modulus), e1, ciphertext_modulus)
    
    return c0, c1