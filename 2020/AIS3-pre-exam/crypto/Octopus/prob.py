import random
import numpy as np
from secret import FLAG, key_exchange

LENGTH = 1024

def rotate(phi):
    return 1 * ( np.cos(phi) + np.sin(phi)*1j )

def get_rect_random() :
    if random.randint(0,2**128) %2 == 0:
        return (1+0j)   # Arrow ↑
    return (0+1j)       # Arrow → 
    
def get_diagonal_random() :
    if random.randint(0,2**128) %2 == 0:
        return complex(0.707, +0.707)   # Arrow ↗
    return complex(0.707, -0.707)   # Arrow ↘

def rotate(q):
    # For diagonal basis measure
    return q * complex(0.707, -0.707)

basis = [random.choice('+x') for i in range(LENGTH)]
qubits = [get_rect_random() if b == '+' else get_diagonal_random() for b in basis ]

print("Basis   : ", basis)
print("Qubits  : ", qubits)

myBasis = [random.choice('+x') for i in range(LENGTH)]

print("myBasis : ", myBasis)

bit_stream = key_exchange(qubits, basis, myBasis)

print(int(bit_stream[:400],2) ^ FLAG)
