#!/usr/bin/env python3
from gmpy2 import mpz, gcd, gcdext
from Crypto.Util.number import *
from random import randint
import functools

def chinese_remainder(a, m):
    sum = 0
    prod = functools.reduce(lambda x, y: x * y, m)
    for ai, mi in zip(a, m):
        Mi = prod // mi
        sum += ai * Mi * inverse(Mi, mi)
    return sum % prod

c1, c2, c3, n1, n2, e1, e2, enc, n, d = eval(open('./data.txt').read())

salt = pow(enc, d, n)

p = 166559812212375057424878757451426044287785611955610968659788093254234556174390568048691834754368288462237749046391701767757348180075441846081460002214756081408128278002709364521670995004638750806040451776758390579648021462920772773039547014422716935678539107571245420768792950941388211219311822431373244703657
q = 139554551381261963247214822373727623963972679707351312403181527456345895959922992181032008791771275669840278264225997669917935873557980268851629034297018293790658464886496865644152843958798712555520148550499593714695432457107763783516267887398663192127636665399947302340130821127242088025281598151564822846327
e = inverse(d, (p - 1) * (q - 1))

p1p2 = pow(c3, e, n)

p1 = gcd(p1p2, n1)
q1 = n1 // p1
print(gcd(e1, q1 - 1))
d1 = inverse(e1, (q1 - 1))
m2q1 = pow(c1, d1, q1)

p2 = gcd(p1p2, n2)
q2 = n2 // p2
print(gcd(e2, q2 - 1))
d2 = inverse(e2, (q2 - 1))
m2q2 = pow(c2, d2, q2)

z = Zmod(q1)
mq1 = int(z(m2q1).sqrt())
z = Zmod(q2)
mq2 = int(z(m2q2).sqrt())

for x in [(mq1, mq2), (mq1, -mq2), (-mq1, mq2), (-mq1, -mq2)]:
    flag = chinese_remainder(x, [q1, q2])
    print(long_to_bytes(flag ^^ salt))
