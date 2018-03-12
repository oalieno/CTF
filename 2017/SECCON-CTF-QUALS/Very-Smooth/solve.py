#!/usr/bin/env python
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from fractions import gcd
from primefac import williams_pp1

def pollard(n):
    a = 2
    b = 2
    while True:
        a = pow(a,b,n)
        d = gcd(a-1,n)
        if 1 < d < n: return d
        b += 1

public = RSA.importKey(open('public.pem').read())

n = public.n
#p = williams_pp1(n)
p = pollard(n)
q = n / p

private = RSA.construct((public.n, public.e, inverse(public.e, (p - 1) * (q - 1))))
with open('private.pem', 'w') as data:
    data.write(private.exportKey('PEM'))
