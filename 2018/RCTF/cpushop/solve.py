#!/usr/bin/env python3
import hashpumpy
from pwn import *

r = remote("cpushop.2018.teamrois.cn", 43000)

r.sendlineafter("Command: ", '2')
r.sendlineafter("Product ID: ", '9')
r.recvuntil('Your order:\n')
order = r.recvline().strip()
data, sign = order.split(b'&sign=')

for i in range(8, 32 + 1):
    new_hash, new_data = hashpumpy.hashpump(sign, data, '&price=0', i)
    r.sendlineafter("Command: ", '3')
    r.sendlineafter("Your order: ", new_data + b'&sign=' + new_hash.encode('ascii'))
    if b'Invalid' not in r.recvline():
        r.interactive()

r.interactive()
