#!/usr/bin/env python3
from Crypto.Cipher import DES

def decode(text):
    h = ''
    for i in range(0, len(text), 8):
        c = int(text[i:i+8]) - 9133337
        if c < 10:
            h += str(c)
        elif c > 10:
            h += 'abcdef'[c - 11]
        else:
            print('WTF')
            exit()
    return bytes.fromhex(bytes.fromhex(h).decode())

cipher = decode(open('./FLAG.enc').read())

IV = b'13371337'

keys = list(map(bytes.fromhex, open('weaks').read().strip().split('\n')))

for k1 in keys:
    for k2 in keys:
        des1 = DES.new(k1, DES.MODE_OFB, IV)
        des2 = DES.new(k2, DES.MODE_OFB, IV)
        plain = des1.decrypt(des2.decrypt(cipher))
        if b'flag' in plain:
            print(k1)
            print(k2)
            print(plain)


