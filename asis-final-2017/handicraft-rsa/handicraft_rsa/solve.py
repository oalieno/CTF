#!/usr/bin/env python
from __future__ import print_function

import sys

from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from base64 import b64decode

message = "eER0JNIcZYx/t+7lnRvv8s8zyMw8dYspZlne0MQUatQNcnDL/wnHtkAoNdCalQkpcbnZeAz4qeMX5GBmsO+BXyAKDueMA4uy3fw2k/dqFSsZFiB7I9M0oEkqUja52IMpkGDJ2eXGj9WHe4mqkniIayS42o4p9b0Qlz754qqRgkuaKzPWkZPKynULAtFXF39zm6dPI/jUA2BEo5WBoPzsCzwRmdr6QmJXTsau5BAQC5qdIkmCNq7+NLY1fjOmSEF/W+mdQvcwYPbe2zezroCiLiPNZnoABfmPbWAcASVU6M0YxvnXsh2YjkyLFf4cJSgroM3Aw4fVz3PPSsAQyCFKBA=="

origin = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq+m7iHurBa9G8ujEiTpZ
71aHOVNhQXpd6jCQNhwMN3hD6JHkv0HSxmJwfGe0EnXDtjRraWmS6OYzT4+LSrXs
z9IkWGzRlJ4lC7WHS8D3NWIWYHCP4TRt2N0TlWXWm9nFCrEXqQ3IWgYQpQvKzsds
etnIZJL1tf1wQzGE6rbkbvURlUBbzBSuidkmi0kY5Qxp2Jfb6OUI647zx2dPxJpD
ffSCNffVIDUYOvrgYxIhs5HmCF3XECC3VfaKtRceL5JM8R0qz5nVU2Ns8hPvSVP+
7/i7G447cjW151si0joB7RpBplu44Vk8TXXDAk0JZdW6KwJn7ITaX04AAAAAAAAA
AQIDAQAB
-----END PUBLIC KEY-----'''

def gcd(x,y):
    while y != 0:
        _x,_y = y,x%y
        x,y = _x,_y
    return x

def factor(n):
    a = 2
    b = 2
    while True:
        sys.stdout.flush()
        print("\rnow : {}".format(b),end='')
        a = pow(a,b,n) 
        d = gcd(a-1,n)
        if 1 < d < n: return d
        b += 1

def decrypt(n, p, q):
    global message
    e = 65537
    d = inverse(e, (p-1)*(q-1))

    key = RSA.construct((long(n), long(e), long(d), long(p), long(q)))
    message = b64decode(message)    

    for _ in xrange(20):
        enc = key.decrypt(message)
        message = enc
        
    return message


key = RSA.importKey(origin)
n = key.n

p = factor(n)
q = n/p
flag = decrypt(n,p,q)
print("")
print(repr(flag))
