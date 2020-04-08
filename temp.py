import numpy as np
import time


def temp_atk(cipher, pk, t, N, decrypt):
    """
    cipher - ciphertext
    t - t parameter of the classicmceliece
    pk - The public key
    N - number of decryption time to compute at each iteration
    decrypt - Patterson algorithm function
    """

    n = cipher.shape
    u = np.zeros(n)

    for i in range(n):
        sparse = np.zeros(n)
        sparse[i] = 1

        cipher_i = np.logical_xor(cipher, sparse)
        times = np.zeros(N)

        for j in range(N):
            starttime = time.clock()
            decrypt(cipher_i, pk)
            endtime = time.clock()
            times[j] = endtime-starttime

        u[i] = np.mean(times)

    M = np.sort(u)[:t]

    return np.array([1 if elem in M else 0 for elem in u])
