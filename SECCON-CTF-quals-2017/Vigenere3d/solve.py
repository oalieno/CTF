#!/usr/bin/env python3

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
cipher = list(map(lambda x: s.index(x), "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"))
plain  = list(map(lambda x: s.index(x) if x != '*' else -1, "SECCON{**************************}"))
key = [-1] * 14

for i, x in enumerate(plain):
    if plain[i] == -1:
        if key[i % 14] != -1:
            plain[i] = (cipher[i] + key[i % 14]) % len(s)
    else:
        k = (plain[i] - cipher[i] + len(s)) % len(s)
        key[i % 14] = k
        key[14 - 1 - (i % 14)] = k

print(''.join(list(map(lambda x: s[x], plain))))
