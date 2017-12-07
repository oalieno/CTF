#!/usr/bin/env python3
import textwrap
import requests

record = [[False for __ in range(256)] for _ in range(50)]

while True:
    r = requests.get("https://hackme.inndy.tw/otp/?issue_otp=jedi")
    enc = r.text.strip('\n').split('\n')
    for e in enc:
        for i, v in enumerate(textwrap.wrap(e, 2)):
            record[i][int(v, 16)] = True
    if all(map(lambda x: x.count(True) == 255, record)): break

ans = ''.join(map(lambda x: chr(x.index(False)), record))

print(ans)
