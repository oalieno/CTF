# -*- coding: utf-8 -*-
from Crypto.Util import number
from Crypto.PublicKey import RSA
from gmpy2 import powmod
import operator
from FLAG import *

def generate_private_key(bits):
    e = 3
    p, q = 1, 1
    while p == q or p % 3 == 1 or q % 3 == 1:
        p = number.getPrime(bits // 2)
        q = number.getPrime(bits // 2)
    return (p * q, 3, powmod(3, -1, (p - 1) * (q - 1)))

def generate_public_key(bits):
    n, e, _ = generate_private_key(bits)
    return n, e

def encrypt(m, e, n):
    return powmod(m, e, n)

def decrypt(c, d, n):
    return powmod(c, d, n)

n, e = generate_public_key(2048)

assert len(FLAG) < 60

m = FLAG * 5
c = encrypt(int(m.encode('hex'), 16), e, n)

f = open('flag.encrypted', 'w')
f.write('n = 0x%s\n' % format(n, 'x'))
f.write('e = 0x%s\n' % format(e, 'x'))
f.write('c = 0x%s\n' % format(c, 'x'))
f.close()

