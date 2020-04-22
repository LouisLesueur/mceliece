from mceliece.mceliececipher import McElieceCipher
import numpy as np
import time


m, n, t = 4, 15, 2

mceliece = McElieceCipher(m, n, t)
mceliece.generate_random_keys()
mceliece.to_numpy()

message = np.array([0, 1, 0, 1, 0, 1, 0])
print("Message original", message)
cypher = mceliece.encrypt(message).astype('bool')



def temp_atk(cipher, t, N, mceliece):
    """
    cipher - ciphertext
    t - t parameter of the classicmceliece
    N - number of decryption time to compute at each iteration
    """

    n = cipher.shape[0]
    u = np.zeros(n)

    for i in range(n):
        sparse = np.zeros(n)
        sparse[i] = 1

        cipher_i = np.bitwise_xor(cipher, sparse.astype('bool'))
        times = np.zeros(N)

        for j in range(N):
            starttime = time.time()
            mceliece.decrypt(cipher_i)
            endtime = time.time()
            times[j] = endtime-starttime

        u[i] = np.mean(times)

    M = np.sort(u)[:t]

    return np.array([1 if elem in M else 0 for elem in u])

print(temp_atk(cypher,t,10,mceliece))
