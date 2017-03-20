#!/usr/bin/env python

with open("enc",'rb') as enc:
    data = enc.read()

ans = ""

key = 217

for d in data:
    ans += chr(ord(d)^key)
    key = (key * 0xc8763) + 9487
    key = key & 0xff

print ans
