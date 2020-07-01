#!/usr/bin/env python3

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

enc = bytearray([89, 74, 75, 43, 126, 69, 120, 109, 68, 109, 109, 97, 73, 110, 45, 113, 102, 64, 121, 47, 111, 119, 111, 71, 114, 125, 68, 105, 127, 124, 94, 103, 46, 107, 97, 104])

key = open('./hell.txt').read().strip()
key = [int(k) for k in key.split('\n')]

for i in range(len(key)):
    enc[i % len(enc)] = enc[i % len(enc)] ^ key[i]

print(enc)
