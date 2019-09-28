#!/usr/bin/env python3
import intervals
import json
import socket
import struct
import string
from Crypto.Util.number import *

class remote:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.buffer = b''
    def recvuntil(self, text):
        while text not in self.buffer:
            self.buffer += self.s.recv(1024)
        index = self.buffer.find(text) + len(text)
        result, self.buffer = self.buffer[:index], self.buffer[index:]
        return result
    def recvline(self):
        return self.recvuntil(b'\n')
    def recvlines(self, n):
        lines = []
        for _ in range(n):
            lines.append(self.recvline())
        return lines
    def _convert_to_bytes(self, text):
        if type(text) is not bytes:
            text = str(text)
        if type(text) is str:
            text = text.encode()
        return text
    def send(self, text):
        text = self._convert_to_bytes(text)
        self.s.sendall(text)
    def sendline(self, text):
        text = self._convert_to_bytes(text)
        self.send(text + b'\n')
    def sendafter(self, prefix, text):
        self.recvuntil(prefix)
        self.send(text)
    def sendlineafter(self, prefix, text):
        self.recvuntil(prefix)
        self.sendline(text)

e = 0x10001
#c = 32028315366572316530941187471534975579021238700122793819215559206747120150118490538115208229905399038122261293920013020124257186389163654867911967899754432511568776857320594304655042217535057811315461534790485879395513727264354857833013662037825295017832478478693519684813603327210332854320793948700855663229
#n = 105494664357066481298273138238876092390330742404078324408026962658968380291303857669383660190770657673465977042032164073836191436822877521608596568122500853908959638684718610332316825906188233823855819550632166881722171330162713932165700003935670468125777337326977215421773864352895234724039118099959574928191
n = 68133346909851679853551514167372067450301556117993136896713910006794887315754524637730284862547187739221324310423713986344631568547244716990409427299661814772053118718463577650022907717960370743542331968113453359945632747473670114337783168598502452776526082218171506766320993358956312909968983308065362204499
c = 35078803862714649900931310105638561005733600075776532258264774292854937549010662955811774143824657576380496279895664644845588346781641306587084049726267948786329431460251171805911281187157583487823339865316781092424581273663784237723413560331647315854178336300710055884190170187892327090208048086025797978735

#r = remote('likeason-01.pwn.beer', 31337)
r = remote('127.0.0.1', 7777)

def oracle(c, x = 1):
    r.sendline(f'{c} {x}')
    return int(r.recvline())

def intervals_len(inter):
    ans = 0
    for i in inter:
        ans += i.upper - i.lower + 1
    return ans

def valid_char(c):
    return chr(c) in '.-\x00'

def valid(lower, upper):
    l = int(lower).to_bytes(128, 'big')
    u = int(upper).to_bytes(128, 'big')
    for i in range(128):
        if l[i] != u[i]:
            if all([not valid_char(j) for j in range(l[i], u[i] + 1)]):
                return False
            break
        else:
            if not valid_char(l[i]):
                return False
    return True

def prune(inter):
    ans = intervals.empty()
    for i in inter:
        if valid(i.lower, i.upper):
            ans |= i
    return ans

def get_mask(s, mbound):
    mask = intervals.empty()

    kbound = intervals.empty()
    for b in mbound:
        kmin = max(0, ceil((2 ** (s - 1) * b.lower - n) / n))
        kmax = floor((2 ** (s - 1) * b.upper - n / 2) / n)
        kbound |= intervals.closed(kmin, kmax)

    print(f's = {s}')
    print(f'kbound intervals = {intervals_len(kbound)}')

    for b in kbound:
        for k in range(b.lower, b.upper + 1):
            lower = ceil((k + 1 / 2) * n / 2 ** (s - 1))
            upper = floor((k + 1) * n / 2 ** (s - 1))
            if valid(lower, upper):
                mask |= intervals.closed(lower, upper)
    
    mask = prune(mask)
    print(f'mask size = {len(mask)}')
    return mask

s, pp = 0, -1
mbound = intervals.closed(0, n - 1)
while intervals_len(mbound) > 5:
    p = oracle(c * pow(2, s * e, n) % n)
    if pp != -1 and pp != p:
        print(f'mbound size = {len(mbound)}')
        print(f'mbound intervals = {intervals_len(mbound)}')
        mbound &= get_mask(s, mbound)
        mbound = prune(mbound)
    s, pp = s + 1, p

print(mbound)
