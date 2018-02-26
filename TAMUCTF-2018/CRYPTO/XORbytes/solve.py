#!/usr/bin/env python3

def xor(A, B):
    return bytes([x ^ y for x, y in zip(A, B)])

with open('./hexxy', 'rb') as data:
    binary = data.read()

key = xor(binary[:16], bytes([0x7f, 0x45, 0x4c, 0x46, 0x02, 0x01, 0x01, 0x00] + [0x0] * 8))

with open("decrypt-hexxy", 'wb') as data:
    for i in range(0, len(binary), 16):
        data.write(xor(binary[i : i + 16], key))
