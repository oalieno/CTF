#!/usr/bin/env python3

def wrap(text, s):
    return [text[i * s : (i + 1) * s] for i in range(len(text) // s)]

with open("./flag.out", 'rb') as data:
    data = data.read()

ans = ""

for i, d in enumerate(wrap(data, 8)):
    if i % 4 == 3:
        ans += '#'
    else:
        ans += chr(d[0])

print(ans)
