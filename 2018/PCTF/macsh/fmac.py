from Crypto import Random
from Crypto.Cipher import AES
from functools import reduce

N = AES.block_size

def to_int(b):
    return int(bytes.hex(b), 16)

def to_block(b):
    return bytes.fromhex('{:0{width}x}'.format(b, width=N*2))

def xor(x, y):
    return bytes([xe ^ ye for xe,ye in zip(x,y)])

def to_blocks(m):
    m += to_block(len(m))
    padb = N - len(m) % N
    m += bytes([padb]) * padb
    blocks = [m[N*i : N*(i+1)] for i in range(len(m) // N)]
    return blocks

def rot(n, c):
    return (n >> c) | ((n & ((1 << c) - 1)) << (8 * N - c))

def f(k0, i):
    return to_block(rot(to_int(k0), i % (8 * N)))

def fmac(k0, k1, m):
    C = AES.new(k1, AES.MODE_ECB)
    bs = [C.encrypt(xor(b, f(k0, i))) for i,b in enumerate(to_blocks(m))]
    return reduce(xor, bs, b"\x00" * N)

def keygen():
    R = Random.new()
    return R.read(N), R.read(N)
