from Polynomial_functions import polynomial_mod_mult, polynomial_mod_add, generate_random_poly_coef1, generate_random_poly, generate_gausian_poly
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