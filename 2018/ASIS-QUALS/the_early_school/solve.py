#!/usr/bin/env python3

with open("FLAG.enc", 'rb') as data:
    cipher = data.read()

cipher = int.from_bytes(cipher, 'big')
cipher = bin(cipher)[2:]

for i in range(20):
    jedi = ""
    for i in range(0, len(cipher), 3):
        if len(cipher[i:i+3]) == 3: jedi += cipher[i:i+2]
        else: jedi += cipher[i:i+1]
    cipher = jedi
    try:
        print(int(cipher, 2).to_bytes(100, 'big'))
    except:
        continue
