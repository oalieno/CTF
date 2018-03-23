#!/usr/bin/env sage
import socket

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
    def send(self, text):
        self.s.sendall(text)
    def sendline(self, text):
        self.s.sendall(text + '\n')

def gcd(a, b):
    return a.monic() if b == 0 else gcd(b, a % b)

r = remote('127.0.0.1', 20000)

for i in range(10):
    n = int(r.recvline())
    c2 = int(r.recvline())
    c1 = int(r.recvline())
    
    F.<x> = PolynomialRing(Zmod(n))
    
    g1 = (x + 1) ^ 3 - c1
    g2 = x ^ 3 - c2

    m = -gcd(g1, g2).coefficients()[0]
    if i < 9: r.sendline(str(m))
    else: print hex(int(m)).strip('0x').strip('L').decode('hex')
    print r.recvline()
