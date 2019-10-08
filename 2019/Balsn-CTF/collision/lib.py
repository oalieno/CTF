import hashlib
import subprocess
import json
from Crypto.Cipher import AES, DES
from Crypto.Util.number import bytes_to_long, long_to_bytes


def omnihash(x):
    ret = subprocess.check_output(['omnihash', '-jcs'], input=x)
    return json.loads(ret)[0][0]


def printflag(x):
    # Update August, 2004 (commit 40de8d): MD5 is broken...
    if hashlib.sha1(x).hexdigest() != '3a4a6c4047f9350493cdabcf719d8e4f3b3c1f2f':
        print('I said you shall not pass!!!')
        return False
    
    # Update Feb, 2017 (commit 56fcd9): Fxxk, SHA1 is broken too
    if hashlib.sha3_224(x).hexdigest() != 'c529d3db40ac50bf3b5c1957b7ef4e632f6fb34ae83b165caed6658d':
        print('Why do you keep trying to hack into my home???? Go away QAQQQQQQ!!!!!')
        return False
    
    # Update May, 2019 (commit c10d5a): Check all well-known hashes

    # Destroy the value
    p = int("""\
    6816b2bba5ad70478c1beadb176b9ab17cb172841b10277f538f9d837f2\
    2bdd807b970605c63859c739571cc535fd0c6879149b2d2eb676a182fd7\
    5ff343e75a22ce75c36a775157c34f17\
    """.replace(' ', ''), 16)
    x = bytes_to_long(x)
    x = pow(x, 31337, p)
    x = long_to_bytes(x)
    
    # Destroy again
    for _ in range(10):
        k = x[:16]
        aes = AES.new(k, AES.MODE_CFB, k)
        x = aes.encrypt(x[16:]) + k

    # Destroy one more time
    x = b'QAQQAQQQ' + x
    for _ in range(10):
        k = hashlib.sha256(x[:8]).digest()[:8]
        des = DES.new(k, DES.MODE_CFB, k)
        x = k + des.encrypt(x[8:])

    # Check
    x = x + b'OAOOAOOO'
    hash = omnihash(x)
    with open('hash.json') as f:
        target = json.load(f)
    if all(hash[k] == v for k, v in target.items()):
        with open('../flag.txt') as f:
            print(f.read())
