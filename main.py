from mceliece.mceliececipher import McElieceCipher
import logging
import numpy as np
import sys


m,n,t = 6,63,8
#m,n,t = 5,30,5


mceliece = McElieceCipher(m, n, t)
mceliece.generate_random_keys()
mceliece.to_numpy()

message = b"A\n"
bin_message = np.unpackbits(np.frombuffer(message, dtype=np.uint8))
bin_message = np.trim_zeros(bin_message, 'b')

print("Message original", bin_message)




cipher = mceliece.encrypt(bin_message).to_numpy()
print("Message crypté : ", cipher)

decipher = mceliece.decrypt(cipher)
print("Message décrypté :", decipher)
