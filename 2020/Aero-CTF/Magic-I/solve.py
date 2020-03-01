from Crypto.Util.number import *

y = 51985830717457237488973954964904090788909
x = 2 * y + 1
key = (x ** 3 - x) // 2
enc = 0xd9a103a6006bfba17074ef571011d8eededdf851b355bdc4795616744066433695b9e9201f6deff7577c03ba690d4d517bdaae
flag = key ^ enc
print(long_to_bytes(flag))
