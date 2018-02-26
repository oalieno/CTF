#!/usr/bin/env python3
from pwn import *
from Crypto.Util.number import inverse

r = remote("127.0.0.1", 20000)

for i in range(10):
    n = int(r.recvline())
    c2 = int(r.recvline())
    c1 = int(r.recvline())

    f = (c1 + 2 * c2 - 1) % n
    g = (c1 - c2 + 2) % n

    ig = inverse(g, n)

    m = f * ig % n

    r.sendline(str(m))
    print(r.recvline())

r.interactive()
