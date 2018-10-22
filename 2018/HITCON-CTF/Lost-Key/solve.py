#!/usr/bin/env python3
import sys
from pwn import *
from Crypto.Util.number import *

gcd = GCD

local = False
if len(sys.argv) > 1 and sys.argv[1] == '-l':
    local = True

def hex2long(x):
    return bytes_to_long(bytes.fromhex(x))

def long2hex(x):
    return long_to_bytes(x).hex()

if local:
    ip, port = '127.0.0.1', 20000
else:
    ip, port = '18.179.251.168', 21700
r = remote(ip, port)

if local:
    realn = int(r.recvline().strip())

r.recvline()
flag = hex2long(r.recvline().strip().decode())

def enc(m):
    m = long2hex(m)
    r.sendlineafter('cmd: ', 'A')
    r.sendlineafter('input: ', m)
    c = hex2long(r.recvline().strip().decode())
    return c

def dec(c):
    c = long2hex(c)
    r.sendlineafter('cmd: ', 'B')
    r.sendlineafter('input: ', c)
    m = hex2long(r.recvline().strip().decode())
    return m

n = gcd(enc(2) ** 2 - enc(2 ** 2), enc(3) ** 2 - enc(3 ** 2))
print('n =', n)
if local:
    print('realn =', realn)

L = 0
H = n
t = enc(256)
c = flag
for _ in range(n.bit_length() // 8):
    c = (t * c) % n
    res = dec(c)
    if res == 0:
        H = n // 256
    else:
        res = -res % 256
        D = H - L
        OL = L
        L = OL + res * D // 256
        H = OL + (res + 1) * D // 256
    print("L =", L)
    print("H =", H)

m = L # plain text
flag = long_to_bytes(m)
print(flag)
if b'hitcon' in flag:
    print(flag)
