# SECCON Quals 2019 : Crazy-Repetition-of-Codes

**category** : crypto

**points** : 326

**solves** : 45

## write-up

CRC can be model as following calculation in Polynomial Ring of GF(2)

[list of crc functions](https://github.com/gsutil-mirrors/crcmod/blob/master/python3/crcmod/predefined.py#L49)

```
(M * x ^ n + Y + (Y + I) * x ^ b) % K
where
M = Input Message
K = Poly
Y = XOR-out
I = Init-value
n = size of K
b = size of M
```

If the crc function is in reverse mode,  
bitwise reverse the `M, K, Y, I` before the calculation ( The Poly column given in the previous link is already reverse in reverse mode ),  
and bitwise reverse the output after the calculation

You can test the below sage code  
The implementation using calculation in Polynomial Ring of GF(2) is identical to the challenge crc32 implementation

```python
def crc32(crc, data):
    crc = 0xFFFFFFFF ^^ crc
    for c in data:
        crc = crc ^^ c
        for i in range(8):
            crc = (crc >> 1) ^^ (0xEDB88320 * (crc & 1))
    return 0xFFFFFFFF ^^ crc

R.<x> = GF(2)['x']

def i2p(p):
    return R(Integer(p).bits())

def p2i(p):
    return Integer(p.list(), 2)

def rev(p, n):
    p = (p.list() + [0] * n)[:n]
    return R(p[::-1])

def crc32_(crc, data):
    n = 32
    b = len(data) * 8
    K = i2p(0x104C11DB7)
    M = i2p(int.from_bytes(data, 'little'))
    I = i2p(crc)
    Y = i2p(0xFFFFFFFF)
    crc = general_crc(K, M, I, Y, n, b, True)
    return p2i(crc)

def general_crc(K, M, I, Y, n, b, reverse):
    if reverse:
        M = rev(M, b)
        Y = rev(Y, n)
        I = rev(I, n)
    crc = (M * x ^ n + (Y + I) * x ^ b + Y) % K
    if reverse:
        crc = rev(crc, n)
    return crc

assert(crc32(0, b'test') == crc32_(0, b'test'))
```

Now we can calculate the power in challenge

```
let S = M * x ^ n + Y * x ^ b + Y
crc_0 = 0
crc_1 = S + crc_0 * x ^ b = S
crc_2 = S + crc_1 * x ^ b = S * (1 + x ^ b)
...
crc_k = S + crc_k-1 * x ^ b = S * (1 + x ^ b + ... + x ^ ((k - 1) * b))

let Z = S * (1 + x ^ b + ... + x ^ ((k - 1) * b))
(x ^ b) * Z = S * (x ^ b + x ^ (2 * b) + ... + x ^ (k * b))
(x ^ b - 1) * Z = S * (x ^ (k * b) - 1)
Z = S * (x ^ (k * b) - 1) / (x ^ b - 1)

All calculation above is under mod K
```

for more detail, read the source code [solve.sage](solve.sage)

flag: `SECCON{Ur_Th3_L0rd_0f_the_R1NGs}`

# other write-ups and resources
