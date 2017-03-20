#!/usr/bin/env python

with open("access-modified.log") as d:
    data = d.read().strip()

flag = ""

last = ""
ans = 0

for line in data.split('\n'):
    status = int(line[:3])
    body = line[49:line.find('>')+1]
    number = int(line[line.find('>')+1:].split()[0])
    if last != body:
        flag += chr(ans)
        ans = 0
        last = body
    if status == 200:
        ans = max(ans,number+1)

print flag
