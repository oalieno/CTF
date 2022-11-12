# https://github.com/yinengy/Mersenne-Twister-in-Python/blob/master/MT19937.py

(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253
lower_mask = 0x7FFFFFFF #(1 << r) - 1 // That is, the binary number of r 1's
upper_mask = 0x80000000 #lowest w bits of (not lower_mask)

class MT:
    def __init__(self):
        self.states = [0 for i in range(n)]
        self.index = n + 1

    def seed(self, seed):
        self.states[0] = seed
        for i in range(1, n):
            temp = f * (self.states[i-1] ^ (self.states[i-1] >> (w-2))) + i
            self.states[i] = temp & 0xffffffff
        
    def twist(self):
        for i in range(0, n):
            x = (self.states[i] & upper_mask) + (self.states[(i+1) % n] & lower_mask)
            xA = x >> 1
            if (x % 2) != 0:
                xA = xA ^ a
            self.states[i] = self.states[(i + m) % n] ^ xA

    def rand(self):
        if self.index >= n:
            self.twist()
            self.index = 0

        y = self.states[self.index]
        y = y ^ ((y >> u) & d)
        y = y ^ ((y << s) & b)
        y = y ^ ((y << t) & c)
        y = y ^ (y >> l)

        self.index += 1
        return y & 0xffffffff

    def randint(self, mn, mx):
        num = mx - mn
        return mn + self.rand() % num
