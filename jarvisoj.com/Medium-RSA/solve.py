#!/usr/bin/env python3
from Crypto.PublicKey import RSA

public = RSA.importKey(open('public.pem').read())
private = RSA.importKey(open('private.pem').read())

with open('flag.enc', 'rb') as data:
    flag = data.read().strip()

flag = private.decrypt(flag)
print(flag)
