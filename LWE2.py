import numpy as np
import random as rm


class LWE:
    """
    Instance of tool for functions of LWE encryption.

    Attributes:
        n (int): Dimension of the lattice.
        m (int): Number of samples.
        q (int): The modulus.

    Methods:
        gen(): generates public and private keys.
        encrypt(message, pk): encrypts a binary string.
        decrypt(ct, pk): decrypts cyphertext.
    """
    def __init__(self, n=512):
        self.n = n
        self.m = 2*n
        self.q = n**2
    
    def gen(self):
        """
        generates public and private keys.

        Returns:
            (np.array, np.array): The public key (A,s).
        """
        # Generate A by filling a m by n matrix with random integers between 0 and q-1
        A = np.zeros((self.m, self.n), dtype=int)
        for i in range(self.m):
            for j in range(self.n):
                A[i][j] = rm.randint(0, self.q-1)
        
        # Generate s by filling a array with random binary integers
        self.s = np.zeros((self.n,1), dtype=int)
        for i in range(self.n):
            self.s[i][0] = rm.randint(0, 1)
        
        # Generate e with a Gaussian distribution
        e = np.random.normal(scale=1/(self.n ), size=self.m).round().astype(int)
        e = e.reshape(-1, 1)

        # Solve for b
        b = (A @ self.s + e) % self.q
        
        #return the public key
        self.pk = (A, b)
        return self.pk
    
    def encrypt(self, message, pk):
        """
        encrypts a binary string.

        Returns:
            (np.array): The cypher text of message.
        """
        # For every bit gerneate a cyphertext
        ct = []
        for bi in message:
            S = np.random.randint(0, 2, size=self.m)  # Random subset S
            
            sum_Ai = np.zeros(self.n, dtype=int)
            sum_bi = int(bi) * (self.q // 2)

            for i, Si in enumerate(S):
                sum_Ai = (sum_Ai + Si * pk[0][i]) % self.q
                sum_bi = (sum_bi + Si * pk[1][i]) % self.q
            
            ct.append((sum_Ai, sum_bi))
        return ct
    
    def decrpyt(self, ct):
        """
        decrypts a binary string.

        Returns:
            (str): A binary string.
        """
        mes = ''
        for i in ct:
            if (i[1] - np.dot(i[0].T,self.s)) % self.q < self.q/4: # checking if b-<a,s> is closer to 0 than q/2
                mes += '0'
            else:
                mes += '1'
        return mes

# np.random.seed()
# Make two people to exchange keys. 
alice = LWE()
bob = LWE()

# Generate their keys
alice_pk = alice.gen()
bob_pk = bob.gen()

# Encrypt then decrypt the message
message = "100111010011"
ct = alice.encrypt(message, bob_pk)
m = bob.decrpyt(ct)
print(m)