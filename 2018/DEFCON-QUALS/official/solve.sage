#!/usr/bin/env sage
import struct
import socket
import hashlib

from sage.modules.free_module_integer import IntegerLattice

p = 145774370140705743619288815016506936272601276321515267981294709325646228235350799641396853482542510455702593145365689674776551326526283561120782331775753481248764911686023024656237178221049671999816376444280423000085773391715885524862881877222848088840644737895543531766907185051846802894682811137086905085419
q = 739904609682520586736011252451716180456601329519

Rp = Integers(p)
Rq = Integers(q)

y = Rp(128135682856750887590860168748824430714190353609169438003724812869569788088376999153566856518649548751808974042861313871720093923966663967385639616771013994922707548355367088446112595542221209828926608117506259743026809879227606814076195362151108590706375917914576011875357384956337974597411261584032533163073)
g = Rp(52865703933600072480340150084328845769706702669400766904467248075164948743170867377627486621900744105555465052783047541675343643777082719270261354312243195450389581166294097053506337884439282134405767273312076933070573084676163659758350542617531330447790290695414443063102502247168199735083467132847036144443)

class remote:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.buffer = ""
    def recvuntil(self, text):
        while text not in self.buffer:
            self.buffer += self.s.recv(1024)
        index = self.buffer.find(text) + len(text)
        ans, self.buffer = self.buffer[:index], self.buffer[index:]
        return ans
    def recvline(self):
        return self.recvuntil('\n')
    def recvlines(self, n):
        lines = []
        for _ in range(n):
            lines.append(self.recvline())
        return lines
    def send(self, text):
        self.s.sendall(text)
    def sendline(self, text):
        self.s.sendall(text + '\n')
    def sendafter(self, prefix, text):
        self.recvuntil(prefix)
        self.send(text)
    def sendlineafter(self, prefix, text):
        self.recvuntil(prefix)
        self.sendline(text)

def proof_of_work(prefix, n):
    guess = 0
    while True:
        result = hashlib.sha256(prefix + struct.pack('<Q', guess)).hexdigest()
        if int(result, 16) % (2 ** n) == 0:
            return guess
        guess += 1

r = remote("3aef2bbc.quals2018.oooverflow.io", 31337)

# proof of work
r.recvline()
prefix = r.recvline().replace(b'Challenge: ', b'').strip()
n = int(r.recvline().replace(b'n: ', b'').strip())
r.sendlineafter('Solution: \n', str(proof_of_work(prefix, n)))

r.recvlines(4)

m = 'ls'.ljust(256, 'a')
h = int(hashlib.sha1(m).hexdigest(), 16)

rs = []
ss = []
L = 100

for i in range(L):
    r.sendlineafter('> ', 'S')
    r.sendafter('cmd:', m)
    rs.append(int(r.recvline().replace(b'r: ', b'').strip()))
    ss.append(int(r.recvline().replace(b's: ', b'').strip()))

sT = 1
sU = 1

mat = matrix(ZZ, L + 2, L + 2)
for i in range(L + 2):
    column = [0] * L
    if i < L:
        column[i] = q
        t = rs[i] * inverse_mod(2 ** 8 * ss[i], q) % q
        u = -h * inverse_mod(2 ** 8 * ss[i], q) % q
        column += [t, u]
    elif i == L:
        column += [sT, 0]
    else:
        column += [0, sU]
    mat.set_column(i, column)

mat = mat.LLL()

for i, v in enumerate(mat):
    if v[-1] == sU:
        x = Rq(-v[-2] / sT)
        break

print 'x: {}'.format(x)

h = int(hashlib.sha1('cat').hexdigest(), 16)
k = Rq(1234567)
r = Rq(g ^ k)
s = (h + x * r) / k

print 'r : {}'.format(r)
print 's : {}'.format(s)
