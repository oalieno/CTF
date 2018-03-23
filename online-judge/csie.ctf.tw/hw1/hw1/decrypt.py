import struct

with open('encrypt') as data:
    encrypt = data.read()

encrypt = struct.unpack('<{}i'.format(len(encrypt) / 4),encrypt)

ans = []

for index,word in enumerate(encrypt):
    x = (0xCCCCCCCD * (index + 2)) >> 35
    y = ((index + 1) << (((index + 2) - x * 10) & 0xFF)) & 0xFFFFFFFF
    ans += [(word - 0x2333) / y]

print ''.join(map(chr,ans))
