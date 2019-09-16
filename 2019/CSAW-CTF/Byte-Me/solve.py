#!/usr/bin/env python3
from pwn import *
import string

r = remote('crypto.chal.csaw.io', 1003)

enc = r.recvline().strip()

def oracle(x):
    r.sendlineafter('Tell me something: ', x)
    r.recvline()
    return r.recvline().strip()

prev = enc[:32]
for i in range(1, 17):
    now = oracle('a' * i)[:32]
    if prev == now:
        salt = 16 - i + 1
        break
    prev = now

print(f'salt = {salt}')

flag = ''
for block in range(1, 5):
    for i in range(16):
        x = 'a' * (16 - salt) + 'a' * (16 - 1 - i)
        target = oracle(x)[32 * block:32 * (block + 1)]
        for c in string.printable:
            now = oracle(x + flag + c)[32 * block:32 * (block + 1)]
            if now == target:
                flag += c
                print(flag)
                break

print(flag)

r.interactive()
