from Crypto.Util.number import *
from gmpy2 import *
from secret import flag,magic_value,p1,q1,p2,q2,e1,e2,ee

Flag = bytes_to_long(flag)

salt = magic_value^Flag
n1 = p1*q1
n2 = p2*q2


c1 = pow(magic_value,e1,n1)
c2 = pow(magic_value,e2,n2)

p = getPrime(1024)
q = getPrime(1024)

ed = invert(ee,(p-1)*(q-1))

c3 = pow(p1*p2,ed,p*q)

enc = pow(salt,ee,p*q)

f = open('data.txt','w')

f.write(str((c1,c2,c3,n1,n2,e1,e2,enc,p*q,ed)))
