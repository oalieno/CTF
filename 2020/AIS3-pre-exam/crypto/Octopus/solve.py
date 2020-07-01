#!/usr/bin/env python3
from output import *
from Crypto.Util.number import *

bits = []
for i in range(1024):
    if Basis[i] == myBasis[i]:
        if Basis[i] == '+':
            bits.append(str(int(Qubits[i].imag == 1.0)))
        else:
            bits.append(str(int(Qubits[i].imag == -0.707)))

print(long_to_bytes(enc ^ int(''.join(bits[:400]), 2)))
