#!/usr/bin/env python
import string

good = map(ord,string.ascii_letters + string.punctuation + string.digits + ' ')

key = "A qua"

def solve(leng,data):
    base = len(data)-32-leng
    key = ['A', ' ', 'q', 'u', 'a'] + [' '] * (leng - 5)
    known = [True] * 5 + [False] * (leng-5)
    while not all(known):
        for i in xrange(len(data)-32-leng,len(data)-32):
            ch = 0
            if known[i%leng]:
                ch = ord(key[i%leng]) ^ ord(data[i])
            if ch in good:
                known[i-base] = True
                key[i-base] = chr(ch)
    return ''.join(key)

with open('true') as d:
    data = d.read().strip().decode('hex')

key_leng = 67

key = solve(key_leng,data)
flag = ""

for i in xrange(len(data)):
    flag += chr(ord(key[i%key_leng]) ^ ord(data[i]))

print flag
