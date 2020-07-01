#!/usr/bin/env python3
from pwn import *
from base64 import *

r = remote('60.250.197.227', 12001)
r.recvuntil('token: ')
token = b64decode(r.recvline())
token = token[:74] + bytes([token[74] ^ 1]) + token[75:]
r.sendlineafter('username : ', 'maojui')
r.sendlineafter('password : ', 'SECRET')
r.sendlineafter('TOKEN : ', b64encode(token))

r.interactive()
