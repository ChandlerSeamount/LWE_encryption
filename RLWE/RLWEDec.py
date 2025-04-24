import numpy as np

def decrypt(secret_key : np.poly1d,             # secret key polynomial
            c0 : np.poly1d,                    # encoded message (c0, c1)
            c1 : np.poly1d,
            Q : int,                            # polynomial modulus
            n : int,                            # polynomial length 
            plaintext_mod : int):   # plaintext modulus 

    ring = np.poly1d([1] + [0] * (n-1) + [1])

    first = np.polymul(c1, secret_key)
    first = mod_center(first, Q)
    first = np.polydiv(first, ring)[1]
    first = mod_center(first, Q)

    
    new_msg = np.polyadd(c0, first)
    new_msg = mod_center(new_msg, Q)
    new_msg = np.polydiv(new_msg, ring)[1]
    new_msg = mod_center(new_msg, Q)

    plaintext_msg = new_msg.c % plaintext_mod

    noise = np.max(np.abs(new_msg.c))
    noise = noise < Q//2

    return plaintext_msg, noise
    
def mod_center(x, m: int):
    if type(x)==np.poly1d:
        coef = x.c
        new_coef = (coef + m // 2) % m - m // 2
        return np.poly1d(new_coef)
    else:
        return (x + m // 2) % m - m // 2

"""
tried to do en example here to no avail
q = 11
n = 4
plaintext_mod = 2

msg = np.poly1d([1,0,0,1])

secret_key = np.poly1d([0, -1, 1, 0])
ring = np.poly1d([1,0,0,0,1])

e = np.poly1d([1,0,-1,0])

a = np.poly1d([2, 5, 3, 8])

first = np.polymul(a, secret_key)
first = np.polydiv(first, ring)[1]
second = np.polymul(e, plaintext_mod)

pk0 = np.polyadd(first, second)
pk1 = np.polymul(a, -1)

print("pk0: ")
print(pk0)
print("pk1:")
print(pk1)

u = np.poly1d([1,0,0,-1])
e0 = np.poly1d([1, 0,-1,0])
e1 = np.poly1d([0,1,1,-1])

first = np.polymul(pk0, u)
second = np.polymul(e0, 2)
c0 = np.polyadd(first, second)
c0 = np.polyadd(c0, msg)

print("c0:")
print(c0)

c0 = np.polydiv(c0, ring)[1]

print("c0:")
print(c0)

#c1 = np.poly1d([])"""



q = 2744103875
n = 2**4
plaintext_mod = 7

secret_key = np.poly1d([-1, 0, -1, 0, -1, 0, -1, -1, 1, 0, 0, 0, -1, 0, 0, 0])
c0 = np.poly1d([-737558948, -713379070, 694192576, 213181798, 16958402, -1246650270, 429237533, -842237688, 
                        1261468670, -373705889, -871140245, -598673598, 254778709, -1329147095, -578799095, -908134074])
c1 = np.poly1d([811902, -877588556, 1098457073, -1188198461, -1237157618, 1217140792, -1237039651, 1168443940,
                        -962051475, -1354042542, -1011787558, -4874771, 1010546968, -551008631, -375343779, -1167722027])

##test = np.poly1d([5, 13, -2])
#print(type(test))

message = decrypt(secret_key, c0, c1, q, n, plaintext_mod)
original = np.poly1d([6, 1, 3, 3, 4, 1, 0, 0, 3, 4, 6, 2, 1, 5, 2, 2])

print("Initial:", original.c)
print("deconded:", message[0].astype(int))

#print(poly_mod(test, 10))
#print(poly_mod2(test, 10))

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