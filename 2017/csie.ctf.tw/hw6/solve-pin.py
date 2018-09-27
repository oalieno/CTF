#!/usr/bin/env python3
import time
import string
import subprocess

def e(s):
    return s.encode('utf-8')

def d(s):
    return s.decode('utf-8')

def command(cmd, inp):
    p = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return p.communicate(inp)[0]

ans = ""

while True:
    record = {}
    for s in string.ascii_letters + string.punctuation:
        count = command("../../../pin -t obj-intel64/inscount0.so -- ./break", e(ans + s)).split(b'\n')[-2]
        record.setdefault(count, []).append(s)
    index = max(record)
    ans += record[index][0]
    print(ans)

print(ans)
