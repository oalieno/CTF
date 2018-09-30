#!/usr/bin/env python3
from pwn import *
import struct

NEQ = b"Looks like you don't know the secret key? Too bad."

r = remote('aes-128-tsb.hackable.software', 1337)

def send_binary(data):
    r.send(struct.pack('<I', len(data)))
    if data:
        r.send(data)

def recv_binary():
    l = struct.unpack('<I', r.recvn(4))[0]
    data = r.recvn(l)
    return data

def pad(data):
    byte = -len(data) % 16
    return data + bytes([byte] * byte)

def wrap(data, step):
    return [data[i:i+step] for i in range(0, len(data), step)]

def xor(X, Y):
    return bytes([x ^ y for x, y in zip(X, Y)])

def send_block(iv, i1, plain):
    i2 = i1
    c1 = xor(iv, i1)
    c2 = xor(c1, i2)
    send_binary(plain)
    send_binary(iv + c1 + c2)
    return recv_binary()

def solve_last(L):
    for x in range(256):
        for l in L:
            if not (1 <= x ^ l <= 15):
                break
        else:
            return x

def solve_block(i1):
    L = []
    for x in range(256):
        iv = b'\x00' * 15 + bytes([x])
        result = send_block(iv, i1, b'')
        if result == NEQ:
            L.append(x)
    j1 = [0] * 16
    j1[-1] = solve_last(L)
    print(j1)
    for i in range(16 - 1):
        iv = b'\x00' * 15 + bytes([j1[-1] ^ (15 - i)])
        for x in range(256):
            result = send_block(iv, i1, bytes(j1[:i] + [x]))
            if result != NEQ:
                j1[i] = x
                print(j1)
                break
    return bytes(j1)

i1 = b'\x00' * 16
j1 = solve_block(i1)

plain = b'gimme_flag'
iv = xor(j1, pad(plain))
enc = send_block(iv, i1, plain)

flag = b''
iv, enc = enc[:16], enc[16:-16]
ct = iv
pt = iv
for block in wrap(enc, 16):
    j1 = solve_block(xor(block, ct))
    p1 = xor(j1, pt)
    ct = block
    pt = p1
    flag += p1
    print(flag)
