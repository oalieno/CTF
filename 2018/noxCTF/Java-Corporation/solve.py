#!/usr/bin/env python3
from pwn import *

def wrap(text, size):
    ans = []
    for i in range(0, len(text), size):
        ans.append(text[i:i+size])
    return ans

def xorbytes(x, y):
    ans = []
    for x, y in zip(x, y):
        ans.append(bytes([x ^ y]))
    return b''.join(ans)

cipher = open('./Encrypted.txt', 'rb').read()
blocks = wrap(cipher, 16)
ans = []

for i in range(1, len(blocks)):
    C2 = blocks[i]
    C1 = blocks[i-1]
    rI2 = b""
    for j in range(16):
        r = remote('chal.noxale.com', 3141)
        current_pad = j + 1
        set_pad = xorbytes(bytes([current_pad] * j), rI2[::-1])
        for k in range(256):
            guess = b'A' * (16 - 1 - j) + bytes([k]) + set_pad
            r.send(str(len(guess + C2)))
            r.send(guess + C2)
            result = r.recvn(1)
            if result == b'1':
                rI2 += bytes([current_pad ^ k])
                break
        r.close()
    I2 = rI2[::-1]
    P2 = xorbytes(C1, I2)
    ans.append(P2)
    print(ans)

print(b''.join(ans))
