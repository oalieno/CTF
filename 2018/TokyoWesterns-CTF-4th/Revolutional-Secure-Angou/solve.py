#!/usr/bin/env python3
from math import gcd
from gmpy2 import iroot
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

rsa = RSA.importKey(open('./publickey.pem').read())

n = rsa.n
e = rsa.e

# k * p * p + p - e * n = 0
for k in range(1, 65537):
    p = (iroot(1 + 4 * k * e * n, 2)[0] - 1) // (2 * k)
    if gcd(n, p) > 1:
        break

q = n // p
c = bytes_to_long(open('./flag.encrypted', 'rb').read())
r = (p - 1) * (q - 1)
d = inverse(e, r)
m = pow(c, d, n)
print(long_to_bytes(m))
