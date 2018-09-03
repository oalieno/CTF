#!/usr/bin/env python3
import string
from pwn import *
from Crypto.Util.number import long_to_bytes

table = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def b59encode(text):
    x = int.from_bytes(text, 'big')
    ans = ''
    while x > 0:
        ans += table[x % 59]
        x //= 59
    return ans[::-1]

def b59decode(text):
    ans = 0
    for c in text:
        ans *= 59
        ans += table.index(c)
    return long_to_bytes(ans)

r = remote('crypto.chal.ctf.westerns.tokyo', 14791)
enc = r.recvline().strip().split(b': ')[1]
r.recvline()

mapping = {}

for ch in string.printable[:-5]:
    r.sendlineafter('message: ', ch)
    result = r.recvline().strip().split(b': ')[1]
    real = b59encode(ch.encode())
    for x, y in zip(result.decode(), real):
        mapping[x] = y

flag = ''

for c in enc.decode():
    flag += mapping[c]

print(b59decode(flag))
