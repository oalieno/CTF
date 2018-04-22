# -*- coding: utf-8 -*-
from Crypto.Util import number
from Crypto.PublicKey import RSA
from gmpy2 import next_prime, gcd, powmod
import operator
from FLAG import *

def generate_private_key(bits, prime_size):
    e = 65537
    assert bits // prime_size >= 1024, 'The smallest prime factor should be of 1024 bits!'
    while 1:
        P = [number.getPrime(bits // prime_size)]
        for i in range(prime_size - 1):
            P.append(next_prime(P[i] * 2))
        n = reduce(operator.mul, P)
        phi_n = reduce(operator.mul, [(x-1) for x in P])
        if gcd(phi_n, e) != 1: continue
        d = powmod(e, -1, phi_n)
        break
    return (int(n), e, d)

def generate_public_key(bits, prime_size):
    n, e, _ = generate_private_key(bits, prime_size)
    return n, e

def encrypt(m, e, n):
    return powmod(m, e, n)

def decrypt(c, d, n):
    return powmod(c, d, n)

n, e = generate_public_key(4096, 4)
c = encrypt(int(FLAG.encode('hex'), 16), e, n)

f = open('flag.encrypted', 'w')
f.write('n = 0x%s\n' % format(n, 'x'))
f.write('e = 0x%s\n' % format(e, 'x'))
f.write('c = 0x%s\n' % format(c, 'x'))
f.close()