#!/usr/bin/env python3
import functools
import gmpy2
from Crypto.Util.number import inverse
from pwn import *

context.log_level = 'ERROR'

def chinese_remainder(n, a):
    sum = 0
    prod = functools.reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * inverse(p, n_i) * p
    return sum % prod

def read(r, filename, e):
    r.sendline('2')
    r.sendline(filename)
    r.recvuntil('N = ')
    n = int(r.recvline().strip(), 16)
    r.sendline(str(e))
    r.recvuntil('C = ')
    c = int(r.recvline().strip(), 16)
    return (n, c)

def custom(r, m, e):
    r.sendline('3')
    r.recvuntil('N = ')
    n = int(r.recvline().strip(), 16)
    r.sendline(str(e))
    result = r.recvuntil('432 bytes)\n')
    if b"Invalid E" in result:
        return None
    r.sendline(m)
    r.recvuntil('C = ')
    c = int(r.recvline().strip(), 16)
    r.sendline('n')
    return (n, c)

N = []
C = []

for i in range(3):
    while True:
        r = remote("47.52.195.203", 2333)
        result = custom(r, 'jedi', 3)
        if result != None:
            break
        r.close()
    result = read(r, 'flag', 3)
    N.append(result[0])
    C.append(result[1])
    r.close()

m = chinese_remainder(N, C)
res = gmpy2.iroot(m, 3)
print(int(res[0]).to_bytes(216, 'big'))
