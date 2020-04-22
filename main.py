from mceliece.mceliececipher import McElieceCipher
import logging
import numpy as np
import sys


def generate(m, n, t):
    mceliece = McElieceCipher(m, n, t)
    mceliece.generate_random_keys()
    return np.array(mceliece.Gp, dtype=np.uint8), np.array(mceliece.S, dtype=np.uint8), np.array(mceliece.S_inv, dtype=np.uint8), np.array(mceliece.H, dtype=np.uint8), np.array(mceliece.G, dtype=np.uint8), np.array(mceliece.P, dtype=np.uint8), np.array(mceliece.P_inv, dtype=np.uint8), np.array(mceliece.g_poly), np.array(mceliece.irr_poly, dtype=np.uint8)


def encrypt(m, n, t, input_arr, Gp):
    mceliece = McElieceCipher(m, n, t)
    mceliece.Gp = Gp

    if mceliece.Gp.shape[0] < len(input_arr):
        raise Exception(f"Input is too large for current N. Should be {mceliece.Gp.shape[0]}")
    output = mceliece.encrypt(input_arr).to_numpy()

    return np.array(output).flatten()


def decrypt(m,n,t,S,S_inv,H,G,P,P_inv,g_poly,irr_poly, input_arr):
    mceliece = McElieceCipher(m, n, t)
    mceliece.S = S
    mceliece.S_inv = S_inv
    mceliece.H = H
    mceliece.G = G
    mceliece.P = P
    mceliece.P_inv = P_inv
    mceliece.g_poly = g_poly
    mceliece.irr_poly = irr_poly

    if len(input_arr) < mceliece.H.shape[1]:
        input_arr = np.pad(input_arr, (0, mceliece.H.shape[1] - len(input_arr)), 'constant')
    return mceliece.decrypt(input_arr)


message = b"A\n"
bin_message = np.unpackbits(np.frombuffer(message, dtype=np.uint8))
bin_message = np.trim_zeros(bin_message, 'b')

print("Message original", bin_message)


m,n,t = 6,63,8
#m,n,t = 5,30,5
Gp,S,S_inv,H,G,P,P_inv,g_poly,irr_poly = generate(m, n, t)

cipher = encrypt(m, n, t, bin_message, Gp)
print("Message crypté : ", cipher)

decipher = decrypt(m,n,t,S,S_inv,H,G,P,P_inv,g_poly,irr_poly, cipher)
print("Message décrypté :", decipher)
