#!/usr/bin/env python3
import math
import json
from pwn import *
from Crypto.Util.number import inverse

r = remote("35.185.151.73",8031)

# stage 1

r.recvlines(2)
n = int(r.recvline().strip()[3:])
c = json.loads(r.recvline().strip()[12:].decode('ascii'))

x0 = ord('v') * (n - 1) // 255
x1 = ord('x') * (n - 1) // 255
y0 = c[0]
y1 = c[1]

a = (y0 - y1) * inverse(x0 - x1, n) % n
b = (y0 - a * x0) % n

flag = ""

for y in c:
    x = (y - b) * inverse(a, n) % n
    x = x * 255 // (n - 1) + (x * 255 % (n - 1) > 0)
    flag += chr(x)

print("stage 1 :", flag)

# stage 2

r.recvlines(2)
n = int(r.recvline().strip()[3:])
c = json.loads(r.recvline().strip()[12:].decode('ascii'))
m = len(c) # 9

for i in range(m):
    for j in range(m):
        x = c[i][j]
        x = x * 255 // (n - 1) + (x * 255 % (n - 1) > 0)
        c[i][j] = chr(x)

x0 = "vxctf{Gu3"
y0 = ''.join(c[0])
inverse = [y0.find(x) for x in x0]

flag = ""
for i in range(m):
    for j in range(m):
        flag += c[i][inverse[j]]

print("stage 2 :", flag.strip('\x00'))
