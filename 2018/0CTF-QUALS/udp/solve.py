#!/usr/bin/env python3

def wrap(data, s):
    return [data[i:i+s] for i in range(0, len(data), s)]

try:
    with open("data", 'rb') as data:
        memory = data.read()
except:
    print("please use the following command in gdb to generate data")
    print("(gdb) dump memory data 0x6020e0 0x80140e0")
    exit(0)

memory = wrap(memory, 8)
memory = list(map(lambda x: int.from_bytes(x, 'little'), memory))
block = wrap(memory, 4000)

ans1 = 0

for i in range(1, 4000):
    ans1 += block[0][i]

ans2 = 0

for i in range(0, 4000):
    if i == 1: continue
    ans2 += block[i][1]

print("flag{{{:x}}}".format(min(ans1, ans2)))
