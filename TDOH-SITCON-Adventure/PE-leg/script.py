#!/usr/bin/env python

ans = ""

with open("matlab-output.txt") as flag:
    data = flag.read().strip()
    data = data.split(',')
    for d in data:
        d = int(d.strip())
        ans += chr(d)

print ans
