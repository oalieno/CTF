#!/usr/bin/env python3
import string
from pwn import *

def xor(A, B):
    return bytearray([a ^ b for a, b in zip(A, B)])

r = remote("hackme.inndy.tw", 7700)

r.recvuntil("Try to decode the cipher:\n")
flag_enc = bytearray.fromhex(r.recvline().strip().decode("ascii"))
flag = [[True] * 128 for i in range(32)]
good = list(map(ord, string.ascii_lowercase))

while True:
    r.recvuntil("(Press any key to continue)\n")
    r.sendline()
    enc = bytearray.fromhex(r.recvline().strip().decode("ascii"))
    now = xor(flag_enc, enc)
    for i in range(32):
        for guess in range(128):
            if now[i] ^ guess not in good: flag[i][guess] = False
    if all(map(lambda x: x.count(True) == 1, flag)): break

print(''.join(map(lambda x: chr(x.index(True)), flag)))

r.interactive()
