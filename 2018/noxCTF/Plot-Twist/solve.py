#!/usr/bin/env python3
import mt19937predictor
from pwn import *
from Crypto.Util.number import *
from Crypto.Cipher import AES

r = remote('chal.noxale.com', 5115)

def decrypt(key):
    r.recvline()
    r.send(key)
    result = r.recvline()
    print(result)
    return result.strip().split(b': ')[1].decode()

predictor = mt19937predictor.MT19937Predictor()

for i in range(624):
    data = int(decrypt('0' * 16))
    predictor.setrandbits(data, 32)

decrypt(str(predictor.getrandbits(32)).rjust(16, '0'))

r.interactive()
