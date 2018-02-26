#!/usr/bin/env python3
import string
from Crypto.Util.number import inverse
from functools import reduce
from sqrt import modular_sqrt
from cipher import n, e, c

def chinese_remainder(a, n):
    ans = 0
    prod = reduce(lambda a, b: a * b, n)
 
    for a_i, n_i in zip(a, n):
        p = prod // n_i
        ans += a_i * inverse(p, n_i) * p
    return ans % prod

def power2roots(a, k):
    if k == 0:
        yield a
        return
    for i in power2roots(a, k-1):
        s1 = modular_sqrt(i, p)
        s2 = modular_sqrt(i, q)
        if s1 and s2:
            yield chinese_remainder([s1, s2], [p, q])
            yield chinese_remainder([p-s1, s2], [p, q])
            yield chinese_remainder([s1, q-s2], [p, q])
            yield chinese_remainder([p-s1, q-s2], [p, q])

p = 123722643358410276082662590855480232574295213977
q = 164184701914508585475304431352949988726937945291

d = inverse(e, (p - 1) * (q - 1))
_m = pow(c, d, n) # calculate m ** 16 % n

for m in power2roots(_m, 4):
    flag = b"hitcon{" + b'\x00' * 42 + b'}'
    flag = int.from_bytes(flag, byteorder = 'big')
    flag += (m % n - flag % n + n) % n
    m = flag
    while m % 256 != ord('}'):
        m += n
    increment = n * 256
    upper = int.from_bytes(b"hitcon{" + b'\x7f' + b'\x00' * 42, byteorder = 'big')
    while m < upper:
        text = m.to_bytes(50, byteorder = 'big')
        if text.startswith(b'hitcon{') and text.endswith(b'}') and all([32 <= t <= 126 for t in text]):
            print(text)
            exit(0)
        m += increment
