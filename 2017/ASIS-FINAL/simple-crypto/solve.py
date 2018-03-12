#!/usr/bin/python

import random
#from secret import FLAG 

KEY = 'musZTXmxV58UdwiKt8Tp'

def xor_str(x, y):
    if len(x) > len(y):
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x[:len(y)], y)])
    else:
        return ''.join([chr(ord(z) ^ ord(p)) for (z, p) in zip(x, y[:len(x)])])

with open('flag.enc','rb') as data:
    FLAG = data.read()
    flag, key = FLAG, KEY.encode('hex')
    enc = xor_str(key * (len(flag) // len(key)), flag)
    with open('flag','wb') as data:
        data.write(enc.decode('hex'))
