import numpy as np
from random import SystemRandom
import math

def secret_key_gen(q,n):
    cryptogen = SystemRandom() 
    s =np.empty(n+1)
    for i in range(0, n+1):
        s[i] = cryptogen.randint(0, q)
    s[0] = 1
    return s

def public_key_gen(q, n, N, s):
    cryptogen = SystemRandom() 

    A = []
    for i in range(0, n):
        r = []
        for j in range(0, N):
            x = cryptogen.randint(0, q)
            r.append(x)
        A.append(r)
    A = np.array(A)


    e = np.random.randint(0, q, N)
    b = np.dot(A, s[1:]) + 2 * e
    b.resize(N, 1)
    A = np.hstack((b, -1 * A)) % q
    assert all(np.dot(A, s) % q == (2 * e) % q)
    return A


s = secret_key_gen(100, 5)

public_key_gen(100, 3, 4, [2])