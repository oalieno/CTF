from Crypto.Util.number import *
from gmpy2 import * 
import random
from secret import flag
from hashlib import sha256

def Hash(data,q):
    return int(sha256(str(data)).hexdigest(),16) % q 

def GenerateKeys(size):
    q = getPrime(size)
    F.<x> = GF(q)
    g1 = g2 = F.random_element()

    rand = lambda: random.randint(133700000,2333799999)
    
    x1,x2,y1,y2,z = [f() for f in [rand]*5]
    
    c = g1^x1 * g2^x2
    d = g1^y1 * g2^y2
    h = g2^z

    return (F,q,g1,g2,c,d,h),(x1,x2,y1,y2,z)

def encrypt(m,pubkey):
    (F,q,g1,g2,c,d,h) = pubkey
    k = int(F.random_element())
    u1,u2 = g1^k, g2^k
    e = m * h^k
    
    a = Hash((u1,u2,e), q)
    v = c^k * d^(k*a)
    
    return (u1,u2,e,v)


pubkey, privkey = GenerateKeys(256L)
open('cipher.text','wb').write(str(encrypt(flag, pubkey)))
open('pub.key','wb').write(str(pubkey))
