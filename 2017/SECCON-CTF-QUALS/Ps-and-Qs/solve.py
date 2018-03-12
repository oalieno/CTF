#!/usr/bin/env python3
from math import gcd
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

with open('pub1.pub') as data:
    n1 = RSA.importKey(data.read()).n

with open('pub2.pub') as data:
    n2 = RSA.importKey(data.read()).n

g = gcd(n1, n2)

N = n1
p = g
q = N // p

r = (p-1) * (q-1)
e = 65537
d = inverse(e, r)

with open('cipher', 'rb') as data:
    c = bytes_to_long(data.read())

plain = pow(c, d, N)

print(long_to_bytes(plain))
