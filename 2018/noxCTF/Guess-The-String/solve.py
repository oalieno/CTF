#!/usr/bin/env python3

primes = []

for i in range(2, 256):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)

s = [0] * 11

s[0] = 47
s[1] = 74

assert(s[0] * s[1] == 3478)

s[2] = s[0] ^ s[1] ^ 49

for i in range(s[2] + 1, 256):
    if i * i % 256 == s[2] * s[2] % 256:
        s[3] = i
        break

def get456():
    for i in primes:
        for j in primes:
            if i > 32 and j > 32 and (i ^ j) % 256 == 126:
                if j - 42 in primes and 2 * j < 256:
                    return (i, j, 2 * (j - 42))

s[4], s[5], s[6] = get456()

for i in range(48, 58):
    if 4 * (i >> 2) == i:
        s[7] = i
        break

s[8] = 0x12 ^ s[7]

s[9] = 2 * s[8]

s[10] = 0x7a

for c in s:
    assert(c > 32)

print(''.join(map(chr, s)))
