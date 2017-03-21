#!/usr/bin/env python

from __future__ import division

def bits(f):
    bytes = (ord(b) for b in f.read())
    array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    now = 0
    for b in bytes:
        array[now] = b
        if now == 14:
            yield array
        now = (now+1)%15

flag = ""

for b in bits(open('image-with-flag-defect.jpg.hamming', 'r')):
    ans = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    multiply = 1
    for i in xrange(8):
        parity = [0,0,0,0]
        for j in xrange(4):
            for k in xrange(1,16):
                if k&(1<<j):
                    parity[j] ^= b[k-1]%2
        if parity[0] or parity[1] or parity[2] or parity[3]:
            b[parity[0]*1+parity[1]*2+parity[2]*4+parity[3]*8-1] ^= 1
        for j in xrange(1,16):
            ans[j-1] += multiply*(b[j-1]%2)
            b[j-1] //= 2
        multiply *= 2
    for i in xrange(1,16):
        if i != 1 and i != 2 and i != 4 and i != 8:
            flag += chr(ans[i-1])

with open("flag.jpg","w") as f:
    f.write(flag)
