#!/usr/bin/env python3
import json
import hashlib
import functools
from Crypto.Cipher import AES, DES
from Crypto.Util.number import *

NON_REVERSE, REVERSE = 0, 1

_crc_definitions_table = [
    [   'crc-8',            'Crc8',             0x107,          NON_REVERSE,    0x00,           0x00,       0xF4,       ],
    [   'crc-8-darc',       'Crc8Darc',         0x139,          REVERSE,        0x00,           0x00,       0x15,       ],
    [   'crc-8-i-code',     'Crc8ICode',        0x11D,          NON_REVERSE,    0xFD,           0x00,       0x7E,       ],
    [   'crc-8-itu',        'Crc8Itu',          0x107,          NON_REVERSE,    0x55,           0x55,       0xA1,       ],
    [   'crc-8-maxim',      'Crc8Maxim',        0x131,          REVERSE,        0x00,           0x00,       0xA1,       ],
    [   'crc-8-rohc',       'Crc8Rohc',         0x107,          REVERSE,        0xFF,           0x00,       0xD0,       ],
    [   'crc-8-wcdma',      'Crc8Wcdma',        0x19B,          REVERSE,        0x00,           0x00,       0x25,       ],
    [   'crc-16',           'Crc16',            0x18005,        REVERSE,        0x0000,         0x0000,     0xBB3D,     ],
    [   'crc-16-buypass',   'Crc16Buypass',     0x18005,        NON_REVERSE,    0x0000,         0x0000,     0xFEE8,     ],
    [   'crc-16-dds-110',   'Crc16Dds110',      0x18005,        NON_REVERSE,    0x800D,         0x0000,     0x9ECF,     ],
    [   'crc-16-dect',      'Crc16Dect',        0x10589,        NON_REVERSE,    0x0001,         0x0001,     0x007E,     ],
    [   'crc-16-dnp',       'Crc16Dnp',         0x13D65,        REVERSE,        0xFFFF,         0xFFFF,     0xEA82,     ],
    [   'crc-16-en-13757',  'Crc16En13757',     0x13D65,        NON_REVERSE,    0xFFFF,         0xFFFF,     0xC2B7,     ],
    [   'crc-16-genibus',   'Crc16Genibus',     0x11021,        NON_REVERSE,    0x0000,         0xFFFF,     0xD64E,     ],
    [   'crc-16-maxim',     'Crc16Maxim',       0x18005,        REVERSE,        0xFFFF,         0xFFFF,     0x44C2,     ],
    [   'crc-16-mcrf4xx',   'Crc16Mcrf4xx',     0x11021,        REVERSE,        0xFFFF,         0x0000,     0x6F91,     ],
    [   'crc-16-riello',    'Crc16Riello',      0x11021,        REVERSE,        0x554D,         0x0000,     0x63D0,     ],
    [   'crc-16-t10-dif',   'Crc16T10Dif',      0x18BB7,        NON_REVERSE,    0x0000,         0x0000,     0xD0DB,     ],
    [   'crc-16-teledisk',  'Crc16Teledisk',    0x1A097,        NON_REVERSE,    0x0000,         0x0000,     0x0FB3,     ],
    [   'crc-16-usb',       'Crc16Usb',         0x18005,        REVERSE,        0x0000,         0xFFFF,     0xB4C8,     ],
    [   'x-25',             'CrcX25',           0x11021,        REVERSE,        0x0000,         0xFFFF,     0x906E,     ],
    [   'xmodem',           'CrcXmodem',        0x11021,        NON_REVERSE,    0x0000,         0x0000,     0x31C3,     ],
    [   'modbus',           'CrcModbus',        0x18005,        REVERSE,        0xFFFF,         0x0000,     0x4B37,     ],
    [   'kermit',           'CrcKermit',        0x11021,        REVERSE,        0x0000,         0x0000,     0x2189,     ],
    [   'crc-ccitt-false',  'CrcCcittFalse',    0x11021,        NON_REVERSE,    0xFFFF,         0x0000,     0x29B1,     ],
    [   'crc-aug-ccitt',    'CrcAugCcitt',      0x11021,        NON_REVERSE,    0x1D0F,         0x0000,     0xE5CC,     ],
    [   'crc-24',           'Crc24',            0x1864CFB,      NON_REVERSE,    0xB704CE,       0x000000,   0x21CF02,   ],
    [   'crc-24-flexray-a', 'Crc24FlexrayA',    0x15D6DCB,      NON_REVERSE,    0xFEDCBA,       0x000000,   0x7979BD,   ],
    [   'crc-24-flexray-b', 'Crc24FlexrayB',    0x15D6DCB,      NON_REVERSE,    0xABCDEF,       0x000000,   0x1F23B8,   ],
    [   'crc-32',           'Crc32',            0x104C11DB7,    REVERSE,        0x00000000,     0xFFFFFFFF, 0xCBF43926, ],
    [   'crc-32-bzip2',     'Crc32Bzip2',       0x104C11DB7,    NON_REVERSE,    0x00000000,     0xFFFFFFFF, 0xFC891918, ],
    [   'crc-32c',          'Crc32C',           0x11EDC6F41,    REVERSE,        0x00000000,     0xFFFFFFFF, 0xE3069283, ],
    [   'crc-32d',          'Crc32D',           0x1A833982B,    REVERSE,        0x00000000,     0xFFFFFFFF, 0x87315576, ],
    [   'crc-32-mpeg',      'Crc32Mpeg',        0x104C11DB7,    NON_REVERSE,    0xFFFFFFFF,     0x00000000, 0x0376E6E7, ],
    [   'posix',            'CrcPosix',         0x104C11DB7,    NON_REVERSE,    0xFFFFFFFF,     0xFFFFFFFF, 0x765E7680, ],
    [   'crc-32q',          'Crc32Q',           0x1814141AB,    NON_REVERSE,    0x00000000,     0x00000000, 0x3010BF7F, ],
    [   'jamcrc',           'CrcJamCrc',        0x104C11DB7,    REVERSE,        0xFFFFFFFF,     0x00000000, 0x340BC6D9, ],
    [   'xfer',             'CrcXfer',          0x1000000AF,    NON_REVERSE,    0x00000000,     0x00000000, 0xBD0BE338, ],
    [   'crc-64',           'Crc64',            0x1000000000000001B,    REVERSE,        0x0000000000000000, 0x0000000000000000, 0x46A5A9388A5BEFFE, ],
    [   'crc-64-we',        'Crc64We',          0x142F0E1EBA9EA3693,    NON_REVERSE,    0x0000000000000000, 0xFFFFFFFFFFFFFFFF, 0x62EC59E3F1A4F00A, ],
    [   'crc-64-jones',     'Crc64Jones',       0x1AD93D23594C935A9,    REVERSE,        0xFFFFFFFFFFFFFFFF, 0x0000000000000000, 0xCAA717168609F281, ],
]

