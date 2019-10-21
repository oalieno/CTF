#!/usr/bin/env python3
from Crypto.Cipher import AES

R.<x> = GF(2)['x']

def i2p(p):
    return R(Integer(p).bits())

def p2i(p):
    return Integer(p.list(), 2)

def rev(p, n):
    p = (p.list() + [0] * n)[:n]
    return R(p[::-1])

def inverse(p, m):
    return xgcd(p, m)[1]

def power(a, b, m):
    ans = R(1)
    while b != 0:
        if b & 1:
            ans = (ans * a) % m
        a = a * a % m
        b >>= 1
    return ans

def crc32_power(data, a):
    n = 32
    b = len(data) * 8
    K = i2p(0x104C11DB7)
    M = i2p(int.from_bytes(data, 'little'))
    Y = i2p(0xFFFFFFFF)
    M = rev(M, b)
    Y = rev(Y, n)
    S = (M * x ^ n + Y * x ^ b + Y) % K
    crc = S * (power(x, a * b, K) - 1) * inverse(x ^ b - 1, K) % K
    crc = rev(crc, n)
    return int(p2i(crc))

ks = [b'TSG', b'is', b'here', b'at', b'SECCON', b'CTF!']
key = b''
for k in ks:
    key += crc32_power(k, int("1" * 10000)).to_bytes(4, 'big')

c = bytes.fromhex('79833173d435b6c5d8aa08f790d6b0dc8c4ef525823d4ebdb0b4a8f2090ac81e')
aes = AES.new(key, AES.MODE_ECB)
flag = aes.decrypt(c)
print(flag)
