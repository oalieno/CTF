#!/usr/bin/env python3
from Crypto.Util.number import *
from tqdm import tqdm

class Solver:
    def __init__(self, x, n):
        self.x = x
        self.n = n
        self.pq = [(0, 0)]

    def add(self, b, p, q):
        if p * q <= n and (p | (b - 1)) * (q | (b - 1)) >= n:
            self.pq.append((p, q))

    def solve(self):
        for shift in tqdm(range(4095, -1, -1)):
            b = 1 << shift
            pq, self.pq = self.pq, []
            for p, q in pq:
                if self.x & b:
                    self.add(b, p | b, q)
                    self.add(b, p, q | b)
                else:
                    self.add(b, p, q)
                    self.add(b, p | b, q | b)
        print(self.pq)
        return self.pq[0]

exec(open('flag.enc').read().lower())
solver = Solver(x, n)
p, q = solver.solve()
r = (p - 1) * (q - 1)
d = inverse(e, r)
m = pow(c, d, n)
print(long_to_bytes(m))
