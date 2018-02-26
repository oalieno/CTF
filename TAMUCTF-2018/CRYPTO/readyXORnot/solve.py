#!/usr/bin/env python3
from base64 import b64decode

plain = b"El Psy Congroo"
enc = b64decode("IFhiPhZNYi0KWiUcCls=")
flag = b64decode("I3gDKVh1Lh4EVyMDBFo=")

key = [x ^ y for x, y in zip(plain, enc)]
flag = [x ^ y for x, y in zip(key, flag)]

print(bytes(flag))
