#!/usr/bin/env python3
from pwn import *
from hashlib import sha256
from Crypto.Util.number import inverse

context.log_level = 'ERROR'

def proof_of_work(condition):
    prefix = condition[8:14]
    hprefix = condition[45:50]
    guess = 0
    while True:
        if sha256(prefix + str(guess).encode('ascii')).hexdigest().startswith(hprefix.decode('ascii')):
            return str(guess)
        guess += 1

def go(padding):
    r = remote("47.75.39.249", 23333)
    condition = r.recvlines(2)[1]
    r.sendline(proof_of_work(condition))
    r.sendline('2')
    r.sendline(padding)
    r.recvuntil('Your Ciphertext is: ')
    C = int(r.recvline().strip())
    r.close()
    return C

N = 21727106551797231400330796721401157037131178503238742210927927256416073956351568958100038047053002307191569558524956627892618119799679572039939819410371609015002302388267502253326720505214690802942662248282638776986759094777991439524946955458393011802700815763494042802326575866088840712980094975335414387283865492939790773300256234946983831571957038601270911425008907130353723909371646714722730577923843205527739734035515152341673364211058969041089741946974118237091455770042750971424415176552479618605177552145594339271192853653120859740022742221562438237923294609436512995857399568803043924319953346241964071252941

C1 = go('jedi')
C2 = go('master')

X1 = int(sha256(b'jedi').hexdigest(), 16)
X2 = int(sha256(b'master').hexdigest(), 16)

B = (X1 - X2) % N

F = (B * (C1 + 2 * C2 - B ** 3)) % N
G = (C1 - C2 + 2 * (B ** 3)) % N

IG = inverse(G, N)

M = F * IG % N

M = (M - X2) % N

print(M.to_bytes(102, 'big'))
