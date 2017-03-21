#!/usr/bin/env python

from z3 import *

NUM = 20
NUMBER = NUM*NUM

MAP = []

def convert(x,y):
    return x*NUM+y

for cols in range(NUMBER):
    now = [False]*NUMBER
    x = cols/NUM
    y = cols%NUM
    if x >= 2:
        now[convert(x-2,y)] = True
    if x+2 < NUM:
        now[convert(x+2,y)] = True
    if y >= 2:
        now[convert(x,y-2)] = True
    if y+2 < NUM:
        now[convert(x,y+2)] = True
    if x >= 1 and y >= 1:
        now[convert(x-1,y-1)] = True
    if x >= 1 and y+1 < NUM:
        now[convert(x-1,y+1)] = True
    if x+1 < NUM and y >= 1:
        now[convert(x+1,y-1)] = True
    if x+1 < NUM and y+1 < NUM:
        now[convert(x+1,y+1)] = True
    MAP.append(now)

input = [Bool("input_%d" % i) for i in range(NUMBER)]
state = [False]*NUMBER

for i in range(NUMBER):
    for j in range(NUMBER):
        state[i] = Xor(state[i],And(MAP[j][i],input[j]))

data = []
with open("normal-data.txt","r") as d:
    content = d.read()
    for i in content:
        if i == '0' or i == '1':
            data.append(i == '1')

s = Solver()
for i in range(NUMBER):
    s.add(state[i] == data[i])
if s.check() != sat:
    print "Unsat"
else:
    ans = s.model()
    ans_string = ""
    for i in range(NUMBER):
        if ans[input[i]] == True:
            ans_string += '1'
        else:
            ans_string += '0'
    with open("ans","w") as a:
        a.write(ans_string)
