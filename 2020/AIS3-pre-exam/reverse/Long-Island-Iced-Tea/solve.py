#!/usr/bin/env python3
import string
import subprocess

def oracle(m):
    p = subprocess.Popen(["./Long_Island_Iced_tea"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate(m)
    return out.split(b'\n')[-1]

for i in string.printable:
    for j in string.printable:
        for k in 'gG9':
            # AIS3{A!girl_g1v3_m3_Ur_IG_4nd_th1s_1s_m1ne_terryterry__}
            m = b'AIS3{' + bytes([ord(i), ord(j), ord(k)]) + b'irl_g1v3_m3_Ur_IG_4nd_th1s_1s_m1ne_terryterry__}'
            print(m)
            c = oracle(m)
            print(c)
            if c[:4] == b'850a2a4d3fac148269726c5f673176335f6d335f55725f49475f346e645f746831735f31735f6d316e655f746572727974657272795f5f7d0000000000000000'[:4]:
                print('found')
                print(m)
                exit()
