#!/usr/bin/env sage
import struct

R = IntegerModRing(0xFFFFFFFB)

def group(data, size):
    ans = []
    for i in range(0, len(data), size):
        ans.append(data[i:i+size])
    return ans

def to_matrix(data):
    ints = struct.unpack('64I', data)
    return Matrix(R, group(ints, 8))

enc = open('flag.enc', 'rb').read()
public = open('public.key', 'rb').read()

C1 = to_matrix(enc[0x000:0x100]) # R x PK1
C2 = to_matrix(enc[0x100:0x200]) # R x PK2
C3 = to_matrix(enc[0x200:0x300]) # R x PK3 + PT

PK1 = to_matrix(public[0x000:0x100])
PK2 = to_matrix(public[0x100:0x200])
PK3 = to_matrix(public[0x200:0x300])

PK = block_matrix(1, 2, [PK1, PK2])
C = block_matrix(1, 2, [C1, C2])

R =  (PK.transpose() \ C.transpose()).transpose()

PT = C3 - R * PK3

flag = ''
for i in range(8):
    for j in range(8):
        flag += chr(PT[i][j])

print flag
