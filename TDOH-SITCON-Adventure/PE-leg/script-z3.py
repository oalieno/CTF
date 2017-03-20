#!/usr/bin/env python

from z3 import *

flag = [ Int('input_{}'.format(i)) for i in xrange(84) ]

s = Solver()

for line in open("leg.txt"):
    s.add(eval(line))

if s.check() != sat:
    print "unsat"
else:
    m = s.model()
    flag = [ chr(m[i].as_long()) for i in flag ]
    print ''.join(flag)
