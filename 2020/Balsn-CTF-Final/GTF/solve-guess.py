#!/usr/bin/env python3
import os
import json
import random
import string
import requests
from Crypto.Cipher import AES

url = 'http://35.236.157.216:11337'
#url = 'http://127.0.0.1:11337'

r = requests.get(f'{url}/status')
status = json.loads(r.text)
enc = bytes.fromhex(status['flag'])

print(f'[INFO] {len(enc) // 16 - 1} blocks to scan')

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

counter = [0]

def oracle(c):
    counter[0] += 1
    r = requests.get(f'{url}/compress', params = {'x': c.hex()})
    return len(r.content)

def grow(s):
    for i in range(256):
        if i not in s:
            s.append(i)
    return s

seq = b'GTF{}' + bytes([c for c in range(0xe0, 0xef)]) + string.digits.encode() + string.ascii_letters.encode() + b' _-.!?:'
seq = list(seq)
seq = grow(seq)

seq_weird = bytes([c for c in range(0xe0, 0xef)]) + bytes([c for c in range(0xa0, 0xbf)]) + bytes([c for c in range(0x80, 0x9f)]) + b'GTF{}' + string.digits.encode() + string.ascii_letters.encode() + b' _-.!?:'
seq_weird = list(seq_weird)
seq_weird = grow(seq_weird)

flag = b''
buf = b''
for k in range(16 + len(flag), len(enc), 16):
    counter_start = counter[0]
    ans = b''

    iv, block = bytearray(enc[k-16:k]), enc[k:k+16]
    
    base = 193
    def getMask():
        mask = bytearray(os.urandom(16))
        while oracle(xor(mask, iv) + block) != base:
            mask = bytearray(os.urandom(16))
        return mask
    masknum = 2
    masks = [getMask() for _ in range(masknum)]

    enable = True
    for i in range(16):
        print(f'counter = {counter[0]}')
        guessed = []

        if enable and buf:
            j, buf = buf[0], buf[1:]
            for m in range(masknum):
                masks[m][i] = j % 256
                l = oracle(xor(masks[m], iv) + block)
                if l >= base:
                    break
            else:
                base = l
                ans += bytes([j % 256])
                print(ans)
                try:
                    print((flag + ans).decode())
                except UnicodeDecodeError:
                    print('[-] Unicode Decode Error, please try again')
                continue
            guessed.append(j)
            buf = b''

        if enable:
            success = False
            while True:
                try:
                    guess = input('guess: ')
                except UnicodeDecodeError:
                    continue
                # command
                if guess == 'bb':
                    break
                if guess == 'ss':
                    r = requests.get(f'{url}/submit', params={'x': (flag + ans).decode()})
                    print(r.text)
                    continue
                if guess == 'cc':
                    enable = False
                    break
                if guess.startswith('0x'):
                    guess = chr(int(guess, 16))
                guess = guess.encode()
                if len(guess) > 1:
                    buf = guess[1:]
                j = guess[0]
                guessed.append(j)
                for m in range(masknum):
                    masks[m][i] = j % 256
                    l = oracle(xor(masks[m], iv) + block)
                    if l >= base:
                        break
                else:
                    base = l
                    ans += bytes([j % 256])
                    print(ans)
                    try:
                        print((flag + ans).decode())
                    except UnicodeDecodeError:
                        pass
                    success = True
                    break
            if success:
                continue

        sss = seq
        if sum([c > 200 for c in flag + ans]) > 1:
            sss = seq_weird
        for j in sss:
            if j in guessed:
                continue
            for m in range(masknum):
                masks[m][i] = j % 256
                l = oracle(xor(masks[m], iv) + block)
                if l >= base:
                    break
            else:
                base = l
                ans += bytes([j % 256])
                print(ans)
                try:
                    print((flag + ans).decode())
                except UnicodeDecodeError:
                    pass
                break
        else:
            print('[Error] False positive case ( try again )')
            print(f'Current flag : {flag + ans}')
            exit()
        if ans.endswith(b'\x00'):
            break

    flag += ans
    print(f'[INFO] block {k // 16 - 1} scan complete ({counter[0] - counter_start} requests)')

print(f'[INFO] send total {counter[0]} requests')

flag = flag.rstrip(b'\x00')
print('----- flag -----')
print(flag)
print(flag.decode())
print('----- server result -----')
r = requests.get(f'{url}/submit', params={'x': flag.decode()})
print(r.text)
