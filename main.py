from mceliece.mceliececipher import McElieceCipher
import numpy as np

mceliece = McElieceCipher(6, 60, 2)
mceliece.generate_random_keys()

# Obligé car pas numpy par défaut
mceliece.Gp = np.array(mceliece.Gp)
mceliece.H = np.array(mceliece.H)
mceliece.P = np.array(mceliece.P)
mceliece.P_inv = np.array(mceliece.P_inv)

cypher = mceliece.encrypt(np.array([0, 1, 0, 1, 0, 1, 0]))

print(cypher)
