#!/usr/bin/env python3
from pwn import *
from base64 import b64decode

def check(c, d):
    L = 2039
    for klen in range(128, 256):
        success = True
        for j in range(klen):
            kc = c[j]
            kd = d[j]
            for i in range(klen, L, klen):
                if i + j >= L: break
                if c[i + j] ^ kc != d[i + j] ^ kd:
                    success = False
                    break
            if not success: break
        if success: return klen
    return 0

C = []

while True:
    r = remote("challenges1.uiuc.tf", 6464)
    d = b64decode(r.recvline().strip())
    for c in C:
        klen = check(c, d)
        if klen > 0:
            print(klen)
            with open('data/c-{}'.format(klen), 'wb') as data: data.write(c)
            with open('data/d-{}'.format(klen), 'wb') as data: data.write(d)
            exit(0)
    C.append(d)
    r.close()
