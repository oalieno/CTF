#!/usr/bin/env python3
from pwn import *
from not_des import *
from functools import reduce

b1_key = b'A' * 8
b2_key = bytes([ord('A') ^ (1 << 0)]) + b'A' * 7
b1_input = b'A' * 8
b2_input = b'A' * 8

def n2bits(x, y):
    x = bin(x)[2:]
    x = '0' * (y - len(x)) + x
    return list(map(lambda x: int(x), x))

b3_key = b'\x01' * 8
b3_input = b'\x91\xe6\xde\x98\x9c\x9f\n\xdf'

r = remote('dm-col.ctfcompetition.com', 1337)
r.send(b1_key + b1_input)
r.send(b2_key + b2_input)
r.send(b3_key + b3_input)

r.interactive()
