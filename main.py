from mceliece.mceliececipher import McElieceCipher
import numpy as np

mceliece = McElieceCipher(4, 15, 2)
mceliece.generate_random_keys()
mceliece.to_numpy()

message = np.array([0, 1, 0, 1, 0, 1, 0])
print("Message original", message)
cypher = mceliece.encrypt(message)
print("Message crypté : ", cypher)
decipher = mceliece.decrypt(cypher)
print("Message décrypté :", decipher)
