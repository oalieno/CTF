#!/usr/bin/env python3
import gmpy2
import json

C = json.load(open('ciphertexts.txt'))
for c in C:
    m = int(gmpy2.iroot(int(c, 16), 3)[0])
    print(m.to_bytes(32, 'big'))
