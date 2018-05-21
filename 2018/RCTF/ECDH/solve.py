#!/usr/bin/env python3
from Crypto.Cipher import AES

key = iv = b'\x00' * 16
cipher = bytes.fromhex('6f5e276e357d625110afebf97aeb49453bd97b63774a639a7c71bcee0da2d192')

aes = AES.new(key, AES.MODE_ECB, iv)
plain = aes.decrypt(cipher)
print(plain)
