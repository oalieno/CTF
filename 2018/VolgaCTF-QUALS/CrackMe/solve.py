#!/usr/bin/env python3
from Crypto.Cipher import AES

with open('./CrackMe.txt', 'rb') as data:
    cipher = data.read()

iv, cipher = cipher[:16], cipher[16:]

for guess in range(400000000, 2 ** 32):
    if guess % 1000000 == 0: print(guess)
    key = guess.to_bytes(4, 'big') * 4
    aes_dec = AES.new(key, AES.MODE_CBC, iv)
    d = aes_dec.decrypt(cipher)
    if d[:8] == b"VolgaCTF":
        print(d)
        break
