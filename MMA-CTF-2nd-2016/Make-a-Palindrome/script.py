#!/usr/bin/env python

from pwn import *
from itertools import *

def isPalindrome(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

ip = "ppc1.chal.ctf.westerns.tokyo"
port = 31111

s = remote(ip,port)
print s.recv()
print "================"
for i in range(30):
    inp = ""
    while True:
        inp = s.recv()
        if inp.find("Input:") != -1:
            break
    print inp
    inp = inp[inp.find("Input:")+7:inp.find("Answer")].strip()
    L = inp.split()
    num = int(L[0])
    L.remove(L[0])
    for j in permutations(L,num):
        if isPalindrome("".join(j)):
            s.sendline(" ".join(j))
            break

s.interactive()
                  
