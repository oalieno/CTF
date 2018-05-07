#!/usr/bin/env python3
import gmpy2
import hashlib
from pwn import *

r = remote("37.139.22.174", 11740)

r.recvlines(5)

def proof_of_work():
    suffix = r.recvline().split(b' = ')[1].strip().decode('ascii')
    i = 0
    while True:
        if hashlib.sha256(str(i).encode('ascii')).hexdigest()[-6:] == suffix:
            r.sendline(str(i))
            break
        i += 1

proof_of_work()

for i in range(10):
    r.recvlines(2)

    n = int(r.recvline()[4:].strip())
    print("i =", i)
    print("n =", n)

    x = int(gmpy2.iroot(n, 2)[0])
    ans = n - x ** 2

    power = 3
    while True:
        x = int(gmpy2.iroot(n, power)[0])
        if x == 1: break
        ans = min(ans, n - x ** power)
        power += 1

    r.sendline(str(ans))

r.interactive()
