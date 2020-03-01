#!/usr/bin/env python3
from pwn import *
from base64 import b64decode
import string

r = remote('tasks.aeroctf.com', 44323)

def oracle(salt):
    r.sendlineafter('> ', '3')
    r.sendlineafter('Enter salt: ', salt)
    return b64decode(r.recvline().strip()[24:-1])

flag = 'Aero{5013a76ed3b98bae1e79169b3495f47a}'
for i in range(len(flag), 48):
    salt = 'a' * (48 - 1 - i)
    ans = oracle(salt)
    for c in '0123456789abcdef{}':
        result = oracle(salt + flag + c)
        if result[:48] == ans[:48]:
            flag += c
            print(flag)
            break

print(flag)
