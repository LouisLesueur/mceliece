"""Atk

Usage:
  main.py
  main.py g
"""

from mceliece.mceliececipher import McElieceCipher
import logging
import numpy as np
import sys
from utils import generate, encrypt, decrypt
from docopt import docopt



args = docopt(__doc__, version='Atk')

m,n,t = 6,63,8
#m,n,t = 5,30,5

if args['g']:
    generate(m,n,t,'sk','pk')


message = b"A\n"
bin_message = np.unpackbits(np.frombuffer(message, dtype=np.uint8))
bin_message = np.trim_zeros(bin_message, 'b')
print("Message original", bin_message)

cipher = encrypt('pk.npz', bin_message)
print("Message crypté : ", cipher)

decipher = decrypt('sk.npz', cipher)
print("Message décrypté :", decipher)
