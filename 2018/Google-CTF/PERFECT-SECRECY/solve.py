#!/usr/bin/env python3
from pwn import *
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

context.log_level = 'ERROR'

def oracle(x):
    while True:
        r = remote("perfect-secrecy.ctfcompetition.com", 1337)
        r.send(b'\x00')
        r.send(b'\x01')
        r.send((x).to_bytes(1024 // 8, 'big'))
        result = r.recvn(100, 100)
        r.close()
        if abs(result.count(b'\x00') - result.count(b'\x01')) < 20:
            print('shit happend : {}'.format(abs(result.count(b'\x00') - result.count(b'\x01'))))
            continue
        if result.count(b'\x00') > result.count(b'\x01'):
            return 0
        else:
            return 1

print("oracle test 0 :", oracle(0))
print("oracle test 1 :", oracle(1))

rsa = RSA.importKey(open('./key_pub.pem').read())
n = rsa.n
e = rsa.e

c = bytes_to_long(open('./flag.txt', 'rb').read())

L = 0
H = n
two = pow(2, e, n)
count = 0
while count < 1024:
    print('count =', count)
    print('L =', L)
    print('H =', H)
    c = (two * c) % n
    if oracle(c) == 0:
        H = (L + H) // 2
    else:
        L = (L + H) // 2
    count += 1

print(long_to_bytes(L))
print(long_to_bytes(H))