G.<h> = GF(2)
R.<t> = GF(2)['t']

def i2p(n, t):
    ans = 0
    for i in bin(n)[2:]:
        ans *= t
        if i == '1':
            ans += 1
    return ans

def pbit(p, bit):
    pl = list(p)
    if bit < len(pl):
        return G(pl[bit])
    return G(0)

def _bitrev(x, n):
    y = 0
    for i in range(n):
        y = (y << 1) | (x & 1)
        x = x >> 1
    return y

def rev(x, bits):
    ans = []
    for i in range(0, bits, 8):
        ans += x[i:i+8][::-1]
    return ans

hashes = json.loads(open('hash.json').read().replace('[', '').replace(']', ''))
mbits = 91 * 8

ms = []
rs = []
for name, _, poly, reverse, init, xor, check in _crc_definitions_table:
    crc = int(hashes[name.upper()].strip('L'), 16)
    size = poly.nbits() - 1
    
    if reverse:
        crc = _bitrev(crc, size)
        init = _bitrev(init, size)
        xor = _bitrev(xor, size)
    
    k = i2p(poly, t)
    r = i2p(crc ^^ xor, t) + i2p(init ^^ xor, t) * (t ^ mbits)
    r = r * xgcd(t ^ size, k)[1] % k

    for bit in range(64):
        rs.append(pbit(r, bit))
        m = []
        for i in range(mbits):
            m.append(pbit(t ^ i % k, bit))
        if not reverse:
            m = rev(m, mbits)
        ms.append(m)

for i, bit in enumerate(f"{int.from_bytes(b'OAOOAOOO', 'little'):064b}"):
    m = [G(0)] * mbits
    m[i] = G(1)
    ms.append(m)
    rs.append(G(bit))

keys = []
k = b'QAQQAQQQ'
for _ in range(10):
    k = hashlib.sha256(k).digest()[:8]
    keys.append(k)

for i, bit in enumerate(f"{int.from_bytes(k, 'little'):064b}"):
    m = [G(0)] * mbits
    m[mbits - (8 * 8) + i] = G(1)
    ms.append(m)
    rs.append(G(bit))

A = matrix(ms)
v = vector(rs)
w = A.solve_right(v)

for kernel in A.right_kernel():
    m = int(''.join(map(str, kernel + w)), 2).to_bytes(mbits // 8, 'little')
    m = m[:-8]
   
    m = m[8:]
    for i in range(10):
        key = keys[10 - 1 - i]
        des = DES.new(key, DES.MODE_CFB, key)
        m = des.decrypt(m)

    for i in range(10):
        key = m[-16:]
        aes = AES.new(key, AES.MODE_CFB, key)
        m = key + aes.decrypt(m[:-16])

    p = int("""\
    6816b2bba5ad70478c1beadb176b9ab17cb172841b10277f538f9d837f2\
    2bdd807b970605c63859c739571cc535fd0c6879149b2d2eb676a182fd7\
    5ff343e75a22ce75c36a775157c34f17\
    """.replace(' ', ''), 16)
    m = bytes_to_long(m)
    d = inverse(31337, p - 1)
    m = pow(m, d, p)
    m = long_to_bytes(m)

    if hashlib.sha1(m).hexdigest() == '3a4a6c4047f9350493cdabcf719d8e4f3b3c1f2f':
        print(m.hex())
        break
