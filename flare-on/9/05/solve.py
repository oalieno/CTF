import hashlib
from base64 import *
from Crypto.Cipher import ARC4

def to_wide(x):
    return b''.join([bytes([i, 0]) for i in x])

def check_wide(x):
    for i, j in enumerate(x):
        if i % 2 == 1 and j != 0:
            return False
    return True

def gen_key(x):
    return to_wide(hashlib.md5(to_wide(x)).hexdigest().encode())

def rc4(key, m):
    return ARC4.new(key).encrypt(m)

enc_req = b64decode("ydN8BXq16RE=")
enc_res = b64decode("TdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg==")

for i in range(256 * 256):
    key = gen_key(b'FO9' + str(i).encode())
    dec_req = rc4(key, enc_req)
    if check_wide(dec_req):
        dec_res = rc4(key, enc_res)
        break

print(dec_req)
print(dec_res)
