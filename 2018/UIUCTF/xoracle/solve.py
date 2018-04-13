#!/usr/bin/env python3

L = 2039
klens = [136, 174, 203, 206]
C = []

for klen in klens:
    with open('data/c-{}'.format(klen), 'rb') as data:
        C.append(data.read())

for guess in range(0, 256):
    plain = [-1] * L
    keys = [[-1] * klens[i] for i in range(len(C))]
    for i in range(len(C)): keys[i][0] = guess ^ C[i][0]
    while True:
        change = False
        for i in range(len(C)):
            for j in range(L):
                if keys[i][j % klens[i]] != -1 and plain[j] == -1:
                    change = True
                    plain[j] = C[i][j] ^ keys[i][j % klens[i]]
                    for k in range(len(C)): keys[k][j % klens[k]] = plain[j] ^ C[k][j]
        if not change: break
    with open('data/m-{}'.format(guess), 'wb') as data:
        data.write(bytes(plain))
