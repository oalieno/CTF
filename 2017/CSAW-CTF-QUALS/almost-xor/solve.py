#!/usr/bin/env python3
import string

def wrap(text, n):
    return [text[i : i + n]for i in range(0, len(text), n)]

def magic(x, n):
    ans = []
    mask = (1 << n) - 1
    for i in range(8):
        ans.append(x & mask)
        x >>= n
    ans.reverse()
    return ans

def rmagic(x, n):
    ans = 0
    for xx in x:
        ans = ans * (1 << n) + xx
    return ans

def xor(x, y, n, f):
    x = int.from_bytes(x, 'big')
    y = int.from_bytes(y, 'big')
    xx = magic(x, n)
    yy = magic(y, n)
    ans = [f(xxx, yyy, n) for xxx, yyy in zip(xx, yy)]
    ans = rmagic(ans, n)
    return ans.to_bytes(n, 'big')

def plus(x, y, n):
    return xor(x, y, n, lambda x, y, n: (x + y) % (1 << n))

def minus(x, y, n):
    return xor(x, y, n, lambda x, y, n: (x - y + (1 << n)) % (1 << n))

cipher = "809fdd88dafa96e3ee60c8f179f2d88990ef4fe3e252ccf462deae51872673dcd34cc9f55380cb86951b8be3d8429839"
cipher = int(cipher, 16)
cipher = cipher.to_bytes(48, 'big')

'''
n = 2
c = wrap(cipher, n)
print(minus(c[0], b'fl', n))
print(minus(c[1], b'ag', n))

n = 3
c = wrap(cipher, n)
print(minus(c[0], b'fla', n))

n = 4
c = wrap(cipher, n)
print(minus(c[0], b'flag', n))
'''

n = 3
c = wrap(cipher, n)
for guess in range(256):
    key = [0, 0]
    key[0] = minus(c[0], b'fla', n)
    key[1] = minus(c[1], b'g{' + bytes([guess]), n)
    ans = b""
    for i in range(0, len(c), 2):
        ans += minus(c[i], key[0], n)
        ans += minus(c[i+1], key[1], n)
    if all(map(lambda x: x in map(ord, string.printable), ans)) and ans.endswith(b'}'):
        print(ans)

