###photo to get ...
import random
import gmpy2

# Integer Ring
class Z:
    # Z^m_n
    def __init__(self, n, m = 0):
        self.n = n
        self.m = m
    def __contains__(self,item):
        if self.m == 0:
            if (type(item) != type(1) and type(item) != type(1L)):
                return False
            return (item < self.n and item >= 0)
        else:
            if (type(item) != type([1]) or len(item) != self.m):
                return False
            for i in item:
                if not (i < self.n and i >= 0):
                    return False
            return True
# Permutation Group S_p
class S:
    def __init__(self, p):
        self.p = p
    def __contains__(self,item):
        if type(item) != type({1:1}):
            return False
        for k in item.keys():
            if (type(k) != type(1) and type(k) != type(1L)):
                return False
            if (k < 0 or k >= self.p):
                return False
            i = item[k]
            if (i < 0 or i >= self.p):
                return False
        return True

# Matrix Ring M_n(R)
class M:
    # M_n(R) is ring of n by n matrix using element in R
    def __init__(self, n, R):
        self.R = R
        self.n = n

    def __contains__(self,item):
        if (type(item) == type([])):
            if (len(item) == self.n):
                for i in range(self.n):
                    if (type(item[i]) != type([])) and (len(item[i]) != self.n) :
                        return False
                for i in range(self.n):
                    for j in range(self.n):
                        if not (item[i][j] in self.R):
                            return False
                return True
        return False

# A mathematical 2-tuple used to define (a,b) in (A,B)
class Tuple2:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __contains__(self,item):
        if (type(item) == type(())) or (type(item) == type([])):
            if len(item) == 2:
                return (item[0] in self.first) and (item[1] in self.second)
        return False

# Substitution Cipher Mathematical Formulation
# P = C = Z_n
# K = E = S_p
# pi in K, e_pi = pi in E
### D = rho^-1: C -> K
class Substitution:
    # note that check coprime to make sure in S_p
    def generate_key(self):
        n = self.P.n
        while True:
            a = random.randint(2,n-1)
            if gmpy2.gcd(a,n) == 1:
                break
        b = random.randint(0,n-1)
        self.key = {}
        for i in range(256):
            c = self.inc[i]
            self.key[c] = (a * c + b) % n
        assert self.key in self.K
        self.enc = self.key
        assert self.enc in self.E

    # Random in fixed interval
    def generate_inc(self):
        n = self.P.n
        assert n >= 256
        d = {}
        for i in range(256):
            """
            u = (i + 1) * (n - 1) / 256
            l = i * (n - 1) / 256
            d[i] = random.randint(l, u-1)
            """
            d[i] = i * (n - 1) / 255
        return d

    def __init__(self, n):
        assert n >= 256
        self.P = Z(n)
        self.C = Z(n)
        # keyspace is permutation group S_p
        self.K = S(n)
        self.E = S(n)
        # a inclusion map i : F_2^8 -> P
        self.inc = self.generate_inc()

    def encode(self,msg):
        s = []
        for i in msg:
            s.append(self.inc[ord(i)])
        return s

    def encrypt(self,msg):
        if not hasattr(self, "key"):
            self.generate_key()
        s = []
        msg = self.encode(msg)
        # dechunk
        for i in msg:
            assert i in self.P
            s.append(self.enc[i])
        for i in s:
            assert i in self.C
        return s



# Generalized Affine mathematical formulation
# P = C = Z^m_n
# K = {(A,b) where A in M_m(Z_n), b in Z^m_n}
# E = {e_k where e_k(x) = xA + b (mod n) forall x in P}
class Generalized_Affine:
    def dr(self, arr, ori):
        for j in range(len(arr)):
            flag = True
            for i in range(len(arr)):
                if arr[i][j] != ori[i][j]:
                    flag = False
                    break
            if flag:
                return False
        return True

    def generate_key(self):
        m = self.K.second.m
        self.key = [[[0 for _ in range(m)] for _ in range(m)],[0 for _ in range(m)]]
        for i in range(m):
            self.key[0][i][i] = 1
        ori = [[self.key[0][i][j] for j in range(m)] for i in range(m)]
        while not (self.dr(self.key[0],ori)):
            a = random.randint(0,m-1)
            b = random.randint(0,m-1)
            self.key[0][a], self.key[0][b] = self.key[0][b], self.key[0][a]
        assert self.key in self.K
        print(self.key)

    def generate_inc(self):
        n = self.P.n
        assert n >= 256
        d = {} 
        for i in range(256):
            d[i] = i * (n - 1) / 255
        return d

    def __init__(self,n,m):
        self.P = Z(n,m)
        self.C = Z(n,m)
        self.K = Tuple2(M(m,Z(n)),Z(n,m))
        self.inc = self.generate_inc()
    
    def encode(self,msg):
        s = []
        for i in msg:
            s.append(self.inc[ord(i)])
        return s

    def encrypt(self,msg):
        m = self.K.second.m
        if not hasattr(self, "key"):
            self.generate_key()
        msg = self.encode(msg)
        # generate m by m matrix form
        assert len(msg) <= m*m
        p = [[0 for _ in range(m)] for _ in range(m)]
        ii = 0
        for i in range(m):
            for j in range(m):
                if ii >= len(msg):
                    break
                p[i][j] = msg[ii]
                ii += 1
        for i in range(m):        
            assert p[i] in self.P
        s = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            # s[i] = p[i] * A + b
            tmp = [0 for _ in range(m)]
            for j in range(m):
                for k in range(m):
                    tmp[j] += p[i][k] * self.key[0][j][k]
                    tmp[j] %= self.C.n
                tmp[j] += self.key[1][j]
                tmp[j] %= self.C.n
                s[i][j] = tmp[j]
            assert s[i] in self.C
        return s
