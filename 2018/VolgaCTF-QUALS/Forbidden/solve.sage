#!/usr/bin/env sage

import textwrap

poly = x ^ 128 + x ^ 7 + x ^ 2 + x + 1
F.<x> = GF(2 ^ 128, modulus = poly)
FF.<y> = PolynomialRing(F)

def s2n(s):
    if not len(s):
        return 0
    return int(s.encode("hex"), 16)

def tobin(x, n):
    x = Integer(x)
    nbits = x.nbits()
    assert nbits <= n
    return [0] * (n - nbits) + x.bits()[::-1]

def frombin(v):
    return int("".join(map(str, v)), 2 )

def toF(x):
    # Little endian, so need bit reverse
    x = frombin(tobin(x, 128)[::-1])
    return F.fetch_int(x)

def fromF(x):
    # Little endian, so need bit reverse
    x = x.integer_representation()
    x = frombin(tobin(x, 128)[::-1])
    return x

C1 = textwrap.wrap('1761e540522379aab5ef05eabc98516fa47ae0c586026e9955fd551fe5b6ec37e636d9fd389285f3'.decode('hex').ljust(48, '\x00'), 16)
C2 = textwrap.wrap('1761e540522365aab1e644ed87bb516fa47ae0d9860667d852c6761fe5b6ec37e637c7fc389285f3'.decode('hex').ljust(48, '\x00'), 16)
C1 = map(lambda x: toF(s2n(x)), C1)
C2 = map(lambda x: toF(s2n(x)), C2)

A1 = "John Doe".ljust(16, '\x00')
A2 = "VolgaCTF".ljust(16, '\x00')
A1 = toF(s2n(A1))
A2 = toF(s2n(A2))

L = '0000000000000008'.decode('hex') + '0000000000000028'.decode('hex')
L = toF(s2n(L))

T1 = toF(0x0674d6e42069a10f18375fc8876aa04d)
T2 = toF(0xcf61b77c044a8fb1566352bd5dd2f69f)

JEDI = (A1 + A2) * (y ** 5) + (C1[0] + C2[0]) * (y ** 4) + (C1[1] + C2[1]) * (y ** 3) + (C1[2] + C2[2]) * (y ** 2) + T1 + T2

H = JEDI.roots()[0][0]

C3 = textwrap.wrap('1761e540522379aab5ef05eabc98516fa47ae0d9860667d852c6761fe5b6ec37e646a581389285f3'.decode('hex').ljust(48, '\x00'), 16)
C3 = map(lambda x: toF(s2n(x)), C3)

A3 = A1

Y = A1 * (H ** 5) + C1[0] * (H ** 4) + C1[1] * (H ** 3) + C1[2] * (H ** 2) + L * H + T1

T3 = A3 * (H ** 5) + C3[0] * (H ** 4) + C3[1] * (H ** 3) + C3[2] * (H ** 2) + L * H + Y

print hex(fromF(T3))
