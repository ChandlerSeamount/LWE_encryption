from Polynomial_functions import polynomial_mod_mult, polynomial_mod_add, generate_random_poly_coef1, generate_random_poly, polynomial_mod_sub
import numpy as np
from typing import Tuple

def secret_key_gen(polynomial_degree : int   # the degree of the created polynomial
                   ) -> np.array:
    return generate_random_poly_coef1(polynomial_degree)

def generate_keys(polynomial_degree : int,   # the degree of the created polynomial
                  ciphertext_modulus : int,   # the ciphertext modulus
                  ) -> Tuple[np.array, np.array, np.array]:
    # random key
    s = secret_key_gen(polynomial_degree)
    # random arr
    a = generate_random_poly(polynomial_degree, ciphertext_modulus)
    # random error
    e = generate_random_poly_coef1(polynomial_degree)
    # b = (-a*s) + e
    b = polynomial_mod_add(- polynomial_mod_mult(a, s, ciphertext_modulus), e, ciphertext_modulus)

    return (a, b), s

#test code
def encrypt2(m : str,                      # The message to be encrypted
            pk : Tuple[np.array, np.array],     # The public key
            ciphertext_modulus : int,           # The ciphertext modulus
            plaintext_modulus : int             # The plaintext modulus
            ) -> Tuple[np.array, np.array]:     # THe ciphertext
    pk0, pk1 = pk
    polynomial_degree = len(pk0)
    u = generate_random_poly_coef1(polynomial_degree) 
    e0 = generate_random_poly_coef1(polynomial_degree)
    e1 = generate_random_poly_coef1(polynomial_degree)

    #scale m up so that it isn't lost in the noise
    m_scaled = np.array([((int(bit))*(ciphertext_modulus // plaintext_modulus)) % ciphertext_modulus for bit in m])

    #c0 = pk0 * u + msg + e0
    c0 = polynomial_mod_add(polynomial_mod_add(polynomial_mod_mult(u, pk1, ciphertext_modulus), m_scaled, ciphertext_modulus),e0, ciphertext_modulus)
    #c1 = pk1 * u + e1
    c1 = polynomial_mod_add(polynomial_mod_mult(u, pk0, ciphertext_modulus), e1, ciphertext_modulus)
    
    return c0, c1
    
def decrypt2(ciphertext: Tuple[np.array, np.array],         # Ciphertext
              s: np.ndarray,                                # secret key
              ciphertext_modulus: int,                      # The ciphertext modulus
              plaintext_modulus: int) -> str:               # The plaintext modulus
    
    c0, c1 = ciphertext
    #msg = c1 * s + c1
    decrypted = polynomial_mod_add(c0, polynomial_mod_mult(c1, s, ciphertext_modulus), ciphertext_modulus)
    #undo scaling
    scaled = (decrypted * plaintext_modulus + ciphertext_modulus // 2) // ciphertext_modulus
    #take the modulus
    result = scaled % plaintext_modulus
    ans = ""
    for num in result:
        ans += str(int(num))
    return ans

public_key, secret_key = generate_keys(5, 1024)
message = "11001"
ciphertext = encrypt2(message, public_key, 1024, 2)
decrypted_message = decrypt2(ciphertext, secret_key, 1024, 2)

print("Original Message:", message)
print("Decrypted Message:", decrypted_message)