import numpy as np
from random import SystemRandom

#polynomial math

def polynomial_mod_add(p1 : np.array,
                       p2 : np.array, 
                       q : int) -> np.array:
    length = max(len(p1), len(p2))
    p1 = np.resize(p1, length)
    p2 = np.resize(p2, length)
    return (p1 + p2) % q

def polynomial_mod_mult(p1 : np.array,
                       p2 : np.array,
                       q : int) -> np.array:
    n = len(p1)

    prod = np.array([0] * (2 * n - 1))
    for i in range(n):
        for j in range(n):
            prod[i + j] += p1[i] * p2[j]
    
    #result = prod mod x^n +1
    result = np.array([0] * n)
    for i in range(2 * n - 1):
        coeff = prod[i]
        quotient, remainder = divmod(i, n)
        result[remainder] = (result[remainder] + (-1)**quotient * coeff) % q
    return result

#polynomial generation

def generate_random_poly(polynomial_degree : int,   # the degree of the created polynomial
                         q : int                    # the modulus of the polynomial
                   ) -> np.array:
    cryptogen = SystemRandom()
    # Draw the secret
    return np.array([cryptogen.randint(0, q-1) for _ in range(polynomial_degree)])

def generate_random_poly_coef1(polynomial_degree : int   # the degree of the created polynomial
                   ) -> np.array:
    cryptogen = SystemRandom() 
    # Draw the secret
    s = np.empty((0,))
    for i in range(polynomial_degree):
        x = cryptogen.randint(0, 4)
        if x < 2:
            s = np.append(s, 0)
        elif x == 2:
            s = np.append(s, 1)
        else:
            s = np.append(s, -1)
    return s

def generate_gausian_poly(polynomial_degree : int,   # the degree of the created polynomial
                          mu : int = 0,                  # the mean of the dist
                          std: int = 3.8) -> np.array:   # the standard deviation
    cryptogen = SystemRandom() 
    return np.array([round(cryptogen.gauss(mu, std)) for _ in range(polynomial_degree)], dtype=object)