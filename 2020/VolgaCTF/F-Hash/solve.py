#!/usr/bin/env python3

table = [0]
for i in range(26):
    table += [i * 10 + 1 + (0xf6 << 120)] * 10

def bitcountsum(a, b):
    a %= (1 << 64)
    b %= (1 << 64)
    return bin(a).count('1') + bin(b).count('1')

def calc(a, b, depth = 256):
    ans = [0]
    ans.append((bitcountsum(a, b), 0, 0))
    ans.append((bitcountsum(a ^ 1, b), 0, 1))

    for i in range(3, depth + 1):
        v15, v16 = ans[i - 1], ans[i - 2]
        v13 = ((v15[0] + v15[1] * (1 << 64)) + (v16[0] + v16[1] * (1 << 64)) + bitcountsum((v15[2] + v16[2]) ^ a, b)) % (1 << 128)
        v14 = table[i]
        while True:
            if (v14 >> 64) > (v13 >> 64):
                break
            if (v14 >> 64) == (v13 >> 64):
                if v14 % (1 << 64) >= v13 % (1 << 64):
                    break
            k = max(1, (v13 >> 64) // (v14 >> 64))
            v13 = (v13 - k * v14) % (1 << 128)
        ans.append((v13 % (1 << 64), (v13 >> 64), (v15[2] + v16[2]) % (1 << 64)))
    return ans

al = [0x6369757120656854, 0x706d756a20786f66, 0x20797a616c206568, 0]
bl = [0x206e776f7262206b, 0x74207265766f2073, 0x80676f64, 0x2b]

for a, b in zip(al, bl):
    print(list(map(hex, calc(a, b)[256])))
