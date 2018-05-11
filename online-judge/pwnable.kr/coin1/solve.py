#!/usr/bin/env python3
from pwn import *

r = remote("pwnable.kr", 9007)

r.recvuntil("- Ready? starting in 3 sec... -\n\t\n")

for i in range(100):
    print(i)
    exec(r.recvline().strip().replace(b' ', b';'))

    l = 0
    h = N - 1
    for _ in range(C):
        m = (l + h) // 2
        r.sendline(' '.join(map(str, range(l, m + 1))))
        price = int(r.recvline().strip())
        if price % 10 == 9:
            h = m
        else:
            l = m + 1

    r.sendline(str(l))
    print(r.recvline())

r.interactive()
