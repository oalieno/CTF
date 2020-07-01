#!/usr/bin/env python3
import requests
from base64 import *

import logging

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def oracle(c):
    r = requests.post('https://turtowl.ais3.org/?action=login', headers = {
        'Cookie': 'PHPSESSID=273ef627a44b5089c668c8b2f16b791e',
        'Content-Type': 'application/x-www-form-urlencoded'
    }, data = {
        'csrf_token': b64encode(c).decode(),
        'username': 'a',
        'password': 'a',
        'submit': 'Login'
    })
    if 'decryption' in r.text:
        return False
    else:
        return True

enc = b64decode('s9bBxdpd09FOP1egpTEmeFSqqSUbpkqMizx1VXWVlSOuxukhDXIIPacXzQwNu5hpb86QKtGPi2cmP0tUBxQuxw==')

flag = b''
for i in range(48, len(enc), 16):
    ans = b''
    iv, block = enc[i-16:i], enc[i:i+16]
    for j in range(16):
        for k in range(256):
            if oracle(iv[:16 - 1 - j] + bytes([k]) + xor(bytes([j + 1] * j), xor(iv[-j:], ans)) + block):
                ans = bytes([iv[16 - 1 - j] ^ k ^ (j + 1)]) + ans
                print(ans)
                break
    flag += ans

print(flag)
