#!/usr/bin/env python3

magic = "_'qwertyuiop{}asdfghjklzxcvbnm|"
cipher = "zmu}jnd{o{f_ndo{{_hz_{ga"

for _ in range(3):
    ncipher = ""
    for c in cipher:
        i = magic.index(c)
        ncipher += chr(i + 0x5f)
    cipher = ncipher

print(cipher)
