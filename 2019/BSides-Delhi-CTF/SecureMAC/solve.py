#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import *
from Crypto.Cipher import AES
from math import gcd

r = remote('35.188.170.152', 1337)

r.recvline()
n = int(r.recvline().split()[1])
c = int(r.recvline().split()[1])
enc_key = int(r.recvline().split()[1])
e = 65537

f = bytes_to_long(b"fake_flag")
p = gcd(pow(f, e) - c, n)
q = n // p
print(p)
print(q)
print(n % p)
phi = (p - 1) * (q - 1)
assert(gcd(e, phi) == 1)
d = inverse(e, phi)
key = pow(enc_key, d, n)
key = long_to_bytes(key)

aes = AES.new(key, AES.MODE_ECB)

m1 = b'\x00' * 15 + b'\x00'
m1 += aes.encrypt(m1)

m2 = b'\x00' * 15 + b'\x01'
m2 += aes.encrypt(m2)

r.sendline(m1.hex())
r.sendline(m2.hex())

r.interactive()
