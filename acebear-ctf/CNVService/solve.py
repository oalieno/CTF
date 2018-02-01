#!/usr/bin/env python3
import hashlib
from pwn import *
from base64 import b64encode, b64decode

def xor(A, B):
    assert(len(A) == len(B))
    return bytes([a ^ b for a, b in zip(A, B)])

r = remote("cnvservice.acebear.site", 1337)

def register(name, username):
    r.sendlineafter("Your choice: ", "1")
    r.sendlineafter("Name: ", name)
    r.sendlineafter("Username: ", username)
    r.recvuntil("Cookie: ")
    cookie = r.recvline().strip()
    return b64decode(cookie)

def login(cookie):
    r.sendlineafter("Your choice: ", "2")
    r.sendlineafter("Cookie: ", cookie)

cookie = register('jedi', 'A' * 16)
iv, cipher = cookie[:16], cookie[16:]
origin = cookie

target = xor(hashlib.md5(cipher[:16]).digest(), b"root*".ljust(16, b'A'))

cookie = register('master', 'A' * 16)
iv, cipher = cookie[:16], cookie[16:]

username = xor(hashlib.md5(cipher[:16]).digest(), target)

cookie = register('master', username)
iv, cipher = cookie[:16], cookie[16:]

magic = cipher[16:32]

origin = origin[:32] + magic + origin[48:]

login(b64encode(origin))

r.interactive()
