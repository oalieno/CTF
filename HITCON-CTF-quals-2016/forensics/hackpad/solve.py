#!/usr/bin/env python3

import textwrap

with open("message") as data:
    message = data.read().strip().split('\n')

cipher = message[0].lstrip("msg=")
print("cipher text :", cipher)
cipher = textwrap.wrap(cipher, 32)
message = message[2+256+1:]

now = 1
ans = ""

for index, line in enumerate(message):
    if line.startswith("md5(decrypt(msg)) = "):
        AB = message[index - 1].lstrip("msg=")[:64]
        A, B = AB[0:32], AB[32:64]
        if A[:2] == '00': continue
        try:
            ans += bytes.fromhex(hex(int(A, 16) ^ int("10" * 0x10, 16) ^ int(cipher[now - 1], 16))[2:]).decode("utf-8")
        except:
            continue
        now += 1

print("decrypted text :", ans)
