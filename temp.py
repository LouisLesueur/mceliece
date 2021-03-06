from mceliece.mceliececipher import McElieceCipher
import numpy as np
import time
import logging
import sys
from utils import generate, encrypt, decrypt


pub_key = np.load('pk.npz', allow_pickle=True)
m,n,t = int(pub_key['m']), int(pub_key['n']), int(pub_key['t'])

print("Params: ",m,n,t)

message = b"A\n"
bin_message = np.unpackbits(np.frombuffer(message, dtype=np.uint8))
bin_message = np.trim_zeros(bin_message, 'b')
print("Message original", bin_message)

cipher = encrypt('pk.npz', bin_message)
print("Message crypté : ", cipher)

decipher = decrypt('sk.npz', cipher)
print("Message décrypté :", decipher)


def temp_atk(cipher, t, N, sk):
    """
    cipher - ciphertext
    t - t parameter of the classicmceliece
    N - number of decryption time to compute at each iteration
    """

    size = cipher.shape[0]
    u = np.zeros(size)

    for i in range(size):
        print(f'step: {i+1}/{size}\r', sep=' ', end='', flush=True)
        sparse = np.zeros(size)
        sparse[i] = 1

        cipher_i = np.bitwise_xor(cipher, sparse.astype('bool'))
        times = np.zeros(N)

        for j in range(N):
            starttime = time.time()
            decrypt(sk, cipher)
            endtime = time.time()
            times[j] = endtime-starttime

        u[i] = np.mean(times)

    M = np.sort(u)[:t]

    return np.array([1 if elem in M else 0 for elem in u])

err_approx = temp_atk(cipher,t,5,'sk.npz')
print("Erreur trouvée par atk:", err_approx)
