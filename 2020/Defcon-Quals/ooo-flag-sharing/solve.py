#!/usr/bin/env python3
import ast
import copy
from pwn import *
from Crypto.Util.number import *

r = remote('ooo-flag-sharing.challenges.ooo', 5000)
#r = remote('127.0.0.1', 20000)

name = 'oalieno'
r.sendlineafter('Username: ', name)

def redeem(secret_id, shares):
    r.sendlineafter('Choice: ', '2')
    r.sendlineafter("Enter the secret's ID: ", secret_id)
    r.sendlineafter("Enter your shares of the secret: ", str(shares))
    r.recvuntil("Your secret is: ")
    secret = r.recvline().strip()
    return int.from_bytes(eval(secret), 'little')

def store_flag():
    r.sendlineafter('Choice: ', '3')
    r.recvuntil("Our secret's ID is: ")
    secret_id = r.recvline().strip().decode()
    r.recvuntil("Your shares are: ")
    shares = ast.literal_eval(r.recvline().strip().decode())
    return secret_id, shares

def redeem_flag(secret_id, shares):
    r.sendlineafter('Choice: ', '4')
    r.sendlineafter("Enter the secret's ID: ", secret_id)
    r.sendlineafter("Enter your shares of the secret: ", str(shares))
    return r.recvline().startswith(b'Congrats')

secret_id, shares = store_flag()
a = redeem(secret_id, [(0, 1)] + [(i, 0) for i in range(1, 5)])

now = 1
while True:
    now += 1
    aa = redeem(secret_id, [(0, now)] + [(i, 0) for i in range(1, 5)])
    P = a * now - aa
    if P > 0:
        print(f'P = {P}')
        break

shares = sorted(shares)

for i in range(1, 100):
    for j in range(i + 1, 100):
        if i in [shares[x][0] for x in range(3)] or j in [shares[x][0] for x in range(3)]:
            continue

        print(i, j)

        fake_shares = sorted([(s[0], 1 if s == shares[-1] else 0) for s in shares] + [(i, 0), (j, 0)])
        a = redeem(secret_id, fake_shares)
        ai = inverse(a, P)

        fail = False
        for k in range(1, 3):
            newshares = copy.deepcopy(shares)
            newshares[2] = (newshares[2][0], (newshares[2][1] + ai * (k << 32)) % P)
            valid = redeem_flag(secret_id, newshares)
            if not valid:
                fail = True
                break

        if not fail:
            L = 0
            H = P >> 32
            while L != H:
                print(((P >> 32) - L).to_bytes(32, 'little'))
                print(((P >> 32) - H).to_bytes(32, 'little'))
                M = (L + H) >> 1
                newshares = copy.deepcopy(shares)
                newshares[2] = (newshares[2][0], (newshares[2][1] + ai * (M << 32)) % P)
                valid = redeem_flag(secret_id, newshares)
                if valid:
                    L = M + 1
                else:
                    H = M
            exit()
