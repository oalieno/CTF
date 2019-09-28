#!/usr/bin/env python3
import intervals
import json
import socket
import struct
import string
from Crypto.Util.number import *
import sys   

sys.setrecursionlimit(10000)

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
#n = 105494664357066481298273138238876092390330742404078324408026962658968380291303857669383660190770657673465977042032164073836191436822877521608596568122500853908959638684718610332316825906188233823855819550632166881722171330162713932165700003935670468125777337326977215421773864352895234724039118099959574928191
#c = 32028315366572316530941187471534975579021238700122793819215559206747120150118490538115208229905399038122261293920013020124257186389163654867911967899754432511568776857320594304655042217535057811315461534790485879395513727264354857833013662037825295017832478478693519684813603327210332854320793948700855663229
n = 68133346909851679853551514167372067450301556117993136896713910006794887315754524637730284862547187739221324310423713986344631568547244716990409427299661814772053118718463577650022907717960370743542331968113453359945632747473670114337783168598502452776526082218171506766320993358956312909968983308065362204499
c = 30114219239892667628290486736731427494873556258670848619310327407555453255306715021419934979916840285122928282506417561332451273155435522830679498343641802083420365324068696406435962456213173734561060791206969088044307942904150014014900798465442902164285751234210102609882759019190172878817794058147653170084

#r = remote('likeason-01.pwn.beer', 31337)
r = remote('127.0.0.1', 7777)

def oracle(c, x = 1):
    r.sendline(f'{c} {x}')
    return int(r.recvline())

def valid_char(c):
    return chr(c) in '.-'

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

def solve(s, lower, upper):
    #print(f'diff = {upper - lower}')
    if not valid(lower, upper):
        return
    if s == len(oracles) or lower >= upper:
        print(f'lower = {lower}')
        print(f'upper = {upper}')
        print(f'[+] found')
        return
    if oracles[s - 1] != oracles[s]:
        solve(s + 1, ceil((lower + upper) / 2), upper)
    else:
        solve(s + 1, ceil((lower + upper) / 2), upper)
        solve(s + 1, lower, floor((lower + upper) / 2))

oracles = [oracle(c * pow(2, s * e, n) % n) for s in range(1024)]
print('[+] oracles retrieved')
solve(1, 0, n - 1)
