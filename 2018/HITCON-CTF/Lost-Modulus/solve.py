#!/usr/bin/env python3
import sys
from pwn import *
from Crypto.Util.number import *

def enc(r, m):
    m = long_to_bytes(m).hex()
    r.sendlineafter('cmd: ', 'A')
    r.sendlineafter('input: ', m)
    c = r.recvline().strip().decode()
    return bytes_to_long(bytes.fromhex(c))

def dec(r, c):
    c = long_to_bytes(c).hex()
    r.sendlineafter('cmd: ', 'B')
    r.sendlineafter('input: ', c)
    m = r.recvline().strip().decode()
    return bytes_to_long(bytes.fromhex(m))

local = False
if len(sys.argv) > 1 and sys.argv[1] == '-l':
    local = True

if local:
    ip, port = '127.0.0.1', 20000
else:
    ip, port = '13.112.92.9', 21701

def get_14_flag(flag):
    r = remote(ip, port)

    if local:
        realn = int(r.recvline().strip().decode())

    r.recvline()
    f = bytes_to_long(bytes.fromhex(r.recvline().strip().decode()))

    n = 0
    for i in range(1023, 7, -1):
        res = dec(r, enc(r, (1 << i) + n))
        if res == 0:
            n |= (1 << i)

    n |= 0x100 - dec(r, enc(r, n + 0x100))

    print('n:', n)
    if local:
        print('realn:', realn)

    g = n + 1
    for i in range(len(flag)):
        f = f * pow(g, -flag[-(i+1)] % n, n * n) % (n * n)
        f = pow(f, inverse(2 ** 8, n), n * n)
    for i in range(14):
        d = dec(r, f)
        flag = bytes([d]) + flag
        f = f * pow(g, -d % n, n * n) % (n * n)
        f = pow(f, inverse(2 ** 8, n), n * n)

    r.close()

    return flag

flag = b''
for i in range(6):
    flag = get_14_flag(flag)
    print(flag)

print(flag)
