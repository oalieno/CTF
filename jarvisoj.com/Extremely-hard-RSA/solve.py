#!/usr/bin/env python3
from Crypto.PublicKey import RSA
import gmpy2

with open('public.pem', 'r') as data:
    public = RSA.importKey(data.read())
    n = public.n

with open('flag.enc', 'rb') as data:
    flag = data.read()
    flag = int.from_bytes(flag, byteorder = 'big')

for i in range(0, 130000000):
    message, success = gmpy2.iroot(flag + n * i, 3)
    if success:
        print(int(message).to_bytes(600, byteorder = 'big'))
        exit(0)
