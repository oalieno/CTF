#!/usr/bin/env python3
from pwn import *

r = remote("macsh.chal.pwning.xxx", 64791)
#r = remote("127.0.0.1", 20000)

def gen_mac(cmd):
    trash = b"echo ".ljust(16, b'A')
    p = -len(cmd) % 16
    pad = bytes([p]) * p
    l = len(cmd).to_bytes(len(cmd), 'big')
    ll = (len(cmd) + 256 * 16).to_bytes(len(cmd), 'big')
    payload = b""
    payload += trash + (l + pad) + trash * 126
    payload += trash + (ll + pad) + trash * 126
    payload += cmd
    r.sendline(b"tag<|>tag " + payload)
    return r.recvline().strip()[5:]

#cmd = b"ls ././././././"
'''
flag.txt
fmac.py
macsh.py
.bashrc
.bash_logout
.profile
'''
cmd = b"cat ./flag.txt"
mac = gen_mac(cmd)
r.sendline(mac + b"<|>" + cmd)

r.interactive()
