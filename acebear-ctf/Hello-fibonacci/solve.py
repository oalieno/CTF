#!/usr/bin/env python3
from pwn import *

def mul(a, b, m):
    c = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c[i][j] += a[i][k] * b[k][j] % m
    return c

def fast_power(x, y, m):
    if y == 0:
        return [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
    k = fast_power(x, y // 2, m)
    if y % 2: return mul(mul(k, k, m), x, m)
    else: return mul(k, k, m)

r = remote("35.200.176.244", 8856)

r.recvuntil("Author: kad96\n")

Q = [[1, 0, 1],
     [1, 0, 0],
     [0, 1, 0]]

for _ in range(100):
    n = int(r.recvline().decode('ascii').strip().strip('n='))
    N = int(r.recvline().decode('ascii').strip().strip('N='))
    
    QQ = fast_power(Q, n - 1 - 2, N)
    ans = (QQ[0][0] + QQ[0][1] * 2 + QQ[0][2] * 3) % N

    r.sendline(str(ans))

r.interactive()
