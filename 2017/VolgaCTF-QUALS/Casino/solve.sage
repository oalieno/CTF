#!/usr/bin/env sage
from remote import remote

def guess(r, x):
    r.recvline()
    r.sendline(str(x))
    text = r.recvline().strip()
    stack = int(text.split(' ')[-1])
    if 'Wrong' in text:
        return int(text[22:].split('.')[0]), stack
    else:
        return x, stack

def ns(state, trans):
    return [i[0] for i in trans * matrix(GF(2), state).transpose()]

while True:
    r = remote('127.0.0.1', 20000)
    r.recvlines(3)

    n = []

    for i in range(20):
        n.append(guess(r, 0)[0])

    need = sum(map(lambda x: x <= 21, n))
    print need

    if need <= 10:
        break

# guess s
for p in range(2 ** need):
    s = []
    k = 0
    for v in n:
        if v <= 21:
            if (p & (1 << k)):
                v += 42
            k += 1
        s += list(map(int, '{:06b}'.format(v)))

    # guess m
    for m in range(24, 65):
        if len(s) < 2 * m + 10:
            break

        A = matrix(GF(2), [[s[i + j] for j in range(0, m)] for i in range(0, m)])
        B = matrix(GF(2), [s[i] for i in range(m, 2 * m)]).transpose()

        try:
            sol = A.solve_right(B)
            sol = [i[0] for i in sol]
        except ValueError:
            continue

        cm = []
        for i in range(1, m):
            row = [0] * (m - 1)
            row.insert(i, 1)
            cm.append(row)
        cm.append(sol)
        trans = matrix(GF(2), cm)

        state = [s[i] for i in range(m, 2 * m)]
        
        # check whether m is correct
        success = True
        for i in range(2 * m, len(s)):
            state = ns(state, trans)
            if s[i] != state[-1]:
                success = False
                break
        if not success:
            continue

        # increase stack
        while True:
            for i in range(6):
                state = ns(state, trans)
            _, stack = guess(r, int(''.join(map(str, state[-6:])), 2) % 42)
            if stack == 101:
                break
        print r.recvline().strip()
        exit(0)
