#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

public = RSA.importKey(open('public.pem').read())

n = public.n
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239

with open('flag.enc', 'rb') as data:
    flag = data.read().strip()

flag = int.from_bytes(flag, byteorder = 'big')

mp = pow(flag, (p + 1) // 4, p)
mq = pow(flag, (q + 1) // 4, q)

yp = inverse(p, q)
yq = inverse(q, p)

r = (yp * p * mq + yq * q * mp) % n
_r = -r % n
s = (yp * p * mq - yq * q * mp) % n
_s = -s % n

print(r.to_bytes(32, byteorder = 'big'))
print(_r.to_bytes(32, byteorder = 'big'))
print(s.to_bytes(32, byteorder = 'big'))
print(_s.to_bytes(32, byteorder = 'big'))
