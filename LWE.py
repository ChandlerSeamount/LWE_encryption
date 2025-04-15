import random

#secret key S and large prime q (these are bad examples, s should be 2^32 bits long and q should be slightly smaller than s)
s = 69
prime = 191


#construct A (public key 1)
A = []
for i in range(20):
    A.append(random.randint(1, 100))

#create vector of errors
e = []
for i in range(20):
    e.append(random.randint(1, 3))

#construct the secound public key B. 
# Bi = Ai * s + ei (mod q)

B = []
for i in range(20):
    B.append((A[i]*s + e[i]) % prime)


Message = "1010"
print("\nMessage: ")
print(Message)

u = []
v = []

#iterate through each bit
for i in range(len(Message)):
    #current bit
    c = Message[i]

    #create a sampling of what i's to use for Ai and Bi
    sample = random.sample(range(20), 3)


    #sum over sampling locations
    sumA = 0
    sumB = 0
    for i in range(3):
        sumA += A[sample[i]]
        sumB += B[sample[i]]
    sumA = sumA % prime
    if c == "1":
        #print("working")
        sumB = (sumB + prime/2) % prime
    else:
        sumB = sumB % prime

    # u = sum samplingA (mod q)
    u.append(sumA)
    # v = sum samplingB + c*q/2 (mod q)
    v.append(sumB)


#two encrypted vectors, where each pair ui vi encodes a bit
print("\nU: ")
print(u)
print("\nV: ")
print(v)

#Dec = vi + ui*s (mod q)
Dec = ""
for i in range(len(Message)):
    x = (v[i] - u[i]*s) % prime
    if (x > prime/2):
        Dec = Dec + "1"
    else:
        Dec = Dec + "0"

print("\nDec: ")
print(Dec)