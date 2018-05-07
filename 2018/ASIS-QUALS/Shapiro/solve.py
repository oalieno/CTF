#!/usr/bin/env python3
import hashlib
import random
import gmpy2
import json
from pwn import *
from math import gcd
from Crypto.Util.number import inverse

def go(k):
    prime = 2
    ax, ay, mx, my = [], [], [], []
    grid = [[False] * k for i in range(k)]
    for i in range(k):
        for j in range(k):
            if grid[i][j] == False:
                ax.append(-i % prime)
                ay.append(-j % prime)
                mx.append(prime)
                my.append(prime)
                for x in range(i % prime, k, prime):
                    for y in range(j % prime, k, prime):
                        grid[x][y] = True
                prime = gmpy2.next_prime(prime)
    return ax, ay, mx, my

def chinese_remainder(a, m):
    sum = 0
    prod = functools.reduce(lambda a, b: a * b, m)
    for a_i, m_i in zip(a, m):
        p = prod // m_i
        sum += a_i * inverse(p, m_i) * p
    return sum % prod, prod

ax, ay, mx, my = go(10)
xa, xm = chinese_remainder(ax, mx)
ya, ym = chinese_remainder(ay, my)

r = remote("37.139.22.174", 17926)

r.recvlines(6)

def proof_of_work():
    suffix = r.recvline().split(b' = ')[1].strip().decode('ascii')
    i = 0
    while True:
        if hashlib.sha256(str(i).encode('ascii')).hexdigest()[-6:] == suffix:
            r.sendline(str(i))
            break
        i += 1

proof_of_work()

for _ in range(8):
    k = int(r.recvline().strip().split(b" = ")[1])
    line = r.recvline().strip()
    small = b"smaller" in line
    limit = int(line.split(b" than ")[1])

    ans = []
    if small:
        ansx = xa - xm
        ansy = ya - ym
    else:
        ansx = xa
        ansy = ya

    for i in range(ansx, ansx + k):
        for j in range(ansy, ansy + k):
            ans.append((i, j))

    r.sendline(json.dumps(ans))
    result = r.recvline()
    print(result)

r.interactive()
