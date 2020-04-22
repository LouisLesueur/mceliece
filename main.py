from mceliece.mceliececipher import McElieceCipher
import logging
import numpy as np
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
#ch.setLevel(logging.DEBUG)
ch.setLevel(logging.INFO)
#ch.setLevel(logging.WARN)
root.addHandler(ch)


mceliece = McElieceCipher(6, 62, 8)
mceliece.generate_random_keys()
mceliece.to_numpy()


message = "CD"
bin_message = ""
for e in message:
    bin_message += bin(ord(e))[2:]
bin_message = np.array(list(bin_message), dtype="int")
print("Message original", bin_message)
cypher = mceliece.encrypt(bin_message)
print("Message crypté : ", cypher)
decipher = mceliece.decrypt(cypher)
print("Message décrypté :", decipher)
