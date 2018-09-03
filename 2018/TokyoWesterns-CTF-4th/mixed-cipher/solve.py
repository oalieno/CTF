#!/usr/bin/env python3
import mt19937predictor
from pwn import *
from Crypto.Util.number import *
from Crypto.Cipher import AES

random_counts = 0

def encrypt(r, data):
    global random_counts
    random_counts += 1
    r.recvlines(6)
    r.sendline('1')
    r.sendlineafter('input plain text: ', data)
    return [bytes.fromhex(r.recvline().strip().split(b': ')[1].decode()), bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())]

def decrypt(r, data):
    r.recvlines(6)
    r.sendline('2')
    r.sendlineafter('input hexencoded cipher text: ', data.hex())
    r.recvline()
    return bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())

def get_flag(r):
    r.recvlines(6)
    r.sendline('3')
    r.recvlines(2)
    return bytes.fromhex(r.recvline().strip().decode())

def get_key(r):
    r.recvlines(6)
    r.sendline('4')
    r.recvline()
    return bytes.fromhex(r.recvline().strip().decode())

r = remote('crypto.chal.ctf.westerns.tokyo', 5643)

'''
predict random.getrandbits
'''
predictor = mt19937predictor.MT19937Predictor()

for i in range(624 // 4):
    data = encrypt(r, 'A')[1][:16]
    predictor.setrandbits(bytes_to_long(data), 128)

random_counts = 0

'''
recover n
'''
A = encrypt(r, 'A')[0]
B = encrypt(r, 'B')[0]
C = encrypt(r, 'C')[0]

e = 65537

def magic(m, c):
    return pow(bytes_to_long(m), e) - bytes_to_long(c)

n = GCD(GCD(magic(b'A', A), magic(b'B', B)), magic(b'C', C))

print('n =', n)

'''
RSA LSB oracle
'''
key = get_key(r)

def oracle(x):
    result = decrypt(r, long_to_bytes(x))
    return result[-1] % 2

L = 0
H = n
t = pow(2, e, n)
c = bytes_to_long(key)
for _ in range(n.bit_length() + 10):
    c = (t * c) % n
    if oracle(c) == 0:
        H = (L + H) // 2
    else:
        L = (L + H) // 2

key = L

for i in range(random_counts):
    predictor.getrandbits(128)

enc = get_flag(r)[16:]

iv = long_to_bytes(predictor.getrandbits(128))

for k in range(key, key + 30):
    aes = AES.new(long_to_bytes(k), AES.MODE_CBC, iv)
    f = aes.decrypt(enc)
    if b'ora' in f:
        flag = f
        key = k
        break

print('key =', key)
print('flag =', flag)


